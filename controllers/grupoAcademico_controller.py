from models.grupoAcademico import grupoAcademico

class grupoAcademicoController():

    def __init__(self):
        self.gruposAcademicos = []

    def agregar_grupo_academico(self, codigoGrupo, asignatura, docente, capacidad, horario):
        grupo = grupoAcademico(codigoGrupo, asignatura, docente, capacidad, horario)
        self.gruposAcademicos.append(grupo)

    def get_grupos_academicos(self):
        return self.gruposAcademicos.copy()