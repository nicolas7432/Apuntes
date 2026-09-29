#Nicolas Bahena Ostermaier
#Apunte2
#Realizar un algoritmo que lea o capture dos valores. Si el primer valor
#es menor al segundo valor, hacer la suma; de lo contrario, hacer la
#diferencia (resta), si son iguales hacer la multiplicación.

print("Valor No. 1: ")
val1 = int(input())

print("Valor No. 2: ")
val2 = int(input())

#Procesos parciales
if val1 < val2:
    res = val1 + val2
else:
    if val1 > val2:
        res = val1 - val2
    else:
        res = val1 * val2


print("Resultado = ", res)