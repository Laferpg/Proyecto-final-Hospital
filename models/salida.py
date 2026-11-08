from enum import Enum

class TipoSalida(Enum):
    alta = "Alta"
    remision = "Remisión"
    fallecimiento = "Fallecimiento"

class Salida:
    
    def __init__(self, fecha_salida, tipo_salida, diagnostico_final, indicaciones):
        self.set_fecha_salida(fecha_salida)
        self.set_tipo_salida(tipo_salida)
        self.set_diagnostico_final(diagnostico_final)
        self.set_indicaciones(indicaciones)
        
    def get_fecha_salida(self):
        return self._fecha_salida
    
    def set_fecha_salida(self, fecha_salida):
        if fecha_salida.strip() != "":
            self._fecha_salida = fecha_salida
        else:
            raise ValueError("La fecha de salida no puede ser vacía")
        
    def get_tipo_salida(self):
        return self._tipo_salida
    
    def set_tipo_salida(self, tipo_salida):
        if isinstance(tipo_salida, TipoSalida):
            self._tipo_salida = tipo_salida
        else:
            raise ValueError(f"Opción inválida, debe ser una de: {[m.value for m in TipoSalida]}")
        
    def get_diagnostico_final(self):
        return self._diagnostico_final
    
    def set_diagnostico_final(self, diagnostico_final):
        if diagnostico_final.strip() != "":
            self._diagnostico_final = diagnostico_final
        else:
            raise ValueError("El diagnóstico final no puede ser vacío")
        
    def get_indicaciones(self):
        return self._indicaciones
    
    def set_indicaciones(self, indicaciones):
        if indicaciones.strip() != "":
            self._indicaciones = indicaciones
        else:
            raise ValueError("Las indicaciones no pueden ser vacías")
        
    def mostrar_informacion(self):
        return (f"Salida\n"
                f"Fecha de salida: {self.get_fecha_salida()}\n"
                f"Tipo de salida: {self.get_tipo_salida().value}\n"
                f"Diagnóstico final: {self.get_diagnostico_final()}\n"
                f"Indicaciones: {self.get_indicaciones()}")
