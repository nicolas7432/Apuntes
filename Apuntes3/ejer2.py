#Nicolas Bahena Ostermaier
#Apunte3
#Realizar un algoritmo para determinar la bonificación que recibe un
#empleado de la compañía ABC, la cuál les otorgan una sola vez al año
#una bonificación de acuerdo con su salario básico y los años de
#antigüedad en la organización según la siguiente información:

#Menos de 5 años 5% del salario basico
#5 años o más y menos de 10 años, 10% del salario básico
#10 años o más y menos de 15 años, 15% del salario básico
#15 años o más y menos de 20 años, 20% del salario básico
#20 años o más y menos de 25 años, 25% del salario básico
#25 años o más y menos de 30 años, 35% del salario básico
#30 años o más, 50% del salario básico

salBas = float(input("Salario basico: "))
tieSer = float(input("Tiempo de servicio en años: "))

#Procesos parciales
if tieSer < 5:
    porBon = 5
else:
    if tieSer < 10:
        porBon = 10
    else:
        if tieSer < 15:
            porBon = 15
        else:
            if tieSer < 20:
                porBon = 20
            else:
                if tieSer < 25:
                    porBon = 25
                else:
                    if tieSer < 30:
                        porBon = 35
                    else:
                        porBon = 50


valBon = salBas * porBon / 100

#Datos de salida parciales
print("Porcentaje de bonificacion: ", porBon)
print("Valor de la bonificacion: ", valBon)