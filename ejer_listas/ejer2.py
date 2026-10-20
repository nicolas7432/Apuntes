"""
Ejercicio 2
Pide a un usuario agregar 10 valores a una lista
(los valores pueden se numericos, reales o cadenas)
Imprime los valores de la lista
Luego invierte los elementos de la lista y muestralos
Ejemplo: [45,21,85,78,99,1,0,78,33,10]
Salida: [10,33,78,0,1,99,78,85,21,45]
"""
#Nicolas Bahena Ostermaier

valores = []
print("Ingrese 10 valores a la lista(numericos, reales o cadena): ")

for i in range(10):
    print("Valor ",i+1,": ",end="")
    valor = input()
    valores.append(valor)

print("\nValores ingresados: ")
for i in valores:
    print(i,end=", ")

valores.reverse()
print("\n\nValores invertidos: ")
for i in valores:
    print(i,end=", ")


    