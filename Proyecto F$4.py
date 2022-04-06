Se le solicita crear una calculadora de áreas en Python para las siguientes figuras geométricas, que muestre al usuario un menú de la siguiente forma.

username = input("Enter username:")
print("username is: " + username)


import math
math.pi
3.141592653589793
pi=math.pi

print("ingresar el radio")
radio=float(input())
area= 2 * pi * radio
print ("area de un circulo:")
print (area)



print("ingresar el lado")
lado=float(input())
area= lado * 2
print ("area de un cuadrado:")
print (area)



base=int(input("ingresar la base: "))
altura=int(input("ingresar la altura: "))
area= base * altura
print ("area del rectangulo es: ",area)
print (area)


d_menor=int(input("ingresar medida de la diagonal menor: "))
D_mayor=int(input("ingresar medida de la diagonal mayor: "))
area= (d_menor * D_mayor)/2
print ("area del rombo es: ",area)
print (area)




BaseMayor=int(input("ingrese la base mayor: "))
basemenor=int(input("ingrese la base menor: "))
altura=int(input("ingrese la altura: "))
area=((BaseMayor+basemenor)/2)*altura
print ("area del trapecio es: ",area)
print (area)


longitud=int(input("ingresar longitud: "))
apotema=int(input("ingresar apotema: "))
area= (5 * longitud * apotema)/2
print ("el area del poligono regular: ",area)
print (area)
