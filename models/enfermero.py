from models.personas import Personas

class Enfermero(Personas):
    
    def __init__(self, identificacion, nombre, correo, Idempleado, turno):
              super().__init__(identificacion, nombre, correo)
              self.set_Idempleado(Idempleado)
              self.set_turno(turno)
    
    def get_Idempleado(self):
            return self._Idempleado
        
    def set_Idempleado (self, Idempleado):
        if(Idempleado != ""):
            self._Idempleado = Idempleado 
        else: 
            raise ValueError("EL Idempleado del enfermero no puede ser vacío")
        
    def get_turno(self):
            return self._turno
        
    def set_turno (self, turno):
        if(turno != ""):
            self._turno = turno 
        else: 
            raise ValueError("EL turno del enfermero no puede ser vacío")
            
    def mostrar_informacion(self):
            return ("Tipo: Medico\n"
                    f"{super().mostrar_informacion()}\n"
                    f"Idempleado: {self.get_Idempleado()}\n"
                    f"turno: {self.get_turno()}\n")

    