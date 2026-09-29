#Nicolas Bahena Ostermaier
#Apunte5
#Un vendedor recibe un sueldo básico más una comisión del 10 % si su
#venta es menor que 100,000 pesos o del 15 % si su venta es mayor o
#igual a 100,000 pesos. El vendedor desea saber cuánto dinero
#obtendrá por concepto de comisión y su sueldo.

sueBas = float(input("Sueldo basico: "))
valVen = float(input("Valor venta: "))

#Procesos parciales
if valVen < 100000:
    porCom = 10
else:
    porCom = 15

valCom = (valVen * porCom) / 100
sueNet = sueBas + valCom

#Datos de salida parciales
print("Porcentaje de comision: ", porCom)
print("Valor comision: ", valCom)
print("Sueldo neto: ", sueNet)