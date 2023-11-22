def contar_digitos(numero, digito):
    # Convertir el número a una cadena para poder utilizar el método count
    numero_str = str(numero)

    # Contar la cantidad de veces que aparece el dígito en el número
    cantidad = numero_str.count(str(digito))

    return cantidad

# Ejemplo de uso
numero_ingresado = 15789000
digito_ingresado = 0

cantidad_veces = contar_digitos(numero_ingresado, digito_ingresado)

print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_ingresado}")
print(f"Cantidad de veces {digito_ingresado} en el número: {cantidad_veces}")
