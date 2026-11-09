"""
Demostración automática del sistema de hospitalización.
Crea los objetos de prueba y ejecuta los casos normales y los casos
excepcionales pedidos en la Actividad Colaborativa N.º 3.
Se ejecuta desde la opción 5 del menú principal.
"""
from models.personas import Personas
from models.enfermero import Turno
from models.habitacion import EstadoHabitacion
from models.cama import EstadoCama
from models.salida import TipoSalida
from models.excepciones import CamaNoDisponibleError, CapacidadHabitacionError, PersonaDuplicadaError
from controllers.persona_controller import PersonaController
from controllers.especialidad_controller import EspecialidadController
from controllers.zona_controller import ZonaController
from controllers.ingreso_controller import IngresoController


def titulo(texto):
    print("\n" + "=" * 70)
    print(texto)
    print("=" * 70)


def ejecutar_demostracion():
    persona_controller = PersonaController()
    especialidad_controller = EspecialidadController()
    zona_controller = ZonaController()
    ingreso_controller = IngresoController()

    # ------------------------------------------------------------------
    titulo("1. CLASE ABSTRACTA: no se puede crear una persona sin rol")
    try:
        Personas("000", "Persona sin rol", "sinrol@hospital.co", "3000000000")
    except TypeError as error:
        print(f"No se pudo crear la persona: {error}")
        print("Personas es abstracta: toda persona debe ser médico, paciente o enfermero.")

    # ------------------------------------------------------------------
    titulo("2. REGISTRO DE ESPECIALIDADES Y PERSONAL")
    cirugia = especialidad_controller.añadir_especialidad("ESP-01", "Cirugía general")
    ginecologia = especialidad_controller.añadir_especialidad("ESP-02", "Ginecología y obstetricia")

    medico1 = persona_controller.añadir_medico("1001", "Carlos Gómez", "cgomez@hospital.co", "3101112233",
                                               "MED-01", "En turno", cirugia)
    medico2 = persona_controller.añadir_medico("1002", "Ana Restrepo", "arestrepo@hospital.co", "3102223344",
                                               "MED-02", "Descansando", ginecologia)
    enfermero1 = persona_controller.añadir_enfermero("2001", "Luis Ramírez", "lramirez@hospital.co", "3113334455",
                                                     "ENF-01", Turno.diurno)
    enfermero2 = persona_controller.añadir_enfermero("2002", "Sofía Castaño", "scastano@hospital.co", "3114445566",
                                                     "ENF-02", Turno.nocturno)
    print(f"Especialidades registradas: {len(especialidad_controller.get_especialidades())}")
    print(f"Médicos: {medico1.get_nombre()} y {medico2.get_nombre()}")
    print(f"Enfermeros: {enfermero1.get_nombre()} y {enfermero2.get_nombre()}")

    # ------------------------------------------------------------------
    titulo("3. REGISTRO DE PACIENTES")
    paciente1 = persona_controller.añadir_paciente("3001", "Mariana Martínez", "mmartinez@correo.co", "3125556677",
                                                   "HC-3001", "2001-04-12", "Femenino", "O+", "Ninguna",
                                                   "Ninguno", "Hipertensión (madre)", "Sura")
    paciente2 = persona_controller.añadir_paciente("3002", "Pedro Salazar", "psalazar@correo.co", "3136667788",
                                                   "HC-3002", "1958-09-30", "Masculino", "A+", "Penicilina",
                                                   "Diabetes tipo 2", "Ninguno", "Nueva EPS")
    paciente3 = persona_controller.añadir_paciente("3003", "Valentina Ríos", "vrios@correo.co", "3147778899",
                                                   "HC-3003", "1995-01-25", "Femenino", "B-", "Ninguna",
                                                   "Ninguno", "Ninguno", "Sanitas")
    print(f"Pacientes registrados: {paciente1.get_nombre()}, {paciente2.get_nombre()} y {paciente3.get_nombre()}")

    # ------------------------------------------------------------------
    titulo("4. POLIMORFISMO: una sola colección y un único ciclo")
    print("La lista contiene médicos, enfermeros y pacientes mezclados.")
    print("El ciclo llama los mismos métodos sobre todos, sin preguntar el tipo de cada objeto.\n")
    for persona in persona_controller.get_persona():
        print(f">>> Rol: {persona.obtener_rol()}")
        print(persona.mostrar_informacion())
        print("-" * 40)

    # ------------------------------------------------------------------
    titulo("5. COMPOSICIÓN: la zona crea sus habitaciones y la habitación crea sus camas")
    zona_general = zona_controller.añadir_zona("Hospitalización general", 4)
    zona_maternidad = zona_controller.añadir_zona("Maternidad", 3)

    hab426 = zona_general.agregar_habitacion(426, 2, EstadoHabitacion.disponible)
    cama426A = hab426.agregar_cama("426A", EstadoCama.disponible)
    cama426B = hab426.agregar_cama("426B", EstadoCama.disponible)

    hab412 = zona_general.agregar_habitacion(412, 1, EstadoHabitacion.mantenimiento)
    cama412A = hab412.agregar_cama("412A", EstadoCama.mantenimiento)

    hab310 = zona_maternidad.agregar_habitacion(310, 2, EstadoHabitacion.disponible)
    cama310A = hab310.agregar_cama("310A", EstadoCama.disponible)
    hab310.agregar_cama("310B", EstadoCama.disponible)

    for zona in zona_controller.get_zonas():
        print(f"\nZona: {zona.get_nombre()} (piso {zona.get_piso()}) - "
              f"{zona.cantidad_habitaciones()} habitación(es)")
        for habitacion in zona.get_habitaciones():
            print(habitacion.mostrar_informacion())

    # ------------------------------------------------------------------
    titulo("6. INGRESOS: asignación de camas a pacientes")
    ingreso1 = ingreso_controller.añadir_ingreso(paciente2, "ING-001", "2026-11-08", "Dolor abdominal intenso", 8,
                                                 "Alerta", False, True, "Apendicitis aguda", cama426A)
    ingreso2 = ingreso_controller.añadir_ingreso(paciente1, "ING-002", "2026-11-08", "Trabajo de parto", 6,
                                                 "Alerta", False, False, "Embarazo a término", cama310A)
    print()
    print(ingreso1.mostrar_informacion())
    print()
    print(zona_general.mostrar_camas_disponibles())

    # ------------------------------------------------------------------
    titulo("7. CASOS EXCEPCIONALES")

    print("\n--- Excepción 1: asignar una cama que ya está ocupada ---")
    try:
        ingreso_controller.añadir_ingreso(paciente3, "ING-003", "2026-11-08", "Fractura de cadera", 9,
                                          "Alerta", False, True, "Fractura de fémur", cama426A)
    except CamaNoDisponibleError as error:
        print(f"Error: {error}")
    print("El programa continúa. El ingreso no se creó y la cama 426A sigue con su paciente.")

    print("\n--- Excepción 1 (otro caso): asignar una cama en mantenimiento ---")
    try:
        ingreso_controller.añadir_ingreso(paciente3, "ING-003", "2026-11-08", "Fractura de cadera", 9,
                                          "Alerta", False, True, "Fractura de fémur", cama412A)
    except CamaNoDisponibleError as error:
        print(f"Error: {error}")
    print("El programa continúa. Se busca otra cama para la paciente:")
    ingreso3 = ingreso_controller.añadir_ingreso(paciente3, "ING-003", "2026-11-08", "Fractura de cadera", 9,
                                                 "Alerta", False, True, "Fractura de fémur", cama426B)

    print("\n--- Excepción 2: agregar más camas de las que caben en la habitación ---")
    try:
        hab426.agregar_cama("426C", EstadoCama.disponible)
    except CapacidadHabitacionError as error:
        print(f"Error: {error}")
    print(f"El programa continúa. La habitación 426 sigue con {len(hab426.get_camas())} camas.")

    print("\n--- Excepción 3: registrar una persona con una identificación que ya existe ---")
    try:
        persona_controller.añadir_enfermero("1001", "Jorge Pérez", "jperez@hospital.co", "3158889900",
                                            "ENF-03", Turno.diurno)
    except PersonaDuplicadaError as error:
        print(f"Error: {error}")
    print(f"El programa continúa. Personas registradas: {len(persona_controller.get_persona())}")

    # ------------------------------------------------------------------
    titulo("8. SALIDA DEL PACIENTE: la cama vuelve a quedar disponible")
    ingreso1.dar_alta("2026-11-11", TipoSalida.alta, "Apendicectomía sin complicaciones",
                      "Reposo por 15 días y control en una semana")
    print(ingreso1.mostrar_informacion())
    print()
    print(zona_general.mostrar_camas_disponibles())

    # ------------------------------------------------------------------
    titulo("9. RESUMEN FINAL")
    for ingreso in ingreso_controller.get_ingresos():
        print(f"{ingreso.get_codigo()} | {ingreso.get_paciente().get_nombre()} | "
              f"Cama {ingreso.get_cama().get_codigo()} | {ingreso.get_estado().value}")
    print()
    print(paciente2.historial_ingresos())
    print("Fin de la demostración. El sistema se ejecutó completo después de todas las excepciones.")
