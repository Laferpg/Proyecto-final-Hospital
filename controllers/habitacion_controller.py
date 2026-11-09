from models.habitacion import Habitacion, EstadoHabitacion


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

    def buscar_habitacion(self, numero):
        for habitacion in self._habitaciones:
            if habitacion.get_num_habitacion() == numero:
                return habitacion
        return None