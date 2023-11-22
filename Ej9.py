def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    resultado = ''.join(caracter for caracter in cadena if caracter not in vocales)
    return resultado

# Solicitar al usuario una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto: ")

# Obtener el resultado con las vocales omitidas
resultado_final = omitir_vocales(cadena_ingresada)

# Mostrar el resultado
print(f"Texto original: {cadena_ingresada}")
print(f"Texto con vocales omitidas: {resultado_final}")
