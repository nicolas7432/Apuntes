#Nicolas Bahena Ostermaier
#Apunte4
"""Un almacen de pedidos por correo vende cinco productos, 
los precios son los siguientes:
-producto 1: $2.98
-producto 2: $4.50
-producto 3: $9.98
-producto 4: $4.49
-producto 5: $6.87

Escriba un programa que solicite el numero del producto y la cantidad vendida.
El programa debe determinar el precio de venta de cada producto, calcular y 
mostrar el valor total del producto vendido """


numPro = int(input("Ingrese el numero del producto (1-5): "))
canVen = int(input("Ingrese la cantidad vendida: "))

if numPro == 1:
    preVen = 2.98
elif numPro == 2:
    preVen = 4.50
elif numPro == 3:
    preVen = 9.98
elif numPro == 4:
    preVen = 4.49
elif numPro == 5:
    preVen = 6.87
else:
    print("Error: El numero del producto debe estar entre 1 y 5")
    preVen = 0

valTot = preVen * canVen
print(f"El total de la venta es: ${valTot:.2f}")
