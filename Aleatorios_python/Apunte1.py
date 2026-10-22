#Apunte. Aleatorios en Python
import random

#random() ----> Generar valores aleatorios entre 0 y 1 (nunca llega al 1)
valor = random.random()
print("Valor aleatorio generado (0 y 1): ",valor)

#randrange(a) - randrange(a,b) - randrange(a,b,c)
valor = random.randrange(10)
print("Valor generado (0 y 9): ",valor)

valor = random.randrange(1,11)
print("Valor generado (1 y 10): ", valor)

valor = random.randrange(50,151,5)
print("Multiplos de 5 en un rango de 50-150: ", valor)

#randint(a,b) - Genera un valor aleatorio entre a y b (incluyendo ambos)
valor = random.randint(1,10)
print("Valor generado (1 y 10): ",valor)

#uniform(a,f) - Genera un valor flotante aleatorio entre a y b
valor = random.uniform(5,8)
print("Valores decimales (5 y 8): ",valor)

#Elegir de forma aleatorio de una lista
#choice(lista/secuencia)
valor = random.choice((10,20,30,40,50))
print("Valor elegido:",valor)

dias=["lunes","marte","miercoles","jueves","viernes"]
valor = random.choice(dias)
print("Valor elegido: ",valor)

valor = random.choice(["elefante","leon","cebra","capibara"])
print("Valor elegido: ",valor)

valor = random.choice("ANAHUAC-MAYAB") #Elige una letra de la cadena
print("Valor elegido: ",valor) 