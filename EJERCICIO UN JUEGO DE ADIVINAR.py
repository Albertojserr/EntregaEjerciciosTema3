from random import randint
print("Ejercicio entre 1 y 15")
numero=randint( 1, 15)
minumero= int(input("Escribe un número:"))
while minumero!=numero:
    if(minumero<numero):
        print("Has escrito un número menor")
    elif(minumero>numero):
        print("Has escrito un número mayor")
    minumero= int(input("Escribe otro número:"))
print("Has acertado el número")

print("Ejercicio entre 1 y 300")
intentos=0
numero=randint(1,300)
minumero=0
while (intentos<9 and minumero!=numero):
    minumero= int(input("Escribe un número:"))
    if(minumero<numero):
        print("Has escrito un número menor")
    elif(minumero>numero):
        print("Has escrito un número mayor")
    intentos+=1

if(minumero==numero):
    print("Has acertado el número")
else:
    print("Te has pasado de intentos, el número era", numero)