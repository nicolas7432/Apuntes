#Nicolas Bahena Ostermaier
#Apunte 2

primos = [2,3,5,7,11,13]
dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
lista = [primos,dias]
peliculas = [["Spider-man Brand new day",2026],["El retorno del rey",2023]]

#Imprimir el valor 11 de la lista primos
print(primos[4])

#Imprimir lunes de la lista dias
print(dias[0])

#Imprimir el 3er elemento de la lista en la posicion 1 de lista[]
print(lista[1][2])

#Imprimir el titulo de la primero pelicula
print(peliculas[0][0])

#Accder a todos los elementos del la lista primos con un ciclo
print()
for i in range(6):
    print(primos[i],end=" ")

#Accder a todos los elementos del la lista primos con un ciclo
print()
for i in dias:
    print(i,end=" ")





