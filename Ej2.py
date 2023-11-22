# Número de filas en el patrón
filas = 5

# Construir el patrón
for i in range(filas * 2):
    if i <= filas:
        print('* ' * i)
    else:
        print('* ' * (filas * 2 - i))
