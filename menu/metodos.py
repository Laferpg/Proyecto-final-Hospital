from models.paciente import Paciente
from models.salida import TipoSalida

def elegir_especialidad(lista):

    print("\nEspecialidades registradas:")
    for i, especialidad in enumerate(lista, start=1):
        print(f"{i}. {especialidad.get_nombre()}")

    while True:
        opcion = int(input("Seleccione la especialidad: "))

        if 1 <= opcion <= len(lista):
            return lista[opcion - 1]
                      
def buscar_persona(personas, identificacion):
    for persona in personas:
        if persona.get_identificacion() == identificacion:
            return persona
    return None

def buscar_zona(zonas, nombre):
    for zona in zonas:
        if zona.get_nombre().lower() == nombre.lower():
            return zona
    return None

def buscar_habitacion(habitaciones, numero):
    for habitacion in habitaciones:
        if habitacion.get_num_habitacion() == numero:
            return habitacion
    return None

def buscar_cama(camas, codigo):
    for cama in camas:
        if cama.get_codigo() == codigo:
            return cama
    return None    

def registrar_ingreso(persona_controller,
                      zona_controller,
                      ingreso_controller):

    pacientes = []    # Se selecciona el paciente a ingresar a hospitalizacion
    for persona in persona_controller.get_persona():
        if isinstance(persona, Paciente):
            pacientes.append(persona)
    if not pacientes:
        print("No existen pacientes registrados.")
        return
    print("\nPACIENTES EN Sistema")
    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. {paciente.get_nombre()}")
    opcion_paciente = int(input("Seleccione paciente: ")) - 1
    paciente = pacientes[opcion_paciente]

    camas_disponibles = []  # Se le da una cama al paciente
    for zona in zona_controller.get_zonas():
        for habitacion in zona.get_habitaciones():
            for cama in habitacion.camas_libres():
                camas_disponibles.append(cama)
    if not camas_disponibles:
        print("No hay camas disponibles.")
        return
    print("\nCAMAS DISPONIBLES")
    for i, cama in enumerate(camas_disponibles, start=1):
        print(f"{i}. {cama.get_codigo()}")
    opcion_cama = int(input("Seleccione cama: ")) - 1
    cama = camas_disponibles[opcion_cama]
    
    codigo = input("Código de ingreso: ")
    fecha_ingreso = input("Fecha de ingreso: ")
    motivo_ingreso = input("Motivo de ingreso: ")

    escala_dolor = int(
        input("Escala de dolor (0 a 10): ")
    )

    estado_conciencia = input(
        "Estado de conciencia: "
    )

    requiere_aislamiento = (
        input("¿Requiere aislamiento? (S/N): ")
        .upper() == "S"
    )

    riesgo_caida = (
        input("¿Riesgo de caída? (S/N): ")
        .upper() == "S"
    )

    diagnostico = input("Diagnóstico: ")

    ingreso_controller.añadir_ingreso( paciente, codigo, fecha_ingreso, motivo_ingreso, escala_dolor, estado_conciencia, requiere_aislamiento, riesgo_caida, diagnostico, cama)
    print("Ingreso registrado correctamente.")


def dar_alta_paciente(ingreso_controller):

    ingresos = ingreso_controller.get_ingresos()
    if not ingresos:
        print("No existen ingresos registrados.")
        return
    print("\nINGRESOS")

    for i, ingreso in enumerate(ingresos, start=1):
        print(
            f"{i}. {ingreso.get_codigo()} - "
            f"{ingreso.get_paciente().get_nombre()}"
        )
    opcion = int(input("Seleccione ingreso: ")) - 1
    ingreso = ingresos[opcion]
    print("1. Alta")
    print("2. Remisión")
    print("3. Fallecimiento")

    tipo = input("Seleccione tipo: ")
    if tipo == "1":
        tipo_salida = TipoSalida.alta
    elif tipo == "2":
        tipo_salida = TipoSalida.remision
    else:
        tipo_salida = TipoSalida.fallecimiento

    fecha_salida = input("Fecha salida: ")
    diagnostico_final = input("Diagnóstico final: ")
    indicaciones = input("Indicaciones: ")

    ingreso.dar_alta(
        fecha_salida,
        tipo_salida,
        diagnostico_final,
        indicaciones
    )
    print("Paciente dado de alta correctamente.")