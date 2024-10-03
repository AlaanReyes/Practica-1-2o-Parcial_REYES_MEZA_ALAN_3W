print("Welcome to Project 1!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO : PRACTICAS TUPLAS   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Lista de materias
materias = [
    "Pensamiento matemático",
    "Leoye",
    "Inglés",
    "Humanidades",
    "Ecosistemas",
    "Programación"
]

# Mostrar materias y mensajes
for materia in materias: #mostrar las materias 
    print(materia) #muestra la materia
    print(f"Estoy cursando {materia}.") #muestra la materia cursada
    calificacion = input(f"Ingrese la calificación para {materia}: ") #calificacion para cada materia
    print()  # Espacio para poner la calificacion
    print(f"En {materia} sacaste {calificacion}.") #muestra que te sacaste en cada materia
    print()  # espacio para la materia con calificacion