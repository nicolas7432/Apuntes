#Nicolas Bahena Ostermaier
#Apunte 4
def potencia2(num):
    return num**2

def esPar(num):
    if num%2==0:
        return True
    else:
        return False

def calcularEdad(anio):
    edad=2026-anio
    return "Tu edad es: "+str(edad) + " años"

x=potencia2(9)
print(f"Potencia 2 de (9): {x}")

print(f"Potencia 2 de (15): {potencia2(15)}")

numero = int(input("Ingresa un numero: "))
print(f"Potencia 2 de ({numero}): {potencia2(numero)}")

print(f"9 es par: {esPar(9)}")
print(f"62 es par: {esPar(62)}")

anioNac=int(input("Ingresa tu año de nacimiento: "))
print(calcularEdad(anioNac))
