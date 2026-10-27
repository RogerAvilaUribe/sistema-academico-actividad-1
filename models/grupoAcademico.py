from models.horario import horario

class grupoAcademico:
    def __init__(self, codigoGrupo, asignatura, docente, capacidad, estudiantesMatriculados, horario):
        self.set_codigoGrupo(codigoGrupo)
        self.set_asignatura(asignatura)
        self.set_docente(docente)
        self.set_capacidad(capacidad)
        self.estudiantesMatriculados=[]
        self.set_horario(horario)
          
    # Getters and Setters
    def set_codigoGrupo(self, codigoGrupo):
        self._codigoGrupo = codigoGrupo
        
    def get_codigoGrupo(self):
        return self._codigoGrupo

    def set_asignatura(self, asignatura):
        self._asignatura = asignatura

    def get_asignatura(self):
        return self._asignatura

    def set_docente(self, docente):
        self._docente = docente

    def get_docente(self):
        return self._docente

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def get_capacidad(self):
        return self._capacidad

    # def set_estudiantesMatriculados(self, estudiantesMatriculados):
    #     self._estudiantesMatriculados = estudiantesMatriculados

    # def get_estudiantesMatriculados(self):
    #     return self._estudiantesMatriculados 

    def set_horario(self, horario):
        self._horario = horario

    def get_horario(self):
        return self._horario     

    def mostrar_informacion_grupo(self):
        print(f"Codigo del grupo: {self.get_codigoGrupo()}")
        print(f"Asignatura: {self.get_asignatura()}")
        print(f"Docente: {self.get_docente()}")
        print(f"Capacidad: {self.get_capacidad()}")
        print(f"Estudiantes matriculados: {self.get_estudiantesMatriculados()}")
        print(f"Horario: {self.get_horario()}")   

    def matricular_estudiante(self, estudiante):
        if len(self.estudiantesMatriculados) < self.get_capacidad():
            # Pendiente validar si el estudiante ya existe
            self.estudiantesMatriculados.append(estudiante)
            print(f"Estudiante matriculado en el grupo {self.get_codigoGrupo()}")
        else:
            print("No se puede matricular más estudiantes. Grupo lleno.")
        print(f"Horario: {self.get_horario()}")  

    def retirar_estudiante(self, codigoEstudiante):
        if codigoEstudiante in self.get_estudiantesMatriculados():
            self.get_estudiantesMatriculados().remove(codigoEstudiante)
            print(f"Estudiante retirado del grupo {self.get_codigoGrupo()}")
        else:
            print("El estudiante no está matriculado en este grupo.")

    def mostrar_estudiantes(self):
        print(f"Estudiantes matriculados en el grupo {self.get_codigoGrupo()}:")
        for estudiante in self.estudiantesMatriculados:
            print(f" - {estudiante}")