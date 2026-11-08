from models.especialidad import Especialidad

class EspecialidadController:
    
    def __init__(self):
        self._especialidades = []
        
    def añadir_especialidad(self, codigo, nombre):
        especialidad = Especialidad(codigo, nombre)
        self._especialidades.append(especialidad)
        
    def get_especialidades(self):
        return self._especialidades.copy()