#Nicolas Bahena Ostermaier
#Apunte 2 - Area y perimetro de un circulo
import math

radio = float(input("Ingrese el radio del circulo: "))

area = 3.14151987552 * radio * radio
print("Area (sin formato): ", area)

area = math.pi * radio ** 2
print(f"Area (con formato): {area:.4f}")

area = math.pi * pow(radio,2)
print(f"Area (con formato): {area:.2f}")

perimetro = 2*radio*math.pi
print(f"Perimetro (con formato): {perimetro:.3f}")