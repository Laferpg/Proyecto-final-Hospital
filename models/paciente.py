from models.personas import Personas

class Paciente(Personas):
    
    def __init__(self, identificacion, nombre, correo, historia_cLinica, fecha_naciemiento, genero, eps):
              super().__init__(identificacion, nombre, correo)
              self.set_historia_clinica(historia_cLinica)
              self.set_fecha_naciemiento(fecha_naciemiento)
              self.set_genero(genero)
              self.set_eps(eps)
        
    def get_historia_clinica(self):
        return self._historia_clinica
    
    def set_historia_clinica (self, historia_clinica):
        if(historia_clinica != ""):
            self._historia_clinica = historia_clinica 
        else: 
            raise ValueError("La Historia CLinica del paciente no puede ser vacía")
    
    def get_fecha_naciemiento (self):
        return self._fecha_naciemiento
        
    def set_fecha_naciemiento (self, fecha_naciemiento):
        if(fecha_naciemiento != ""):
            self._fecha_naciemiento = fecha_naciemiento
        else: 
            raise ValueError("La Fecha Naciemiento del paciente  no puede ser vacía")
        
    def get_genero (self):
        return self._genero
            
    def set_genero (self, genero):
        if genero != "": 
            self._genero = genero
        else: 
            raise ValueError("El genero del paciente  no puede estar vacío")
        
    def get_genero (self):
            return self._genero
                
    def set_eps (self, eps):
        if eps != "": 
            self._eps = eps
        else: 
            raise ValueError("La eps del paciente  no puede estar vacía")
        
    def mostrar_informacion(self):
        return ("Tipo: Paciente\n"
                f"{super().mostrar_informacion()}\n"
                f"Historia Clinica: {self.get_historia_clinica()}\n"
                f"Fecha Naciemiento: {self.get_fecha_naciemiento()}\n"
                f"genero: {self.get_genero()}\n"
                f"eps: {self.get_eps()}")
        
        
