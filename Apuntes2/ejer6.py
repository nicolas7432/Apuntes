#Nicolas Bahena Ostermaier
#Un estudiante desea saber cuál será su calificación final en el curso de
#Algoritmos, con los siguientes ı́tems de calificaciones: Primer parcial:
#20 % Segundo parcial: 20 % Práctica: 35 % Parcial final: 25 %.

#Inicializar las variables
porPriPar = 20
porSegPar = 20
porPra = 35
porParFin = 25

#Daton de entrada
print("Primer parcial: ")
priPar = float(input())
print("Segundo parcial: ")
segPar = float(input())
print("Practica: ")
pra = float(input())
print("Parcial final: ")
parFin = float(input())

#Procesos parciales
notDef = (priPar * porPriPar / 100) + (segPar * porSegPar / 100) + (pra * porPra / 100) + (parFin * porParFin / 100)

#Datos de salida parciales
print("Nota definitiva: ", notDef)
