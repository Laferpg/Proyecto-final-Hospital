from enum import Enum
from models.excepciones import CamaNoDisponibleError

class EstadoCama(Enum):
    ocupada = "Ocupada"
    disponible = "Disponible"
    mantenimiento = "Mantenimiento"
    
class Cama:
    def __init__(self, codigo, estado):
        self.set_codigo(codigo)
        self.set_estado(estado)
    
    def get_codigo(self):
        return self._codigo 
    
    def set_codigo(self, codigo):
        if codigo.strip() != "":
            self._codigo = codigo
        else:
            raise ValueError("El código de la cama no puede ser vacío")
    
    def get_estado(self):
        return self._estado    
    
    def set_estado(self, estado):
        if isinstance(estado, EstadoCama):
            self._estado = estado
        else:
            raise ValueError(f"Opción inválida, debe ser una de: {[m.value for m in EstadoCama]}")
        
    def esta_disponible(self):
        return self.get_estado() == EstadoCama.disponible

        def ocupar(self):
        # La cama solo se puede ocupar si está disponible
        if not self.esta_disponible():
            raise CamaNoDisponibleError(f"La cama {self.get_codigo()} no está disponible "
                                        f"(estado actual: {self.get_estado().value})")
        self.set_estado(EstadoCama.ocupada)
        
    def liberar(self):
        # Al dar de alta al paciente la cama vuelve a quedar disponible
        self.set_estado(EstadoCama.disponible)
        
    def mostrar_informacion(self):
        return f"Cama {self.get_codigo()} - {self.get_estado().value}"


        


