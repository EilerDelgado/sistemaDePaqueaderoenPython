from datetime import datetime

# Variables de capacidad del parqueadero
capacidadMotos = 20
capacidadCarros = 10
capacidadTotal = capacidadCarros + capacidadMotos
cantidadMotos = 0
cantidadCarros = 0

# Una lista que dentro contiene un diccionario y dupla
vehiculos = [
    {"datos": ("AXT456", "Carro"), "horaEntrada": "10:30", "horaSalida": None},
    {"datos": ("XYZ123", "Moto"), "horaEntrada": "10:45", "horaSalida": None},
    {"datos": ("ABCD12", "Carro"), "horaEntrada": "11:00", "horaSalida": None},
    {"datos": ("EFG789", "Moto"), "horaEntrada": "11:15", "horaSalida": None}
]


# Funcion para contar la cantidad que hay de cada tipo de vehiculo
def contarVehiculos(vehiculos):
    cantidadMotos = 0
    cantidadCarros = 0
    # Se recorre la lista de vehiculos
    for vehiculo in vehiculos:
        tipoVehiculo = vehiculo["datos"][1]  # se extrae el dato de la dupla
        if tipoVehiculo == "Moto":
            cantidadMotos += 1
        elif tipoVehiculo == "Carro":
            cantidadCarros += 1
    return cantidadCarros, cantidadMotos


# Funcion para registrar el vehiculo y tambien hacer la validacion sin el parqueadero esta lleno
# o ya esta registrado el vehiculo.
def registrarIngreso(vehiculos, capacidadMotos, capacidadCarros, capacidadTotal):
    cantidadCarros, cantidadMotos = contarVehiculos(vehiculos)

    if len(vehiculos) >= capacidadTotal:
        print("PARQUEADERO LLENO")
        return

    tipoVehiculo = input("Ingrese el tipo de vehículo (Carro/Moto): ").strip().capitalize()
    placa = input("Ingrese la placa del vehiculo: ").strip().upper()

    # Validamos si hay cupo para el tipo de vehiculo
    if tipoVehiculo == "Moto" and cantidadMotos >= capacidadMotos:
        print("No hay Espacio Disponible para Moto")
        return
    elif tipoVehiculo == "Carro" and cantidadCarros >= capacidadCarros:
        print("No hay espacio disponible para carro")
        return

    # Validar si ya esta registrado
    for vehiculo in vehiculos:
        if vehiculo["datos"][0] == placa and vehiculo["horaSalida"] is None:
            print("El Vehiculo ya esta registrado")
            return

    # Registramos el ingreso
    hora_actual = datetime.now().strftime("%H:%M")
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
            hora_actual = datetime.now().strftime("%H:%M")
            vehiculo["horaSalida"] = hora_actual

            # Calcular el valor a pagar
            pago = calcularPago(vehiculo)

            # Mostrar datos del vehiculo
            print("\n--- DATOS DEL VEHÍCULO ---")
            print(f"Placa: {vehiculo['datos'][0]}")
            print(f"Tipo: {vehiculo['datos'][1]}")
            print(f"Hora de entrada: {vehiculo['horaEntrada']}")
            print(f"Hora de salida: {vehiculo['horaSalida']}")
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


# Funcion para mostrar el menu
def mostrarMenu():
    print("\n=== SISTEMA DE PARQUEADERO ===")
    print("1. Ingresar vehículo")
    print("2. Salida de vehículo")
    print("3. Mostrar espacios disponibles")
    print("4. Salir")
    print("================================")


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
            print("Gracias por usar el sistema de parqueadero")
            break
        else:
            print("Opción no válida. Por favor seleccione una opción del 1 al 4")


# Funcion para calcular el valor a pagar
def calcularPago(vehiculo):
    # Tarifas por hora
    tarifaCarro = 2500
    tarifaMoto = 1700

    # Convertimos las horas de entrada y salida a objetos datetime
    formato = "%H:%M"
    horaEntrada = datetime.strptime(vehiculo["horaEntrada"], formato)
    horaSalida = datetime.strptime(vehiculo["horaSalida"], formato)

    # Calculamos la diferencia en minutos
    tiempoEstadia = horaSalida - horaEntrada
    minutos = tiempoEstadia.total_seconds() / 60

    # Convertimos a horas (con decimales)
    horas = minutos / 60

    # Calculamos el costo segun el tipo
    if vehiculo["datos"][1] == "Carro":
        costo = horas * tarifaCarro
    else:  # Moto
        costo = horas * tarifaMoto

    return round(costo, 0)



# Ejecutar el programa
if __name__ == "__main__":
    main()

