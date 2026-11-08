from models.zona import Zona

class ZonaController:
    
    def __init__(self):
        self.zonas = []
        
    def añadir_zona (self, nombre, piso):
        zona = Zona (nombre, piso)
        self.zonas.append(zona)
        return zona
        
    def get_zonas(self):
        return self.zonas.copy()
