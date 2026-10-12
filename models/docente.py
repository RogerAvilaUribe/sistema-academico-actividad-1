from models.persona import persona

class docente (persona):

    def __init__(self, nombre, identificacion, correo, numeroDeEmpleado, facultad, tipoDeContratacion, numeroDeHorasSemanales):
        super().__init__(nombre, identificacion, correo)
        self.setNumeroDeEmpleado(numeroDeEmpleado)
        self.setFacultad(facultad)
        self.setTipoDeContratacion(tipoDeContratacion)
        self.setNumeroDeHorasSemanales(numeroDeHorasSemanales)

    def mostrar_informacion(self):
        return super().mostrar_informacion(), self.getNumeroDeEmpleado(), self.getFacultad(), self.getTipoDeContratacion(), self.getNumeroDeHorasSemanales()

    # SETTERS
    def setNumeroDeEmpleado(self, numeroDeEmpleado):
        self._numeroDeEmpleado = numeroDeEmpleado

    def setFacultad(self, facultad):
        self._facultad = facultad 

    def setTipoDeContratacion(self, tipoDeContratacion):
        self._tipoDeContratacion = tipoDeContratacion

    def setNumeroDeHorasSemanales(self, numeroDeHorasSemanales):
        self._numeroDeHorasSemanales = numeroDeHorasSemanales

    # GETTERS
    def getNumeroDeEmpleado(self):
        return self._numeroDeEmpleado

    def getFacultad(self):
        return self._facultad
    
    def getTipoDeContratacion(self):
        return self._tipoDeContratacion

    def getNumeroDeHorasSemanales(self):
        return self._numeroDeHorasSemanales
    