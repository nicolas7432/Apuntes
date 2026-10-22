"""
1. Generar 9 calificaciones aleatorias de un alumno (rango 5-10),
2. almacenarlas en una lista
3. obtener el promedio y
4. mostrar la grafica de frecuencias del promedio y cada calificacion-

Ejemplo
cal1 9 *********
cal2 7 *******
cal3 10 **********
.
.
.
cal10 5 *****

Promedio: 8.4 ********
"""
#Nicolas Bahena Ostermaier

import random

cal = []
suma = 0

for i in range(9):
    valor = random.randint(5, 10)
    cal.append(valor)

for i in range(9):
    print("Cal", i + 1, " ", cal[i], " ", "*" * cal[i],sep="")
    suma += cal[i]

promedio = suma / 9

print("Promedio: ", round(promedio, 1), '*' * int(round(promedio)))
