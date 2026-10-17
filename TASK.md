# Checklist del Taller: Sistema de Gestión Académica (POO en Python)

## README.md
- [] Estructura de archivos
- [] Instrucciones para ejecutar el proyecto
- [] Explicacion breve de como se aplicaron la herencia, la sobre escritura y el polimosrfismo

## Fase 1: Modelado inicial del sistema (Clases base y constructores)
- [x] Crear la clase `persona`
    - Atributos: 
        - identificación
        - nombre
        - correo
    - Métodos `mostrar_informacion()`
- [x] Crear la clase `programaAcademico`
    - Atributos:
        - código
        - nombre
        - facultad
        - número de semestres
    - Métodos `mostrar_informacion()`
- [x] Crear la clase `asignatura`
    - Atributos:
        - código
        - nombre
        - número de créditos
        - programa académico
    - Métodos `mostrar_informacion()`
- [x] Configurar constructores (`__init__`) en todas las clases.

## Fase 2: Encapsulamiento y validación de datos
- [x] Aplicar encapsulamiento (atributos privados con `_` o `__`).
- [x] Implementar métodos getters y setters con validaciones:
  - [x] Correo electrónico no vacío.
  - [x] Número de semestres > 0.
  - [x] Número de créditos > 0.
- [x] Mensajes de advertencia cuando el valor ingresado sea inválido.

## Fase 3: Herencia (Especialización de personas)
- [x] Crear clase `estudiante` heredando de `persona`
    - Atributos extra:
        - código estudiantil
        - programa académico
        - semestre
        - promedio acumulado
- [x] Crear clase `docente` heredando de `persona`
    - Atributos extra:
        - número de empleado
        - facultad
        - tipo de contratación
        - horas semanales
- [x] Crear clase `administrativo` heredando de `persona`
    - Atributos extra:
        - número de empleado
        - dependencia
        - cargo
        - jornada
- [x] Utilizar `super()` en los constructores para reutilizar los atributos comunes.

## Fase 4: Sobrescritura de métodos (Polimorfismo estático / comportamientos particulares)
- [x] Sobrescribir `mostrar_informacion()` en `estudiante`, `docente` y `administrativo` para incluir sus datos específicos.
- [x] Implementar y sobrescribir el método `realizar_actividad_principal()` en cada clase hija con su comportamiento particular.

## Fase 5: Procesamiento conjunto y Polimorfismo dinámico
- [x] Crear una única colección (lista) en el programa principal con al menos 2 estudiantes, 2 docentes y 2 administrativos.
- [x] Recorrer la colección usando un **único ciclo** sin condicionales de tipo (`isinstance` o `type`), invocando `mostrar_informacion()` y `realizar_actividad_principal()`.

## Fase 6: Pruebas, Repositorio y Documentación (GitHub)
- [x] Escribir el script de pruebas en el archivo principal (`main.py`) cubriendo todos los requerimientos
    - [x] La creación de programas académicos y asignaturas.
    - [x] La creación de al menos seis personas.
    - [x] La consulta de la información de los objetos.
    - [x] La modificación válida de datos encapsulados.
    - [x] El intento de asignar al menos tres valores inválidos.
    - [x] La presentación particular de cada tipo de persona.
    - [x] El recorrido polimórfico de la colección de personas.