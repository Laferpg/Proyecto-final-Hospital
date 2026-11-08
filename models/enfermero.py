from models.personas import Personas
from enum import Enum

class Turno(Enum):
    diurno = "Diurno"
    nocturno = "Nocturno"

class Enfermero(Personas):
    
    def __init__(self, identificacion, nombre, correo, num_celular, Idempleado, turno):
              super().__init__(identificacion, nombre, correo, num_celular)
              self.set_Idempleado(Idempleado)
              self.set_turno(turno)
    
    def get_Idempleado(self):
            return self._Idempleado
        
    def set_Idempleado (self, Idempleado):
        if(Idempleado.strip() != ""):
            self._Idempleado = Idempleado 
        else: 
            raise ValueError("EL código de empleado del enfermero no puede ser vacío")
        
    def get_turno(self):
            return self._turno
        
    def set_turno (self, turno):
        if isinstance(turno, Turno):
            self._turno = turno 
        else: 
            raise ValueError("Opción inválida, debe ser diurno o nocturno")
            
    def mostrar_informacion(self):
            return ("Tipo: Enfermero\n"
                    f"{super().mostrar_informacion()}\n"
                    f"Id de empleado: {self.get_Idempleado()}\n"
                    f"Turno: {self.get_turno().value}\n")
    
    def obtener_rol(self):
        return "Enfermero(a)"

    