from models.habitacion import Habitacion, EstadoHabitacion
from models.excepciones import CapacidadHabitacionError


class HabitacionController:

    def __init__(self):
        self._habitaciones = []

    def añadir_habitacion(self, num_habitacion, capacidad_camas, estado: EstadoHabitacion):
        habitacion = Habitacion(
            num_habitacion,
            capacidad_camas,
            estado
        )

        self._habitaciones.append(habitacion)
        return habitacion

    def get_habitaciones(self):
        return self._habitaciones.copy()

    
    
