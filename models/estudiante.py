from models.persona import persona

class estudiante (persona):
    
    def __init__(self, nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio):
        super().__init__(nombre, identificacion, correo)
        self.setCodigoEstudiante(codigoEstudiante)
        self.setProgramaAcademico(programaAcademico)
        self.setSemestre(semestre)
        self.setPromedio(promedio)
    
    def mostrar_informacion(self):
        return super().mostrar_informacion(), self.getProgramaAcademico(), self.getSemestre(), self.getPromedio()
    
    # SETTERs
    def setCodigoEstudiante(self, codigoEstudiante):
        # validaciones
        self._codigoEstudiante = codigoEstudiante
        
    def setProgramaAcademico(self, programaAcademico):
        self._programaAcademico = programaAcademico
    
    def setSemestre(self, semestre):
        self._semestre = semestre
        
    def setPromedio(self, promedio):
        self._promedio = promedio
        
    # GETTERS
    def getCodigoEstudiante(self):
        return self._codigoEstudiante
    
    def getProgramaAcademico(self):
        return self._programaAcademico

    def getSemestre(self):
        return self._semestre

    def getPromedio(self):
        return self._promedio