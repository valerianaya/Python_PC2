def fibonacci_hasta_n(n):
    # Inicializar la serie de Fibonacci con los dos primeros números
    fibonacci = [0, 1]

    # Generar la serie hasta alcanzar o superar n
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci

# Obtener la serie de Fibonacci hasta 50
serie_fibonacci = fibonacci_hasta_n(50)

# Mostrar la serie de Fibonacci
print("Serie de Fibonacci hasta 50:")
print(serie_fibonacci)
