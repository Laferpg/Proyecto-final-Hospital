from enum import Enum
from models.cama import Cama, EstadoCama

class EstadoHabitacion(Enum):
    disponible = "Disponible"
    ocupada = "Ocupada"
    mantenimiento = "Mantenimiento"
    
class Habitacion:
    def __init__(self, num_habitacion, capacidad_camas, estado):
        self.set_num_habitacion(num_habitacion)
        self.set_capacidad_camas(capacidad_camas)
        self.set_estado (estado)
        self._camas: list[Cama] = []
        
    def get_num_habitacion(self):
        return self._num_habitacion
        
    def set_num_habitacion(self, num_habitacion):
        if num_habitacion > 0:
            self._num_habitacion = num_habitacion
        else:
            raise ValueError("El número de habitación debe ser un entero positivo")
            
    def get_capacidad_camas(self):
        return self._capacidad_camas 
    
    def set_capacidad_camas(self, capacidad_camas):
        if capacidad_camas > 0:
            self._capacidad_camas = capacidad_camas
        else:
            raise ValueError("La capacidad de camas debe ser un entero positivo")
    
    def get_estado(self):
        return self._estado        
    
    def set_estado(self, estado):
            if isinstance(estado, EstadoHabitacion):
                self._estado = estado
            else:
                raise ValueError(f"Opción inválida, debe ser una de: {[m.value for m in EstadoHabitacion]}")
            
    def agregar_cama(self, codigo, estado:EstadoCama):
        if len(self._camas) >= self.get_capacidad_camas():
            raise ValueError(f"La habitación {self.get_num_habitacion()} ya alcanzó su "
                                f"capacidad de {self.get_capacidad_camas()} cama(s)")
        cama = Cama(codigo, estado)
        self._camas.append(cama)
        return cama
    
    def get_camas(self):
        return self._camas.copy()
    
    def camas_libres(self):
        libres=[]
        for u in self._camas:
            if u.esta_disponible():
                libres.append(u)
        return libres
    
    def mostrar_camas_libres(self):
        libres=self.camas_libres()
        if not libres:
            return "No hay camas disponibles\n"
        texto = f"Hay {len(libres)} cama(s) disponible(s): \n"
        for u in libres:
            texto += f"- Cama {u.get_codigo()} \n"
        return texto

    def mostrar_info(self):
        return (f"Habitación: \n"
                f"Número de habitación: {self.get_num_habitacion()}\n"
                f"Capacidad de camas: {self.get_capacidad_camas()}\n"
                f"Estado de la habitación: {self.get_estado().value}\n"
                f"Camas en la habitación: {len(self._camas)}\n"
                f"{self.mostrar_camas_libres()}")
 
            
            
            
            
            