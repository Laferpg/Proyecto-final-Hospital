from models.cama import Cama, EstadoCama


class CamaController:
    def __init__(self):
        self._camas = []
        
        
    def agregar_cama(self, codigo, estado: EstadoCama):
        cama = Cama(codigo, estado)
        self._camas.append(cama)
        return cama
    
    def get_camas(self):
        return self._camas.copy()

    
    def camas_disponibles(self):
        return [
            cama for cama in self._camas
            if cama.esta_disponible()
            ]