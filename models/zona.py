from models.habitacion import Habitacion, EstadoHabitacion

class Zona:
    def __init__(self, nombre, piso):
        self.set_nombre(nombre)
        self.set_piso(piso)
        self._habitaciones: list[Habitacion] = []
 
    def cantidad_habitaciones(self):
        return len(self._habitaciones)
 
    def get_nombre(self):
        return self._nombre
        
    def get_piso(self):
        return self._piso 
    
    def set_nombre(self, nombre):
        if nombre.strip() != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede ser vacío")
    
    def set_piso(self, piso):
        if piso > 0:
            self._piso = piso 
        else: 
            raise ValueError("El piso debe ser un número entero positivo")
 
    def agregar_habitacion(self, num_habitacion, capacidad_camas, estado:EstadoHabitacion):
        habitacion = Habitacion(num_habitacion, capacidad_camas, estado)
        self._habitaciones.append(habitacion)
        return habitacion

    def get_habitaciones(self):
        return self._habitaciones.copy()

    def camas_disponibles(self):
        libres = []
        for h in self._habitaciones:
            libres.extend(h.camas_libres())
        return libres
 
    def mostrar_camas_disponibles(self):
        texto = f"Camas libres en la zona {self.get_nombre()}:\n"
        for h in self._habitaciones:
            texto += f"- Habitación {h.get_num_habitacion()}: {h.mostrar_camas_libres()}\n"
        return texto
