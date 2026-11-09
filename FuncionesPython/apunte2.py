#Nicolas Bahena Ostermaier
#Apunte 2
a=0
b=0

def lectura():
    global a,b
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))

def suma():
    print(f"La suma es: {a+b}")

def resta():
    print(f"La resta es: {a-b}")

def multiplicacion():
    print(f"La multiplicacion es: {a*b}")

def division():
    if b!=0:
        print(f"La division es: {a/b}")
    else:
        print("Division por cero")

#------Invocacion de funciones
print("OPERACIONES ARITMETICAS")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
opc=int(input("¿Que operacion desea realizar?"))

lectura()

if opc==1:
    suma()
elif opc==2:
    resta()
elif opc==3:
    multiplicacion()
elif opc==4:
    division()
else:
    print("Opcion no valida")

