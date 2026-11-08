from models.personas import Personas
from models.especialidad import Especialidad

class Medico(Personas):
    
    def __init__(self, identificacion, nombre, correo, codigo, estado, especialidad):
              super().__init__(identificacion, nombre, correo)
              self.set_codigo(codigo)
              self.set_estado(estado)
              self.set_especialidad(especialidad)
    
    def get_codigo(self):
            return self._codigo
        
    def set_codigo (self, codigo):
        if(codigo.strip() != ""):
            self._codigo = codigo 
        else: 
            raise ValueError("El código del Médico no puede ser vacío")
        
    def get_estado(self):
            return self._estado
        
    def set_estado (self, estado):
        if(estado.strip() != ""):
            self._estado = estado 
        else: 
            raise ValueError("El estado del Médico no puede ser vacío")
        
    def get_especialidad(self):
        return self._especialidad
    
    def set_especialidad (self, especialidad):
        if isinstance(especialidad, Especialidad):
            self._especialidad = especialidad 
        else: 
            raise ValueError("La especialidad del Médico debe ser un objeto válido")
            
    def mostrar_informacion(self):
            return ("Tipo: Medico\n"
                    f"{super().mostrar_informacion()}\n"
                    f"Codigo: {self.get_codigo()}\n"
                    f"Estado: {self.get_estado()}\n"
                    f"Especialidad: {self.get_especialidad()}\n")
    