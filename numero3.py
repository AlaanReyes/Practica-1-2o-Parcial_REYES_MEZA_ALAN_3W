print("Welcome to Project 1!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO : PRACTICAS TUPLAS   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def obtener_numeros_triunfadores():
    numeros = []
    
    while True:
        entrada = input("Ingresa un número triunfador (o 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            break
        
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
   
            print("ingesaste un numero no valido ")
    print(" ")
    return numeros

def main():
    numeros_triunfadores = obtener_numeros_triunfadores()
    
    # Ordenar la lista
    numeros_triunfadores.sort()
    
    # Convertir la lista en tuplas
    tuplas_numeros = [(num,) for num in numeros_triunfadores]
    
    # Mostrar los resultados
    print("Números triunfadores (de menor a mayor):")
    for tupla in tuplas_numeros:
        print(tupla)

if __name__ == "__main__":
    main()