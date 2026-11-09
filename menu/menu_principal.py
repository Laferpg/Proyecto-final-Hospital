from models.enfermero import Turno
from models.habitacion import EstadoHabitacion
from models.cama import EstadoCama
from menu.metodos import registrar_ingreso,buscar_persona,buscar_zona,buscar_cama,buscar_habitacion,elegir_especialidad
from menu.metodos import dar_alta_paciente, registrar_ingreso
from models.excepciones import PersonaDuplicadaError


def agregar(
            persona_controller,
            especialidad_controller,
            ingreso_controller,
            zona_controller,
            cama_controller,
            habitacion_controller
):
    while True:
        print("\nQue elemento desea reguistar en el sistema")
        print("1. Registrar especialidad")
        print("2. Registrar médico")
        print("3. Registrar enfermero")
        print("4. Registrar paciente")
        print("5. Registrar zona")
        print("6. Registrar habitación")
        print("7. Registrar cama")
        print("8. Registrar ingreso")
        
        option = input("Selecciona una opción: ")
        
        match option:
            
            case "1":
                print("\nREGISTRO ESPECIALIDAD")
                codigo=input("Ingresa el código de la especialidad: ")
                nombre = input("Ingrese el nombre de la especialidad: ")

                especialidad_controller.añadir_especialidad(codigo, nombre)
                print("La especialidad se ha agregado con éxito") 
            
            case "2":
                print("\nREGISTRO MÉDICO")
                if  not especialidad_controller.get_especialidades():
                    print("Primero debe registrar al menos una especialidad")
                    continue
                identificacion = input("Identificación: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                celular = input("Celular: ")
                codigo_empleado = input("Código empleado: ")
                estado = input("Estado: ")
                especialidad = elegir_especialidad(especialidad_controller.get_especialidades())
                try:
                    persona_controller.añadir_medico(identificacion, nombre, correo, celular, codigo_empleado, estado, especialidad)
                    print("Médico registrado correctamente.")
                except PersonaDuplicadaError as e:
                    print("Intenta registrar una persona con una identificación que ya existe en el sistema\n")
                
            case "3":
                print("\nREGISTRO ENFERMERO")
                identificacion = input("Identificación: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                celular = input("Celular: ")
                id_empleado = input("ID empleado: ")
                print("1. Diurno")
                print("2. Nocturno")
                opcion_turno = input("Seleccione turno: ")
                if opcion_turno == "1":
                    turno = Turno.diurno
                else:
                    turno = Turno.nocturno
                try:
                    persona_controller.añadir_enfermero(identificacion, nombre, correo, celular, id_empleado, turno)
                    print("Enfermero registrado correctamente.")
                except PersonaDuplicadaError as e:
                    print("Intenta registrar una persona con una identificación que ya existe en el sistema\n")
                
            case "4":
                print("\nREGISTRO PACIENTE")
                identificacion = input("Identificación: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                celular = input("Celular: ")
                historia_clinica = input("Historia clínica: ")
                fecha_nacimiento = input("Fecha nacimiento: ")
                genero = input("Género: ")
                tipo_sangre = input("Tipo de sangre: ")
                alergias = input("Alergias: ")
                antecedentes_personales = input("Antecedentes personales: ")
                antecedentes_familiares = input("Antecedentes familiares: ")
                eps = input("EPS: ")
                try:
                    persona_controller.añadir_paciente(identificacion, nombre, correo, celular, historia_clinica, fecha_nacimiento, genero, tipo_sangre, alergias, antecedentes_personales, antecedentes_familiares, eps)
                    print("Paciente registrado correctamente.")
                except PersonaDuplicadaError as e:
                    print("Intenta registrar una persona con una identificación que ya existe en el sistema\n")
                         
            case "5":
                print("\nREGISTRO ZONA")
                nombre = input("Nombre de la zona: ")
                piso = int(input("Piso: "))
                zona_controller.añadir_zona(nombre, piso)
                print("Zona registrada correctamente.")
            
            case "6":
                print("\nREGISTRO HABITACION")
                if not habitacion_controller.get_habitaciones():
                    print("Primero debe registrar al menos una zona")
                    
                    for i, zona in enumerate(zonas, start=1):
                            print(f"{i}. {zona.get_nombre()}")
                            
                            opcion_zona = int(
                            input("Seleccione la zona: ")) - 1
                            zona = zonas[opcion_zona]
                            continue
                num_habitacion = int(input("Número de habitación: "))
                capacidad_camas = int(input("Capacidad camas: "))
                print("1. Disponible")
                print("2. Ocupada")
                print("3. Mantenimiento")
                op_estado = input("Seleccione estado: ")
                if op_estado == "1":
                    estado = EstadoHabitacion.disponible
                elif op_estado == "2":
                    estado = EstadoHabitacion.ocupada
                else:
                    estado = EstadoHabitacion.mantenimiento
                habitacion_controller.añadir_habitacion(num_habitacion, capacidad_camas, estado)
                zona.agregar_habitacion_existente(habitacion)
                print("Habitación registrada correctamente.")
                
            case "7":
                print("\nREGISTRO CAMA")
                habitaciones = habitacion_controller.get_habitaciones()
                
                if not habitaciones:
                    print("Primero debe registrar una habitación")
                    continue
                
                for i, habitacion in enumerate(habitaciones, start=1):
                    print(f"{i}. Habitación "
                          f"{habitacion.get_num_habitacion()}")
                    opcion = int(
                        input("Seleccione la habitación: ")) - 1
                    
                    habitacion = habitaciones[opcion]
                    codigo = input("Código cama: ")
                    print("\nEstado de la cama")
                    print("1. Disponible")
                    print("2. Ocupada")
                    print("3. Mantenimiento")
                    op = input("Seleccione estado: ")
                    if op == "1":
                        estado = EstadoCama.disponible
                    elif op == "2":
                        estado = EstadoCama.ocupada
                    elif op == "3":
                        estado = EstadoCama.mantenimiento
                    else:
                        print("Opción inválida")
                        continue
                    
                    habitacion.agregar_cama(codigo, estado)
                    
                    cama_controller.agregar_cama(codigo, estado)
                    print("Cama registrada correctamente.")
            
            case "8":
                print("\nREGISTRO DE INGRESO A PISO DE HOSPITALIZACION")
                
                registrar_ingreso(persona_controller, zona_controller, ingreso_controller)
            
def buscar(
        persona_controller,
        zona_controller,
        habitacion_controller,
        cama_controller
):

    while True:

        print("\nQue desea buscar")
        print("1. Buscar una persona")
        print("2. Buscar zonas")
        print("3. Buscar una habitación")
        print("4. Buscar una cama")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":

                identificacion = input( "Ingrese la identificación: ")
                persona = buscar_persona(
                    persona_controller.get_persona(),
                    identificacion
                )
                if persona:
                    print("\nPersona encontrada")
                    print(persona.mostrar_informacion())
                else:
                    print("Persona no encontrada")

            case "2":
                nombre = input("Ingrese el nombre de la zona: ")

                zona = buscar_zona(
                    zona_controller.get_zonas(),
                    nombre
                )

                if zona:
                    print(f"\nZona: {zona.get_nombre()}")
                    print(
                        f"Piso: {zona.get_piso()}"
                    )
                else:
                    print("Zona no encontrada")

            case "3":

                numero = int(
                    input("Ingrese el número de habitación: "))

                habitacion = buscar_habitacion(
                    habitacion_controller.get_habitaciones(),numero
                )

                if habitacion:
                    print(
                        habitacion.mostrar_informacion()
                    )
                else:
                    print("Habitación no encontrada")

            case "4":

                codigo = input("Ingrese el código de la cama: ")

                cama = buscar_cama(
                    cama_controller.get_camas(),codigo
                )

                if cama:
                    print(
                        cama.mostrar_informacion()
                    )
                else:
                    print("Cama no encontrada")

            case "5":
                break

            case _:
                print("Opción inválida")


def menu_principal(
    persona_controller,
    especialidad_controller,
    ingreso_controller,
    zona_controller,
    cama_controller,
    habitacion_controller
    
):
    
    while True:
       print("\n Bienvenido a su sistema de gestion de piso de Hospitalización")
       print("\n Seleccione la funcion desea realizar")
       print("1. Reguistro" )
       print("2. Dar de alta")
       print("3. Buscar")
       print("4. Salir")
       
       
       option = input("Selecciona una opción: ")
       try:
        match option:
                     case "1":
                        agregar(
                            persona_controller,
                            especialidad_controller,
                            ingreso_controller,
                            zona_controller,
                            cama_controller,
                            habitacion_controller
                           )
                     
                     case "2":
                       dar_alta_paciente(ingreso_controller)

                        
                     case "3":
                        buscar(
                            persona_controller,
                            zona_controller,
                            habitacion_controller,
                            cama_controller
                            )
                
                     case "4":
                        print("Vuelve pronto")
                        break
                
                     case _:
                        print("Opción inválida")
       except ValueError as error:
                print(f"Dato inválido: {error}. No se guardaron los cambios.")
