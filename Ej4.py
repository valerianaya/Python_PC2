# Inicializar la lista para almacenar los datos de los alumnos
lista_alumnos = []

# Solicitar al usuario ingresar la cantidad de alumnos (n)
n = int(input("Ingrese la cantidad de alumnos: "))

# Bucle para ingresar datos de cada alumno
for _ in range(n):
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    calificaciones = [float(input(f"Ingrese la calificación {i + 1} del alumno {nombre_alumno}: ")) for i in range(3)]

    # Crear un diccionario para el alumno actual
    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}

    # Agregar el diccionario a la lista de alumnos
    lista_alumnos.append(alumno)

# Mostrar el listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
