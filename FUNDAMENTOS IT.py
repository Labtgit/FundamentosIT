Username = input("Enter username:")
from datetime import datetime
now= datetime.now()
print("current time=",now)
import math
math.pi
3.141592653589793
pi=math.pi

print("Select option to peform")
print("1.Area de círculo.\n2.Area de Cuadrado.\n3.Area de Rectángulo.\n4.Area de Rombo\n5.Area de Romboide.\n6.Area de Trapecio.\n7.Area de Polígono Regular.\n8.Salir,S/N")
x=int(input("Choose the figure"))

if x==1:
    print("ingresar el radio")
radio=float(input())
area= pi * radio**2
print ("area de un circulo:")
print (area)

if x==2:
    print("ingresar el lado")
lado=float(input())
area= lado * 2
print ("area de un cuadrado:")
print (area)


if x==3:
    base =int(input("ingresar la base: "))
    altura=int(input("ingresar la altura: "))
area= base * altura
print ("area del rectangulo es: ",area)
print (area)

if x==4:
    d_menor=int(input("ingresar medida de la diagonal menor: "))
D_mayor=int(input("ingresar medida de la diagonal mayor: "))
area= (d_menor * D_mayor)/2
print ("area del rombo es: ",area)
print (area)

if x==5:
    base=int(input("ingresar la base: "))
altura=int(input("ingresar la altura: "))
area= base * altura
print ("area del romboide es: ",area)
print (area)

if x==6:
    BaseMayor=int(input("ingrese la base mayor: "))
basemenor=int(input("ingrese la base menor: "))
altura=int(input("ingrese la altura: "))
area=((BaseMayor+basemenor)/2)*altura
print ("area del trapecio es: ",area)
print (area)

if x==7:
    longitud=int(input("ingresar longitud: "))
apotema=int(input("ingresar apotema: "))
area= (5 * longitud * apotema)/2
print ("el area del poligono regular: ",area)
print (area)

