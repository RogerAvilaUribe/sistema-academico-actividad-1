
#Importar Clases
from models.programaAcademico import programaAcademico
from models.estudiante import estudiante
from models.asignatura import asignatura

if __name__ == "__main__":
    
    # Crear una instancia de la clase estudiante
    estu = estudiante("Richard Tabares", "12312313123", "richardtabares@example.com", "EST-0001", "Ingenieria en ciberseguridad", "2do semestre", 4.5 )
    print("Nombre del estudiante: ", estu.mostrar_informacion()[0][0])
    print("Identificación del estudiante: ", estu.mostrar_informacion()[0][1])
    print("Correo del estudiante: ", estu.mostrar_informacion()[0][2])
    print("Código del estudiante: ", estu.mostrar_informacion()[0])
    print("Programa académico: ", estu.mostrar_informacion()[1])
    print("Semestre: ", estu.mostrar_informacion()[2])

    # # Crear una instancia de la clase Programa Academico
    # programa1 = programaAcademico("ISI001", "Ingeniería en Seguridad de la Información", "Facultad de Ingenierías", 9)

    # # Crear una instancia de la clase asignatura
    # asignature = asignatura("MAT001", "Matemáticas", 3, "PRO001")

    # # Mostrar la información del 
    # print(programa1.mostrar_informacion())