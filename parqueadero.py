from datetime import datetime, timedelta

# Variables de capacidad del parqueadero
capacidadMotos = 20
capacidadCarros = 10
capacidadTotal = capacidadCarros + capacidadMotos

# Una lista que dentro contiene un diccionario y dupla
vehiculos = [
    # Carros
    {"datos": ("AXT456", "Carro"), "horaEntrada": "2025-08-16 08:30", "horaSalida": None},
    {"datos": ("ABC123", "Carro"), "horaEntrada": "2025-08-16 09:15", "horaSalida": None},
    {"datos": ("GHI789", "Carro"), "horaEntrada": "2025-08-16 10:45", "horaSalida": None},
    {"datos": ("JKL012", "Carro"), "horaEntrada": "2025-08-15 11:20", "horaSalida": None},
    {"datos": ("MNO345", "Carro"), "horaEntrada": "2025-08-14 12:10", "horaSalida": None},
    {"datos": ("PQR678", "Carro"), "horaEntrada": "2025-08-13 13:30", "horaSalida": None},
    # Motos
    {"datos": ("XYZ12L", "Moto"), "horaEntrada": "2025-08-16 08:45", "horaSalida": None},
    {"datos": ("EFG78P", "Moto"), "horaEntrada": "2025-08-16 09:00", "horaSalida": None},
    {"datos": ("STU90Y", "Moto"), "horaEntrada": "2025-08-15 09:30", "horaSalida": None},
    {"datos": ("VWX23R", "Moto"), "horaEntrada": "2025-08-15 10:15", "horaSalida": None},
    {"datos": ("YZA56T", "Moto"), "horaEntrada": "2025-08-14 10:50", "horaSalida": None},
    {"datos": ("BCD89Ñ", "Moto"), "horaEntrada": "2025-08-14 11:05", "horaSalida": None},
    {"datos": ("DEF12Q", "Moto"), "horaEntrada": "2025-08-14 11:40", "horaSalida": None},
    {"datos": ("HIJ45T", "Moto"), "horaEntrada": "2025-08-13 12:25", "horaSalida": None},
    {"datos": ("KLM78F", "Moto"), "horaEntrada": "2025-08-13 12:55", "horaSalida": None},
    {"datos": ("NOP01H", "Moto"), "horaEntrada": "2025-08-13 13:15", "horaSalida": None},
    {"datos": ("QRS34V", "Moto"), "horaEntrada": "2025-08-12 13:45", "horaSalida": None},
    {"datos": ("TUV67J", "Moto"), "horaEntrada": "2025-08-12 14:20", "horaSalida": None},
    {"datos": ("WXY90K", "Moto"), "horaEntrada": "2025-08-12 14:50", "horaSalida": None},
    {"datos": ("ZAB23M", "Moto"), "horaEntrada": "2025-08-11 15:10", "horaSalida": None},
    {"datos": ("CDE56D", "Moto"), "horaEntrada": "2025-08-11 15:35", "horaSalida": None}
]


# Funcion para contar la cantidad que hay de cada tipo de vehiculo
def contarVehiculos(vehiculos):
    cantidadMotos = 0
    cantidadCarros = 0
    # Se recorre la lista de vehiculos
    for vehiculo in vehiculos:
        # Solo contar vehículos que AUN están en el parqueadero
        if vehiculo["horaSalida"] is None:
            tipoVehiculo = vehiculo["datos"][1]  # se extrae el dato de la dupla
            if tipoVehiculo == "Moto":
                cantidadMotos += 1
            elif tipoVehiculo == "Carro":
                cantidadCarros += 1
    return cantidadCarros, cantidadMotos


# Función para validar el tipo de vehículo
def validarTipoVehiculo():
    while True:
        tipoVehiculo = input("Ingrese el tipo de vehículo (Carro/Moto): ").strip().capitalize()
        if tipoVehiculo in ["Carro", "Moto"]:
            return tipoVehiculo
        else:
            print("Error ingrese el tipo de Vehiculo")


'''Funcion para registrar el vehiculo y tambien hacer la validacion sin el parqueadero esta lleno
o ya esta registrado el vehiculo.'''

def registrarIngreso(vehiculos, capacidadMotos, capacidadCarros, capacidadTotal):
    cantidadCarros, cantidadMotos = contarVehiculos(vehiculos)

    # Usamos la función validarTipoVehiculo para obtener el tipo de vehículo
    tipoVehiculo = validarTipoVehiculo()

    # Validamos si hay cupo para el tipo de vehiculo
    if tipoVehiculo == "Moto" and cantidadMotos >= capacidadMotos:
        print("No hay Espacio Disponible para Moto")
        return
    elif tipoVehiculo == "Carro" and cantidadCarros >= capacidadCarros:
        print("No hay espacio disponible para carro")
        return

    placa = input("Ingrese la placa del vehiculo: ").strip().upper()

    # Validar si ya esta registrado
    for vehiculo in vehiculos:
        if vehiculo["datos"][0] == placa and vehiculo["horaSalida"] is None:
            print("El Vehiculo ya esta registrado")
            return

    # Registramos el ingreso
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    vehiculos.append({
        "datos": (placa, tipoVehiculo),
        "horaEntrada": hora_actual,
        "horaSalida": None
    })
    print(f'{tipoVehiculo} con placa {placa} fue registrado exitosamente')


