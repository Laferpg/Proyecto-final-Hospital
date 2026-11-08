from models.personas import Personas
from models.especialidad import Especialidad

class Medico(Personas):
    
    def __init__(self, identificacion, nombre, correo, num_celular, codigo_empleado, estado, especialidad):
              super().__init__(identificacion, nombre, correo, num_celular)
              self.set_codigo_empleado(codigo_empleado)
              self.set_estado(estado)
              self.set_especialidad(especialidad)
    
    def get_codigo_empleado(self):
            return self._codigo_empleado
        
    def set_codigo_empleado(self, codigo_empleado):
        if(codigo_empleado.strip() != ""):
            self._codigo_empleado = codigo_empleado
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
            return ("Tipo: Médico\n"
                    f"{super().mostrar_informacion()}\n"
                    f"Código de empleado: {self.get_codigo_empleado()}\n"
                    f"Estado: {self.get_estado()}\n"
                    f"Especialidad: {self.get_especialidad().get_nombre()}\n")
            
    def obtener_rol(self):
        return "Médico"
    