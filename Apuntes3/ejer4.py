#Nicolas Bahena Ostermaier
#Apunte 6
#Un almacén les hace descuento a sus clientes de acuerdo con la
#siguiente información:
#Compras mayores o iguales a 100000 y menores de 200000 tienen descuento del 10 %.
#Compras mayores o iguales a 200000 y menores de 300000 tienen descuento del 15 %.
#Compras mayores o iguales a 300000 y menores de 400000 tienen descuento del 20 %.
#Compras mayores o iguales a 400000 y menores de 500000 tienen descuento del 25 %.
#Compras mayores o iguales a 500000 tienen descuento del 30 %.
#Realizar un algoritmo para determinar el valor que un cliente debe pagar por su compra.

valCom = float(input("Valor de la compra: "))

#Procesos parciales
if valCom < 100000:
    porDes = 0
elif valCom < 200000:
    porDes = 10
elif valCom < 300000:
    porDes = 15
elif valCom < 400000:
    porDes = 20
elif valCom < 500000:
    porDes = 25
else:
    porDes = 30


valDes = (valCom * porDes) / 100
valPag = valCom - valDes

#Datos de salida
print("Porcentaje de descuento: ", porDes)
print("Valor descontado: ", valDes)
print("Valor a pagar: ", valPag)