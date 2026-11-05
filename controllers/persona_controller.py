
from models.medico import Medico
from models.paciente import Paciente
from models.enfermero import Enfermero

class PersonaController:
    
    def __init__(self):
        self.personas = [] #se crea la lista

    def añadir_medico(self, identificacion, nombre, correo, codigo, estado, especialidad):
        
        for persona in self.personas:
            if persona.get_identificacion() == identificacion:
                raise ValueError(
                f"Ya existe una persona con identificación {identificacion}"
            )
        
        medico=Medico(identificacion, nombre, correo, codigo, estado, especialidad)
        self.personas.append(medico)
        
    def añadir_paciente(self, identificacion, nombre, correo, historia_cLinica, fecha_naciemiento, genero, eps):
        paciente=Paciente(identificacion, nombre, correo, historia_cLinica, fecha_naciemiento, genero, eps)
        self.personas.append(paciente)
        
    def añadir_enfermero(self, identificacion, nombre, correo, Idempleado, turno):
        enfermero=Enfermero(identificacion, nombre, correo, Idempleado, turno)
        self.personas.append(enfermero)
        
    def get_persona(self):
        return self.personas.copy()