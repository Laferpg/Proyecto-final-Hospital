from models.personas import Personas

class Paciente(Personas):
    
    def __init__(self, identificacion, nombre, correo, num_celular, historia_cLinica, fecha_nacimiento, genero, tipo_sangre, alergias,antecedentes_personales, antecedentes_familiares, eps):
              super().__init__(identificacion, nombre, correo, num_celular)
              self.set_historia_clinica(historia_cLinica)
              self.set_fecha_nacimiento(fecha_nacimiento)
              self.set_genero(genero)
              self.set_tipo_sangre(tipo_sangre)
              self.set_alergias(alergias)
              self.set_antecedentes_personales(antecedentes_personales)
              self.set_antecedentes_familiares(antecedentes_familiares)
              self.set_eps(eps)
              self._historial_ingresos = []
        
    def get_historia_clinica(self):
        return self._historia_clinica
    
    def set_historia_clinica (self, historia_clinica):
        if(historia_clinica != ""):
            self._historia_clinica = historia_clinica 
        else: 
            raise ValueError("La Historia CLinica del paciente no puede ser vacía")
    
    def get_fecha_nacimiento (self):
        return self._fecha_nacimiento
        
    def set_fecha_nacimiento (self, fecha_nacimiento):
        if(fecha_nacimiento != ""):
            self._fecha_nacimiento = fecha_nacimiento
        else: 
            raise ValueError("La fecha nacimiento del paciente  no puede ser vacía")
        
    def get_genero (self):
        return self._genero
            
    def set_genero (self, genero):
        if genero != "": 
            self._genero = genero
        else: 
            raise ValueError("El género del paciente  no puede estar vacío")
        
    def set_tipo_sangre (self, tipo_sangre):
        if tipo_sangre != "":
            self._tipo_sangre = tipo_sangre
        else:
            raise ValueError("El tipo de sangre del paciente no puede estar vacío")
            
    def get_tipo_sangre (self):
            return self._tipo_sangre

    def set_alergias (self, alergias):
        if alergias != "":
            self._alergias = alergias
        else:
            raise ValueError("Las alergias del paciente no pueden estar vacías")

    def get_alergias (self):
            return self._alergias

    def set_antecedentes_personales (self, antecedentes_personales):
        if antecedentes_personales != "":
            self._antecedentes_personales = antecedentes_personales
        else:
            raise ValueError("Los antecedentes del paciente no pueden estar vacios")

    def get_antecedentes_personales (self):
            return self._antecedentes_personales

    def set_antecedentes_familiares (self, antecedentes_familiares):
        if antecedentes_familiares != "":
            self._antecedentes_familiares = antecedentes_familiares
        else:
            raise ValueError(" Los antecedentes familiares del paciente no pueden estar vacios")

    def get_antecedentes_familiares (self):
            return self._antecedentes_familiares
                
    def set_eps (self, eps):
        if eps != "": 
            self._eps = eps
        else: 
            raise ValueError("La eps del paciente no puede estar vacía")
    
    def get_eps(self):
        return self._eps
    
    def registrar_ingreso(self, ingreso):
        if ingreso not in self._historial_ingresos:
            self._historial_ingresos.append(ingreso)

    def historial_ingresos(self):
        if not self._historial_ingresos:
            return f"{self.get_nombre()} no tiene ingresos registrados"
        texto = f"Historial de ingresos de {self.get_nombre()}:\n"
        for ingreso in self._historial_ingresos:
            texto += (f"- {ingreso.get_codigo()} | {ingreso.get_fecha_ingreso()} | "
                      f"{ingreso.get_motivo_ingreso()} | {ingreso.get_estado().value}\n")
        return texto
        
    def mostrar_informacion(self):
        return ("Tipo: Paciente\n"
                f"{super().mostrar_informacion()}\n"
                f"Historia Clinica: {self.get_historia_clinica()}\n"
                f"Fecha Nacimiento: {self.get_fecha_nacimiento()}\n"
                f"Género: {self.get_genero()}\n"
                f"Tipo de sangre: {self.get_tipo_sangre()}\n"
                f"Alergias: {self.get_alergias()}\n"
                f"Antecedentes personales: {self.get_antecedentes_personales()}\n"
                f"Antecedentes familiares: {self.get_antecedentes_familiares()}\n"
                f"EPS: {self.get_eps()}")

    def obtener_rol(self):
        return "Paciente"
        
        
