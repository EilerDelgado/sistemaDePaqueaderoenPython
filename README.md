# 🚗🅿️ Proyecto Parqueadero en Python

Este es un proyecto sencillo que hice en Python para simular un sistema de parqueadero.  
La idea es tener un menú donde se pueden hacer estas cosas:

- Ingresar vehículos (Carros o Motos) ✅  
- Registrar la salida de un vehículo ✅  
- Ver los espacios disponibles en el parqueadero ✅  
- Calcular cuánto debe pagar el vehículo al salir según el tiempo que estuvo ✅  

---

## ⚙️ Tecnologías usadas
- Python 3  
- Librería `datetime` (para manejar horas y calcular el tiempo)  

---

## 📂 Archivos del Proyecto

- [parqueadero.py](parqueadero.py) → Archivo principal con el menú y las funciones.  

---

## 📌 Funcionalidades

### 1. Ingresar Vehículo
- **Descripción**: Registra un carro o moto con su placa y la hora exacta de entrada.  
- **Características**:  
  - Valida que no se repita una placa ya registrada.  
  - Valida si el parqueadero tiene espacio disponible para carros o motos.  

---

### 2. Salida de Vehículo
- **Descripción**: Registra la hora de salida de un vehículo y calcula el pago.  
- **Características**:  
  - Muestra los datos del vehículo (placa, tipo, hora entrada/salida).  
  - Calcula el tiempo total que estuvo y el valor a pagar según tarifas.  

---

### 3. Mostrar Espacios Disponibles
- **Descripción**: Indica cuántos espacios libres quedan para carros y motos.  
- **Características**:  
  - Considera solo los vehículos que aún no han salido.  

---

### 4. Cálculo del Pago
- **Descripción**: Calcula el valor a pagar en base al tiempo de estadía.  
- **Tarifas usadas en este proyecto**:  
  - Carros: $2500 por hora.  
  - Motos: $1700 por hora.  
- **Características**:  
  - Cobra fracciones de hora proporcionalmente.  
  - Maneja casos donde la salida ocurre después de la medianoche.  

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar o descargar este repositorio.  
2. Abrir el archivo `parqueadero.py` en un editor de código (ejemplo: PyCharm, VSCode).  
3. Ejecutar el programa.  
4. Seguir el menú en la consola:  

