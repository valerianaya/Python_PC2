def obtener_fecha_en_formato_ymd(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Intentar parsear la fecha en formato mes-día-año
    try:
        mes, dia, anio = fecha.split("/")
    except ValueError:
        # Si no se puede parsear, intentar parsear en formato "Mes día, año"
        partes = fecha.split(" ")
        mes = partes[0].capitalize()
        dia = partes[1].strip(",")
        anio = partes[2]

    # Obtener el índice del mes en la lista de meses
    indice_mes = meses.index(mes) + 1

    # Formatear la fecha en AAAA-MM-DD
    fecha_ymd = f"{anio:04d}-{indice_mes:02d}-{int(dia):02d}"

    return fecha_ymd

# Solicitar al usuario una fecha
fecha_ingresada = input("Ingrese una fecha (en formato mes-día-año o Mes día, año): ")

# Obtener la fecha en formato AAAA-MM-DD
fecha_ymd = obtener_fecha_en_formato_ymd(fecha_ingresada)

# Mostrar el resultado
print(f"Fecha original: {fecha_ingresada}")
print(f"Fecha en formato AAAA-MM-DD: {fecha_ymd}")
