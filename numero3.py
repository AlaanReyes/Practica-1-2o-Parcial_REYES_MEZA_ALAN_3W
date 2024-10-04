print("Welcome to Project 1!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Lista para almacenar los números
numeros_triunfadores = []

# Preguntar por los números
while True:
    numero = input("Ingresa un número triunfador (o 'final' para terminar): ")
    if numero == 'final':
        break
    try:
        numeros_triunfadores.append(int(numero))
    except ValueError:
        print("Número inválido.")

# Mostrar los números ordenados
print("Números triunfadores (ordenados):", sorted(numeros_triunfadores))