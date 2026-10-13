from models.persona import persona 

class administrativo (persona):

    def __init__(self, nombre, identificacion, correo, numeroDeEmpleado, dependencia, cargo, jornada):
        super().__init__(nombre, identificacion, correo)
        self.setNumeroDeEmpleado(numeroDeEmpleado)
        self.setDependencia(dependencia)
        self.setCargo(cargo)
        self.setJornada(jornada)

    def mostrar_informacion(self):
        return super().mostrar_informacion(), self.getNumeroDeEmpleado(), self.getDependencia(), self.getCargo(), self.getJornada()

    # SETTERS
    def setNumeroDeEmpleado(self, numerodeEmpleado):
        self._numeroDeEmpleado = numerodeEmpleado

    def setDependencia(self, dependencia):
        self._dependencia = dependencia

    def setCargo(self, cargo):
        self._cargo = cargo

    def setJornada(self, jornada):
        self._jornada = jornada

    # GETTERS
    def getNumeroDeEmpleado(self):
        return self._numeroDeEmpleado

    def getDependencia(self):
        return self._dependencia

    def getCargo(self):
        return self._cargo 

    def getJornada(self):
        return self._jornada

    
