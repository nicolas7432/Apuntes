"""
                    Diferencias
C++ (arreglos)                  | Python (Listas)
Tamaño es fijo                  | Tamaño dinamico
Son de un mismo tipo            | Puede ser del mismo tipo o combinados

Similares
-Acceso a los elementos
-Posicion(Indices)

Para curiosos -> array con numpy

"""
#Nicolas Bahena Ostermaier

#Declarar o definir listas en Python

#Listas vacias
lista = []
print(lista)

#listas con elementos numericos
primos = [2,3,5,7,11,13]

#lista con elementos de cadenas
dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]

print(primos)
print(dias)

#listas con elementos combinados
fecha = [20,"octubre",2026,8.49]
print(fecha)

#lista de listas
peliculas = [["Spider-man Brand new day",2026],["El retorno del rey",2023]]
print(peliculas)

lista = [primos,dias,fecha]
print(lista)