def registrarSalida(vehiculos):
    placa = input("Ingrese la placa del vehículo que va a salir: ").strip().upper()

    for vehiculo in vehiculos:
        if vehiculo["datos"][0] == placa and vehiculo["horaSalida"] is None:
            # Registrar hora de salida
            hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
            vehiculo["horaSalida"] = hora_actual

            # Calcular el valor a pagar
            pago, horas = calcularPago(vehiculo)

            # Mostrar datos del vehiculo
            print("\n--- DATOS DEL VEHÍCULO ---")
            print(f"Placa del Vehiculo: {vehiculo['datos'][0]}")
            print(f"Tipo de Vehiculo: {vehiculo['datos'][1]}")
            print(f"Hora de entrada: {vehiculo['horaEntrada']}")
            print(f"Hora de salida: {vehiculo['horaSalida']}")
            print(f"Total de Horas: {horas}")
            print(f"Total a pagar: ${pago:,.0f}")
            print("Salida registrada exitosamente")
            return

    print("Vehículo no encontrado o ya registró salida")


# Funcion para mostrar espacios disponibles
def mostrarEspaciosDisponibles(vehiculos, capacidadMotos, capacidadCarros):
    cantidadCarros, cantidadMotos = contarVehiculos(vehiculos)

    espaciosCarros = capacidadCarros - cantidadCarros
    espaciosMotos = capacidadMotos - cantidadMotos
    espaciosTotal = espaciosCarros + espaciosMotos

    print("\n--- ESPACIOS DISPONIBLES ---")
    print(f"Espacios para carros: {espaciosCarros}")
    print(f"Espacios para motos: {espaciosMotos}")
    print(f"Total espacios libres: {espaciosTotal}")


# Funcion para generar informe semanal
def generarInformeSemanal(vehiculos):
    from datetime import datetime, timedelta

    # Obtener fecha actual y calcular rango de la semana
    fecha_actual = datetime.now()
    inicio_semana = fecha_actual - timedelta(days=7)

    print(f"\n=== INFORME SEMANAL ===")
    print(f"Periodo: {inicio_semana.strftime('%Y-%m-%d')} al {fecha_actual.strftime('%Y-%m-%d')}")
    print("=" * 50)

    # Contadores para el informe
    carros_ingresados = 0
    motos_ingresadas = 0
    total_ingresos_carros = 0
    total_ingresos_motos = 0
    vehiculos_sin_salida = 0

    # Recorrer todos los vehículos
    for vehiculo in vehiculos:
        # Convertir fecha de entrada para comparar
        fecha_entrada = datetime.strptime(vehiculo["horaEntrada"], "%Y-%m-%d %H:%M")

        # Verificar si el vehículo ingresó en la última semana
        if fecha_entrada >= inicio_semana:
            tipo_vehiculo = vehiculo["datos"][1]

            if tipo_vehiculo == "Carro":
                carros_ingresados += 1
            else:  # Moto
                motos_ingresadas += 1

            # Si el vehículo ya salió, calcular ingresos
            if vehiculo["horaSalida"] is not None:
                pago, horas = calcularPago(vehiculo)

                if tipo_vehiculo == "Carro":
                    total_ingresos_carros += pago
                else:  # Moto
                    total_ingresos_motos += pago
            else:
                vehiculos_sin_salida += 1

    # Mostrar resultados
    print(f"VEHICULOS INGRESADOS:")
    print(f"  Carros: {carros_ingresados}")
    print(f"  Motos: {motos_ingresadas}")
    print(f"  Total vehiculos: {carros_ingresados + motos_ingresadas}")
    print()

    print(f"INGRESOS GENERADOS:")
    print(f"  Carros: ${total_ingresos_carros:,.0f}")
    print(f"  Motos: ${total_ingresos_motos:,.0f}")
    print(f"  Total ingresos: ${total_ingresos_carros + total_ingresos_motos:,.0f}")
    print()

    if vehiculos_sin_salida > 0:
        print(f"NOTA: {vehiculos_sin_salida} vehiculo(s) aun no han registrado salida")

    print("=" * 50)


# Funcion para mostrar el menu
def mostrarMenu():
    print("\n=== SISTEMA DE PARQUEADERO ===")
    print("1. Ingresar vehículo")
    print("2. Salida de vehículo")
    print("3. Mostrar espacios disponibles")
    print("4. Generar informe semanal")
    print("5. Salir")
    print("================================")


# Funcion para calcular el valor a pagar
def calcularPago(vehiculo):
    # Tarifas por hora
    tarifaCarro = 2500
    tarifaMoto = 1700

    # Convertimos las horas de entrada y salida a objetos datetime
    formato = "%Y-%m-%d %H:%M"
    horaEntrada = datetime.strptime(vehiculo["horaEntrada"], formato)
    horaSalida = datetime.strptime(vehiculo["horaSalida"], formato)

    # Calculamos la diferencia
    tiempoEstadia = horaSalida - horaEntrada

    # Convertimos a horas
    horas = tiempoEstadia.total_seconds() / 3600

    # Calculamos el costo segun el tipo
    if vehiculo["datos"][1] == "Carro":
        costo = horas * tarifaCarro
    else:  # Moto
        costo = horas * tarifaMoto

    # Redondeamos a número entero (sin decimales)
    return int(round(costo, 0)), round(horas, 1)


# Programa principal con menu
def main():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrarIngreso(vehiculos, capacidadMotos, capacidadCarros, capacidadTotal)
        elif opcion == "2":
            registrarSalida(vehiculos)
        elif opcion == "3":
            mostrarEspaciosDisponibles(vehiculos, capacidadMotos, capacidadCarros)
        elif opcion == "4":
            generarInformeSemanal(vehiculos)
        elif opcion == "5":
            print("Gracias por usar el sistema de parqueadero")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 5")


# Ejecutar el programa
if __name__ == "__main__":
    main()