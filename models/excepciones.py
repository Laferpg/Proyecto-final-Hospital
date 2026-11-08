# Excepciones personalizadas del sistema de hospitalización.
# Todas heredan de HsopitalError, así en el programa principal se pueden 
# capturar una por una o todas juntas.

class HospitalError(Exception):
    """Clase base de los errores propios del sistema de hospitalización"""
    pass


class CamaNoDisponibleError(HospitalError):
    """Se lanza cuando se intenta asignar una cama ocupada o en mantenimiento"""
    pass


class CapacidadHabitacionError(HospitalError):
    """Se lanza cuando se intenta agregar más camas de las que caben en una habitación"""
    pass


class
    """Se lanza cuando se intenta registrar una persona con una identificación que ya existe"""
    pass
