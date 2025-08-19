# 🚗🅿️ Proyecto Parqueadero en Python

Este es un proyecto sencillo desarrollado en Python para simular un sistema de parqueadero.  
La idea principal es contar con un menú interactivo que permita realizar diferentes operaciones relacionadas con la administración de un parqueadero.

---

## ⚙️ Tecnologías usadas
- Python 3  
- Librería `datetime` y `timedelta` (para manejar fechas y calcular tiempos)  

---

## 📂 Archivos del Proyecto
- `parqueadero.py` → Archivo principal con el menú y las funciones.  

---

## 📌 Funcionalidades

### 1. Ingresar vehículo
**Descripción:**  
Permite registrar un carro o moto con su placa y la hora exacta de entrada.  

**Características:**  
- Valida que no se repita una placa ya registrada.  
- Verifica si el parqueadero tiene espacio disponible para carros o motos.  

---

### 2. Salida de Vehículo
**Descripción:**  
Permite registrar la hora de salida de un vehículo y calcular el pago.  

**Características:**  
- Muestra los datos del vehículo (placa, tipo, hora entrada/salida).  
- Calcula el tiempo total que estuvo y el valor a pagar según tarifas.  

---

### 3. Mostrar Espacios Disponibles
**Descripción:**  
Indica cuántos espacios libres quedan para carros y motos.  

**Características:**  
- Solo considera los vehículos que aún no han salido.  

---

### 4. Cálculo del Pago
**Descripción:**  
Calcula el valor a pagar en base al tiempo de estadía.  

**Tarifas usadas en este proyecto:**  
- Carros: $2500 por hora.  
- Motos: $1700 por hora.  

**Características:**  
- Cobra fracciones de hora proporcionalmente.  
- Maneja casos donde la salida ocurre después de la medianoche.  

---

### 5. Generar Informe Semanal 🆕
**Descripción:**  
Genera un informe de la última semana con datos de uso del parqueadero.  

**Incluye:**  
- Número de carros y motos ingresados.  
- Total de ingresos generados por cada tipo de vehículo.  
- Total de ingresos combinados.  
- Cantidad de vehículos que siguen dentro del parqueadero sin registrar salida.  

---

## ▶️ Cómo ejecutar el proyecto
1. Clonar este repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/proyectoParqueadero.git
   ```

2. Abrir el archivo `parqueadero.py` en un editor de código (ejemplo: PyCharm, VSCode).  

3. Ejecutar el programa:  
   ```bash
   python parqueadero.py
   ```

---

## 📝 Notas
- Este proyecto está pensado con fines educativos para practicar **Programación en Python**.  
- A futuro se podrían implementar mejoras como: guardar datos en una base de datos, interfaz gráfica y diferentes planes de tarifas.  
