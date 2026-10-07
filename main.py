
from models.persona import persona
from models.asignatura import asignatura

# Crear una instancia de la clase persona
person = persona("Roger", "10171550171", "roger@example.com")

# Mostrar la información de la persona
print(person.mostrar_informacion())

# Crear una instancia de la clase asignatura
asignature = asignatura("MAT001", "Matemáticas", 3, "PRO001")

# Mostrar la información de la asignatura
print(asignature.mostrar_informacion())