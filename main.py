from controllers.user_controller import userController
from controllers.asignatura_controller import asignaturaController
from controllers.programa_controller import programaController

# metodo para mostrar todo los usuario y aplica POLIMORFISMO
def mostrar_usuarios(user_controller):
    usuarios = user_controller.get_personas()
    
    if not usuarios:
        print("Sin personas para mostrar")
        return
    
    for usuario in usuarios:
        usuario.mostrar_informacion()
        print(f"Su actividad principal es: ", end="")
        usuario.realizar_actividad_principal()
        print("-"*100)

# metodo para mostrar todo las asignaturas
def mostrar_asignaturas(asignatura_controller):
    asignaturas = asignatura_controller.get_asignaturas()
    
    if not asignaturas:
        print("Sin asignaturas para mostrar")
        return
    
    for asignatura in asignaturas:
        asignatura.mostrar_informacion()
        print("-"*100)

# metodo para mostrar todos los programas
def mostrar_programas(programa_controller):
    programas = programa_controller.get_programas()
    
    if not programas:
        print("Sin programas para mostrar")
        return
    
    for programa in programas:
        programa.mostrar_informacion()
        print("-"*100)

def main():
    
    # Inicializamos el controlador de usuarios
    user_controller = userController()

    # Inicializamos el controlador de asignaturas
    asignatura_controller = asignaturaController()

    # Inicializamos el controlador de programas
    programa_controller = programaController()
    
    # Precargamos algunos datos
    user_controller.agregar_estudiante("Lucía Pérez", "1010222", "lucia-perez@gmail.com", "EST-01", "Ingeniería de Sistemas", 3, 4.3)
    user_controller.agregar_estudiante("Mateo Gómez", "1010333", "mateo.gomez@um.edu.co", "EST-02", "Ingeniería de Sistemas", 1, 4.0)
    user_controller.agregar_docente("Dr. Alberto Rueda", "987654", "alberto.rueda@um.edu.co", "EMP-D-01", "Facultad de Ingeniería", "Planta", 40)
    user_controller.agregar_docente("Dra. Sofia Castro", "987655", "sofia.castro@um.edu.co", "EMP-D-02", "Facultad de Ciencias", "Cátedra", 16)
    user_controller.agregar_administrativo("Carla Mendoza", "554433", "carla.mendoza@um.edu.co", "EMP-A-01", "Registro Académico", "Coordinadora", "Completa")
    user_controller.agregar_administrativo("Julián Ruiz", "554434", "julian.ruiz@um.edu.co", "EMP-A-02", "Biblioteca", "Asistente", "Media")
    asignatura_controller.agregar_asignatura("PRO001", "Programación 1", 4, "ING001")
    programa_controller.agregar_programa("ING001", "Ingenieria en Seguridad de la Información", "Ingenierias", 9)
    
    while True:
        
        print("\n")
        print("==================================================")
        print("    SISTEMA DE GESTIÓN ACADÉMICA - MENÚ PRINCIPAL")
        print("==================================================")
        print("===>   Se auto preacarga los siguientes datos   <===")
        print("+ 2 Usuarios Estudiantes")
        print("+ 2 Usuarios Docentes")
        print("+ 2 Usuarios Administrativos")
        print("+ 1 Progarma Académico")
        print("+ 1 Asignatura")
        print("===> *** Validaciones básicas *** <===")
        print("*El correo del usuario no puede ir vacios")
        print("*El numero de semestres para el programar academico debe ser mayor a 0")
        print("*El numero de creditos para asignatura debe ser mayor a 0")
        print("="*50)
        print("\n")
        print("OPCIONES")
        print("1. Registrar Programa Académico")
        print("2. Registrar Asignatura")
        print("3. Registrar Estudiante")
        print("4. Registrar Docente")
        print("5. Registrar Personal Administrativo")
        print("6. Listar Programas")
        print("7. Listar Asignaturas")
        print("8. Generar Reporte Polimórfico de personas")
        print("9. Salir")
        
        # capturamos la opcion a ejecutar
        option = input("Ingrese una opción del 1 al 9: ").strip()
        print("\n")
        
        # se optado por utiliza un try except para capturar los errores en cada una de los casos
        match option:
            
            case '1':
                print("\n--- Registrar Programa Academico ---")
                try:
                    # capturamos los datos del programa
                    codigoPrograma = input("Ingrese el codigo del programa: ")
                    nombre = input("Ingrese el nombre del programa: ")
                    facultad = input("Ingresa facultad a la que pertenece: ")
                    numeroDeSemestres = int(input("Ingrese el numero de semestres: "))
                                    
                    # utilizamos el controlador para agregar un nuevo programa
                    programa_controller.agregar_programa(
                        codigoPrograma, nombre, facultad, numeroDeSemestres)
                                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            case '2':
                print("\n--- Registrar Asignatura ---")
                try:
                    # capturamos los datos de la asignatura
                    codigoAsignatura = input("Ingrese el codigo de la asignatura: ")
                    nombre = input("Ingrese el nombre de la asignatura: ")
                    numeroDeCreditos = int(input("Ingresa numero de los creditos: "))
                    codigoPrograma = input("Ingrese el codigo del programa: ")
                                    
                    # utilizamos el controlador para agregar una nueva asignatura
                    asignatura_controller.agregar_asignatura(
                        codigoAsignatura, nombre, numeroDeCreditos, codigoPrograma)
                                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '3':
                print("\n--- Registrar Estudiante ---")
                try:
                    # capturamos los datos del usuario estudiante
                    nombre = input("Ingrese nombre del estudiante: ")
                    identificacion = input("Ingrese identificacion del estudiantes: ")
                    correo = input("Ingresa correo electronico: ")
                    codigoEstudiante = input("Ingrese el codigo del estudiante: ")
                    programaAcademico = input("Ingrese programa academico: ")
                    semestre = input("Ingrese semestre que actualmente cursa: ")
                    promedio = input("Ingrese promedio: ")
                    
                    # utilizamos el controlador para agregar un nuevo estudiante
                    user_controller.agregar_estudiante(nombre, identificacion, correo, codigoEstudiante, programaAcademico, semestre, promedio)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '4':
                print("\n--- Registrar Docente ---")
                try:
                     # capturamos los datos del usuario docente
                    nombre = input("Ingrese nombre del docente: ")
                    identificacion = input("Ingrese identificacion del docente: ")
                    correo = input("Ingresa correo electronico: ")
                    numeroEmpleado = input("Ingrese numero de empleado: ")
                    facultad = input("Ingrese facultad: ")
                    tipoContrato = input("Ingrese tipo de contratacion: ")
                    horaSemanales = input("Ingrese numero de horas semanales: ")
                    
                    # # utilizamos el controlador para agregar un nuevo docente
                    user_controller.agregar_docente(nombre, identificacion, correo, numeroEmpleado, facultad, tipoContrato, horaSemanales)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
            
            case '5':
                print("\n--- Registrar Personal Administrativo ---")
                try:
                     # capturamos los datos del usuario administrativo
                    nombre = input("Ingrese nombre del administrativo: ")
                    identificacion = input("Ingrese identificacion del administrativo: ")
                    correo = input("Ingresa correo electronico: ")
                    numeroEmpleado = input("Ingrese numero de empleado: ")
                    dependencia = input("Ingrese dependencia: ")
                    cargo = input("Ingrese cargo: ")
                    jornada = input("Ingrese jornada: ")
                    
                    # utilizamos el controlador para agregar un nuevo administrativo
                    user_controller.agregar_administrativo(nombre, identificacion, correo, numeroEmpleado, dependencia, cargo, jornada)
                    
                except ValueError as e:
                    print(f"Error de validacion: {e}")
                    
            case '6':
                print("\n--- Listado de programas ---")
                mostrar_programas(programa_controller)
            
            case '7':
                print("\n--- Listado de asignaturas ---")
                mostrar_asignaturas(asignatura_controller)
            
            case '8':
                # mostraremos todos los usuario registrados sin importar el tipo
                print("=====================================================")
                print("   REPORTE DE USUARIOS REGISTRADOS (POLIMORFISMO)  ")
                print("=====================================================")
                mostrar_usuarios(user_controller)
            
            case '9':
                print("Salir del sistema")
                break
                
            case _:
                print("Opcion invalida, seleccione un numero del 1 al 9")

if __name__ == "__main__":
    main()