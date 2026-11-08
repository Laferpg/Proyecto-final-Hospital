
class Especialidad:
    
    def __init__(self, codigo, nombre):
        self.set_codigo(codigo)
        self.set_nombre(nombre)
        
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        if codigo.strip() != "":
            self._codigo = codigo
        else:
            raise ValueError("El código de la especialidad no puede ser vacío")
        
    def get_nombre(self):
        return self._nombre 
    
    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self._nombre = nombre
        else: 
            raise ValueError("El nombre de la especialidad no puede ser vacío")
        
    def mostrar_informacion(self):
        return (f"Especialidad \n"
                f"Código: {self.get_codigo()}\n"
                f"Nombre: {self.get_nombre()}")