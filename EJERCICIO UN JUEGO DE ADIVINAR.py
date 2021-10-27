from random import randint

numero=randint( 1, 15)
a= int(input())
while a!=numero:
    if(a<numero):
        print("Has escrito un número menor")
    elif(a>numero):
        print("Has escrito un número mayor")
    a= int(input())
print("Has acertado el número")
