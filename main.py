
#Importar Clases
from models.persona import persona
from models.programaAcademico import programaAcademico
from models.asignatura import asignatura
from models.estudiante import estudiante
from models.docente import docente
from models.administrativo import administrativo

if __name__ == "__main__":
    # TEST PARA LA FASE 1
    print("---TESTEANDO LA FASE 1: MODELADO INICIAL----------------")
    # 1. Crear una persona
    print("---CREACION DE PERSONA---")
    person = persona("Richard Tabares", "12312313123", "richardtabares@example.com")
    person.mostrar_informacion()
    # 2. Crear un programa
    print("---CREACION DE PROGRAMA---")
    program = programaAcademico("ING-0001", "Ingenieria en Seguridad de la información", "Facultad de Ingenierias", 10)
    program.mostrar_informacion()
    # 3. Crear asignatura
    print("---CREACION DE ASGINATURA---")
    asignature = asignatura("MAT-0001", "Matematicas", 4, "ING-0001")
    asignature.mostrar_informacion()
    
    # TEST PARA LA FASE 2
    print("\n---TESTEANDO LA FASE 2: ENCAPSULAMIENTO Y VALIDACIONES--------------------")
    # 1. Crear programa y asignatura válidos
    print("---CREAR PROGRAMA Y ASIGNATURA VALIDO---")
    program = programaAcademico("ING-0001", "Ingenieria en Seguridad de la información", "Facultad de Ingenierias", 10)
    asignature = asignatura("MAT-0001", "Matematicas", 3, program.get_codigoPrograma())
    print(asignature.mostrar_informacion())
    
    # 2. Intentos de asignar valores INVÁLIDOS (Debe mostrar los mensajes de error)
    #print("--- PROBANDO VALORES INVALIDOS ---")
    
    # Intento 1: Correo vacío en Persona
    #person = persona("10203040", "Carlos Pérez", "carlos@um.edu.co")
    #person.set_correo("")

    # Intento 2: Número de semestres menor o igual a cero en Programa
    #program.set_numeroDeSemestres(0)

    # Intento 3: Número de créditos menor o igual a cero en Asignatura
    #asignature.set_numeroDeCreditos(-2)


    # TEST PARA LA FASE 3 y 4
    print("\n---TESTEANDO LA FASE 3 y 4: HERENCIA Y SOBREESCRITURA-----------------------")
    # 1. crear estudiante
    estu = estudiante(person.get_nombre(), person.get_identificacion(), person.get_correo(), "EST-0001", program.get_codigoPrograma(), "2do semestre", 4.8)
    estu.mostrar_informacion()
    estu.realizar_actividad_principal()
    # 2. crear docente
    doce = docente("Natalia Castellanos", "01010101010", "castellanos@manizales.gov.co", "EMP-0001", "Ingenierias", "Contrato Indefinido", 120)
    doce.mostrar_informacion()
    doce.realizar_actividad_principal()
    # 3. crear administrativo
    admin = administrativo("Jose Luis Torres", "321321321312", "torres@manizales.gov.co", "EMP-0001", "Administrativo", "Rector", "Diurna")
    admin.mostrar_informacion()
    admin.realizar_actividad_principal()