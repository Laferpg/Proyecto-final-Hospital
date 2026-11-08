
from models.medico import Medico
from models.paciente import Paciente
from models.enfermero import Enfermero, Turno
from models.excepciones import PersonaDuplicadaError

class PersonaController:
    
    def __init__(self):
        self.personas = [] 

    def _verificar_identificacion(self, identificacion):
        for persona in self.personas:
            if persona.get_identificacion() == identificacion:
                raise PersonaDuplicadaError(
                    f"Ya existe una persona con identificación {identificacion} "
                    f"({persona.obtener_rol()}: {persona.get_nombre()})"
                )

    def añadir_medico(self, identificacion, nombre, correo, num_celular, codigo_empleado, estado, especialidad):
        self._verificar_identificacion(identificacion)
        medico = Medico(identificacion, nombre, correo, num_celular, codigo_empleado, estado, especialidad)
        self.personas.append(medico)
        return medico
        
    def añadir_paciente(self, identificacion, nombre, correo, num_celular, historia_clinica, fecha_nacimiento,
                        genero, tipo_sangre, alergias, antecedentes_personales, antecedentes_familiares, eps):
        self._verificar_identificacion(identificacion)
        paciente = Paciente(identificacion, nombre, correo, num_celular, historia_clinica, fecha_nacimiento,
                            genero, tipo_sangre, alergias, antecedentes_personales, antecedentes_familiares, eps)
        self.personas.append(paciente)
        return paciente
        
    def añadir_enfermero(self, identificacion, nombre, correo, num_celular, Idempleado, turno:Turno):
        self._verificar_identificacion(identificacion)
        enfermero = Enfermero(identificacion, nombre, correo, num_celular, Idempleado, turno)
        self.personas.append(enfermero)
        return enfermero
        
    def get_persona(self):
        return self.personas.copy()
