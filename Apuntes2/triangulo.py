#Nicolas Bahena Ostermaier
#Calcular el area y perimetro de un triangulo
#asumir que es un triangulo equilatero

altura = float(input("Ingrese la altura del triangulo: "))
lado = float(input("Ingrese el lado del triangulo: "))

area = (lado * altura) / 2
perimetro = lado * 3

print("")
print("El area del triangulo es: ", area)
print("El perimetro del triangulo es: ", perimetro)

