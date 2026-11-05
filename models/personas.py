class Personas:
    def __init__(self, identificacion, nombre, correo,):
        self.set_identificacion(identificacion)
        self.set_nombre(nombre)
        self.set_correo(correo)
        
    def get_identificacion(self):
        return self._identificacion
    
    def set_identificacion (self, identificacion):
        if(identificacion != ""):
            self._identificacion = identificacion 
        else: 
            raise ValueError("La identificación de la persona no puede ser vacía")
    
    def get_nombre (self):
        return self._nombre
        
    def set_nombre (self, nombre):
        if(nombre != ""):
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
        
    def mostrar_informacion(self):
        return (f"Identificación: {self.get_identificacion()}\n"
                f"Nombre: {self.get_nombre()}\n"
                f"Correo: {self.get_correo()}")

