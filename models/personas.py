from abc import ABC, abstractmethod

class Personas(ABC):
    def __init__(self, identificacion, nombre, correo, num_celular):
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_num_celular(num_celular)
        
    def get_identificacion(self):
        return self._identificacion
    
    def set_identificacion (self, identificacion):
        if(identificacion.strip() != ""):
            self._identificacion = identificacion 
        else: 
            raise ValueError("La identificación de la persona no puede ser vacía")
    
    def get_nombre (self):
        return self._nombre
        
    def set_nombre (self, nombre):
        if(nombre.strip() != ""):
            self._nombre = nombre
        else: 
            raise ValueError("El nombre de la persona no puede ser vacío")
        
    def get_correo (self):
        return self._correo
            
    def set_correo (self, correo):
        if correo and correo.strip() != "": #para remover espacios en blanco antes de validar el contenido
            self._correo = correo
        else: 
            raise ValueError("El correo de la persona no puede ser vacío")
        
    def get_num_celular(self):
        return self._num_celular 
    
    def set_num_celular(self, num_celular):
        if num_celular.strip() != "":
            self._num_celular = num_celular 
        else: 
            raise ValueError ("El número de celular no puede ser vacío")
        
    @abstractmethod
    def mostrar_informacion(self):
        return (f"Identificación: {self.get_identificacion()}\n"
                f"Nombre: {self.get_nombre()}\n"
                f"Correo: {self.get_correo()}\n"
                f"Número de celular: {self.get_num_celular()}")
        
    @abstractmethod
    def obtener_rol(self):
        """cada clase hija sobrescribe su rol"""

