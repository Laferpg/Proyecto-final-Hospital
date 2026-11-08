from models.paciente import Paciente
from models.cama import Cama, EstadoCama
from enum import Enum

class EstadoIngreso(Enum):
    activo = "Activo"
    de_alta = "Dado de alta"

class Ingreso:
    
    def __init__(self, paciente, codigo, fecha_ingreso, motivo_ingreso, escala_dolor, estado_conciencia, requiere_aislamiento,
                 riesgo_caida, diagnostico, estado, cama):
        self.set_paciente(paciente)
        self.set_codigo(codigo)
        self.set_fecha_ingreso(fecha_ingreso)
        self.set_motivo_ingreso(motivo_ingreso)
        self.set_escala_dolor(escala_dolor)
        self.set_estado_conciencia(estado_conciencia)
        self.set_requiere_aislamiento(requiere_aislamiento)
        self.set_riesgo_caida(riesgo_caida)
        self.set_diagnostico(diagnostico)
        self.set_estado(estado)
        self.set_cama(cama)
        self._paciente.registrar_ingreso(self)
    
    def get_paciente(self):
        return self._paciente
    
    def set_paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self._paciente = paciente 
        else: 
            raise ValueError("El paciente debe un objeto existente")
    
    def get_codigo(self):
        return self._codigo
        
    def set_codigo(self, codigo):
        if(codigo.strip() != ""):
            self._codigo = codigo
        else: 
            raise ValueError("El código no puede ser vacío")
    
    def get_fecha_ingreso(self):
        return self._fecha_ingreso
    
    def set_fecha_ingreso(self,fecha_ingreso):
        if fecha_ingreso != "":
            self._fecha_ingreso = fecha_ingreso
        else:
            raise ValueError("La fecha de ingreso no puede ser vacía")
        
    def get_motivo_ingreso(self):
        return self._motivo_ingreso
    
    def set_motivo_ingreso(self, motivo_ingreso):
        if motivo_ingreso.strip() != "":
            self._motivo_ingreso = motivo_ingreso
        else: 
            raise ValueError("El motivo del ingreso no puede ser vacío")
        
    def get_escala_dolor(self):
        return self._escala_dolor
    
    def set_escala_dolor(self, escala_dolor):
        if 0 <= escala_dolor <= 10:
            self._escala_dolor = escala_dolor
        else:
            raise ValueError("La escala de dolor debe estar entre 0 y 10")
            
    def get_estado_conciencia(self):
        return self._estado_conciencia
    
    def set_estado_conciencia(self, estado_conciencia):
        if estado_conciencia.strip() != "":
            self._estado_conciencia = estado_conciencia
        else:
            raise ValueError("El estado de conciencia no puede estar vacío")
            
    def get_requiere_aislamiento(self):
        return self._requiere_aislamiento
    
    def set_requiere_aislamiento(self, requiere_aislamiento):
        if isinstance(requiere_aislamiento, bool):
            self._requiere_aislamiento = requiere_aislamiento
        else:
            raise ValueError("El requisito de aislamiento debe ser un valor booleano")
            
    def get_riesgo_caida(self):
        return self._riesgo_caida
    
    def set_riesgo_caida(self, riesgo_caida):
        if isinstance(riesgo_caida, bool):
            self._riesgo_caida = riesgo_caida
        else:
            raise ValueError("El riesgo de caída debe ser un valor booleano")
            
    def get_diagnostico(self):
        return self._diagnostico
    
    def set_diagnostico(self, diagnostico):
        if diagnostico.strip() != "":
            self._diagnostico = diagnostico
        else:
            raise ValueError("El diagnóstico no puede estar vacío")
            
    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        if isinstance(estado, EstadoIngreso):
            self._estado = estado
        else:
            raise ValueError(f"El estado debe ser activo o dado de alta")
        
    def get_cama(self):
        return self._cama 
    
    def set_cama(self, cama:Cama):
        if cama.esta_disponible():
            self._cama = cama
            cama.set_estado(EstadoCama.ocupada)
            print(f"Cama {cama.get_codigo()} asignada con éxito al ingreso {self._codigo}")
        else:
            print(f"La cama {cama.get_codigo()} ya está ocupada")
        
        
    