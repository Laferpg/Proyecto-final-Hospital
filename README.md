# Sistema de Gestión de Hospitalización
Proyecto final (Actividad Colaborativa N.º 3) — Programación I, Universidad de Manizales.

Sistema en Python, construido con Programación Orientada a Objetos, que gestiona el ciclo de una hospitalización: el **ingreso** del paciente con sus datos clínicos de admisión, la **asignación de una cama** dentro de la estructura del hospital (zonas, habitaciones y camas) y la **salida**, que libera la cama. Además conserva el historial de ingresos de cada paciente y registra al personal asistencial (médicos y enfermeros).

## Integrantes
- María José Osorio Giraldo - @MariaJose1220
- Laura Fernanda Pérez Galvis - @Laferpg
- Juan Camilo Pérez Oviedo - @juankp86

## Estructura del proyecto
```
~ main.py                     -> Archivo principal: crea los controladores e inicia el menú
~ demostracion.py             -> Demostración automática con casos normales y excepcionales
~ README.md
~ menu
   - menu_principal.py        -> Menú principal y submenús de registro y búsqueda
   - metodos.py               -> Funciones auxiliares (ingreso, alta, búsquedas, mostrar personas)
~ controllers
   - persona_controller.py    -> Guarda médicos, enfermeros y pacientes en una sola lista
   - especialidad_controller.py
   - zona_controller.py
   - ingreso_controller.py
~ models
   - personas.py              -> Clase abstracta Personas
   - medico.py, enfermero.py, paciente.py -> Clases hijas de Personas
   - especialidad.py          -> Especialidad médica (asociada al médico)
   - zona.py                  -> Zona del hospital (contiene habitaciones)
   - habitacion.py            -> Habitación (contiene camas)
   - cama.py                  -> Cama con su estado
   - ingreso.py               -> Ingreso de un paciente a una cama
   - salida.py                -> Salida que cierra un ingreso
   - excepciones.py           -> Excepciones personalizadas
```

## Ejecución
Requiere Python 3.10 o superior (el menú usa `match`). No necesita librerías externas.
```bash
git clone https://github.com/Laferpg/Proyecto-final-Hospital.git
cd Proyecto-final-Hospital
python main.py
```

Menú principal:
1. **Registro:** especialidad, médico, enfermero, paciente, zona, habitación, cama e ingreso.
2. **Dar de alta** a un paciente (crea la salida y libera la cama).
3. **Buscar** una persona, zona, habitación o cama.
4. **Mostrar personas registradas** (polimorfismo).
5. **Ejecutar la demostración del sistema** (crea los objetos de prueba y ejecuta todos los casos).
6. **Salir.**

Orden recomendado para registrar por teclado: especialidad → médico → paciente → zona → habitación → cama → ingreso.

## Conceptos aplicados

### Clase abstracta, herencia y sobrescritura
`Personas` hereda de `ABC` y declara como abstractos `mostrar_informacion()` y `obtener_rol()`, por lo que no se puede instanciar (Python lanza `TypeError`). `Medico`, `Enfermero` y `Paciente` heredan de ella (un médico *es una* persona), llaman a `super().__init__()` y sobrescriben los dos métodos con sus datos propios.

### Polimorfismo
`PersonaController` guarda médicos, enfermeros y pacientes en una sola lista. La opción 4 del menú y la sección 4 de la demostración la recorren con un único ciclo que llama `obtener_rol()` y `mostrar_informacion()` sin condicionales de tipo.

### Composición
`Zona.agregar_habitacion()` crea la habitación dentro de la zona, y `Habitacion.agregar_cama()` crea la cama dentro de la habitación, controlando su capacidad. Las partes no existen fuera del todo. No es herencia porque una cama no *es* una habitación: la habitación *tiene* camas.

### Relaciones entre objetos
- `Medico` → `Especialidad` (recibe el objeto, no un texto).
- `Ingreso` → `Paciente` e `Ingreso` → `Cama`.
- `Ingreso` → `Salida` (cero o una por ingreso).
- `Paciente` guarda su historial de ingresos.

### Excepciones personalizadas
Definidas en `models/excepciones.py`, todas heredan de `HospitalError`:

| Excepción | Situación | Se lanza en |
|---|---|---|
| `CamaNoDisponibleError` | Asignar una cama ocupada o en mantenimiento | `Cama.ocupar()` (llamado desde `Ingreso.set_cama()`) |
| `CapacidadHabitacionError` | Agregar más camas que la capacidad de la habitación | `Habitacion.agregar_cama()` |
| `PersonaDuplicadaError` | Registrar una identificación que ya existe | `PersonaController` |

Se capturan con `try/except` en el menú y en la demostración, se muestra un mensaje claro y el programa continúa.

## Diagrama UML y documento
- Diagrama de clases: ver la carpeta `docs/`.
- Documento de Decisiones de Diseño: ver la carpeta `docs/`.

## Uso de inteligencia artificial
El uso de herramientas de inteligencia artificial se declara en el Documento de Decisiones de Diseño.
