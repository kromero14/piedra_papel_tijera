from random import *
print("Bienvenido ")
print("vamos a jugar ")
# input

X=(input("ingrese su decision: "))

#processing

Y=("piedra" ,"papel" ,"tijera" )

if X == Y:
    print("es un empate")
elif (X== "piedra" and Y == "tijera") or \
     (X== "papel" and Y == "piedra") or \
     (X== "tijera" and Y == "papel"):
    print("Ganaste",)
else:
    print("perdiste",) 