# Calcular la distancia entre dos puntos del plano cartesiano
# usando tuplas
import math
def calcularDistancia(punto1, punto2):
    # Desempaquetar la tupla en 2 variables
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia

print("Punto 1: ")
x1 = (float(input("Ingrese el valor de x: ")))
y1 = (float(input("Ingrese el valor de y: ")))
punto1 = (x1, y1)
print("Punto 2: ")
x2 = (float(input("Ingrese el valor de x: ")))
y2 = (float(input("Ingrese el valor de y: ")))
punto2 = (x2, y2)

print(f"\nLa distancia es: {calcularDistancia(punto1, punto2)}")