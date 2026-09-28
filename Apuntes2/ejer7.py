#Nicolas Bahena Ostermaier
#Determinar el porcentaje de hombres y de mujeres presentes en el curso
#de Algoritmos, si se conoce el número de hombres y mujeres que tiene.

hombres = int(input("Ingrese el numero de alumnos hombres en el curso: "))
mujeres = int(input("Ingrese el numero de alumnas mujeres en el curso: "))

total = hombres + mujeres

porcentajeH = hombres / total * 100
porcentajeM = mujeres / total * 100

print(f"El porcentaje de alumnos hombres es: {porcentajeH}%")
print(f"El porcentaje de alumnas mujeres es: {porcentajeM}%")
