from models.personas import Personas

class Medico(Personas):
    
    def __init__(self, identificacion, nombre, correo, codigo, estado, especialidad):
              super().__init__(identificacion, nombre, correo)
              self.set_codigo(codigo)
              self.set_estado(estado)
              self.set_especialidad(especialidad)
    
    def get_codigo(self):
            return self._codigo
        
    def set_codigo (self, codigo):
        if(codigo != ""):
            self._codigo = codigo 
        else: 
            raise ValueError("EL codigo del Medico no puede ser vacía")
        
    def get_estado(self):
            return self._estado
        
    def set_estado (self, estado):
        if(estado != ""):
            self._estado = estado 
        else: 
            raise ValueError("EL estado del Medico no puede ser vacío")
        
    def get_espacialidad(self):
        return self._especiaidad
    
    def set_especiaidad (self, especialidad):
            if(especialidad != ""):
                self._especiaidad = especialidad 
            else: 
                raise ValueError("La especialidad del Medico no puede ser vacía")
            
    def mostrar_informacion(self):
            return ("Tipo: Medico\n"
                    f"{super().mostrar_informacion()}\n"
                    f"Codigo: {self.get_codigo()}\n"
                    f"Estado: {self.get_estado()}\n"
                    f"Especialidad: {self.get_espacialidad()}\n")
    