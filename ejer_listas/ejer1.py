"""
Ejercicio 1
Declare una lista de numeros con los siguientes
valores: 10,21,4,45,66,93,11
Imprima los elementos de la lista utilizando un ciclo
Determine cuantos son pares y cuantos son impares

"""
#Nicolas Bahena Ostermaier

numeros = [10,21,4,45,66,93,11]
pares = 0
impares = 0

for i in numeros:
    if i%2 == 0:
        pares += 1
    else:
        impares += 1
    print(i, end=" ")


print("\n\nCantidad de numeros pares: ", pares)
print("\nCantidad de numeros impares: ", impares)
