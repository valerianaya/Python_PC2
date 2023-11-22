# Inicializar la lista para almacenar los números ingresados
numeros = []

# Bucle while para permitir el ingreso de números
while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if desea_ingresar != "SI":
        break

    numero_ingresado = int(input("Ingrese el número: "))
    numeros.append(numero_ingresado)

# Mostrar los números ingresados
print("Números ingresados:", numeros)

# Contar la cantidad de números pares e impares
numeros_pares = sum(1 for num in numeros if num % 2 == 0)
numeros_impares = len(numeros) - numeros_pares

# Mostrar la cantidad de números pares e impares
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
