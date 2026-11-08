from models.ingreso import Ingreso, Paciente, Cama

class IngresoController:
    
    def __init__(self):
        self._ingresos = []
        
    def añadir_ingreso(self, paciente:Paciente, codigo, fecha_ingreso, motivo_ingreso, escala_dolor, estado_conciencia,
                       requiere_aislamiento, riesgo_caida, diagnostico, cama:Cama):
        ingreso = Ingreso(paciente, codigo, fecha_ingreso, motivo_ingreso, escala_dolor, estado_conciencia,
                          requiere_aislamiento, riesgo_caida, diagnostico, cama)
        self._ingresos.append(ingreso)
        return ingreso
        
    def get_ingresos(self):
        return self._ingresos.copy()
