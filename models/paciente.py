from models.personas import Personas

class Paciente(Personas):
    
    def __init__(self, identificacion, nombre, correo, historia_cLinica, fecha_naciemiento, genero, tipo_sangre, alergias,antecedentes_personales, antecedentes_familiares, eps):
              super().__init__(identificacion, nombre, correo)
              self.set_historia_clinica(historia_cLinica)
              self.set_fecha_naciemiento(fecha_naciemiento)
              self.set_genero(genero)
              self.set_tipo_sangre(tipo_sangre)
              self.alergias(alergias)
              self.antecedentes_personales(antecedentes_personales)
              self.antecedentes_familiares(antecedentes_familiares)
              self.set_eps(eps)
        
    def get_historia_clinica(self):
        return self._historia_clinica
    
    def set_historia_clinica (self, historia_clinica):
        if(historia_clinica != ""):
            self._historia_clinica = historia_clinica 
        else: 
            raise ValueError("La Historia CLinica del paciente no puede ser vacía")
    
    def get_fecha_naciemiento (self):
        return self._fecha_naciemiento
        
    def set_fecha_naciemiento (self, fecha_naciemiento):
        if(fecha_naciemiento != ""):
            self._fecha_naciemiento = fecha_naciemiento
        else: 
            raise ValueError("La Fecha Naciemiento del paciente  no puede ser vacía")
        
    def get_genero (self):
        return self._genero
            
    def set_genero (self, genero):
        if genero != "": 
            self._genero = genero
        else: 
            raise ValueError("El genero del paciente  no puede estar vacío")
        
    def get_genero (self):
            return self._genero
        
    def set_tipo_sangre (self, tipo_sangre):
        if tipo_sangre != "":
            self._tipo_sangre = tipo_sangre
        else:
            raise ValueError("El tipo de sangre del paciente no puede estar vacio")
            
    def get_tipo_sangre (self):
            return self.tipo_sangre

    def set_alergias (self, alergias):
        if alergias != "":
            self._alergias = alergias
        else:
            raise ValueError(" Las alergias del paciente no puede estar vacias")

    def get_alergias (self):
            return self.alergias

    def set_antecedentes_personales (self, antecedentes_personales):
        if antecedentes_personales != "":
            self.antecedentes_personales = antecedentes_personales
        else:
            raise ValueError(" Los antecedentes del paciente no pueden estar vacios")

    def get_antecedentes_personales (self):
            return self.antecedentes_personales

    def set_antecedentes_familiares (self, antecedentes_familiares):
        if antecedentes_familiares != "":
            self.antecedentes_familiares = antecedentes_familiares
        else:
            raise ValueError(" Los antecedentes familiares del paciente no pueden estar vacios")

    def get_antecedentes_familiares (self):
            return self.antecedentes_familiares
                
    def set_eps (self, eps):
        if eps != "": 
            self._eps = eps
        else: 
            raise ValueError("La eps del paciente  no puede estar vacía")
        
    def mostrar_informacion(self):
        return ("Tipo: Paciente\n"
                f"{super().mostrar_informacion()}\n"
                f"Historia Clinica: {self.get_historia_clinica()}\n"
                f"Fecha Naciemiento: {self.get_fecha_naciemiento()}\n"
                f"Genero: {self.get_genero()}\n"
                f"Tipo de sangre: {self.tipo_sangre()}\n"
                f"Alergias: {self.alergias()}\n"
                f"Antecedentes personales: {self.antecedentes_personales()}\n"
                f"Antecedentes familiares: {self.antecedentes_familiares()}\n"
                f"eps: {self.get_eps()}")

    def obtener_rol(self):
        return "Paciente"
        
        
