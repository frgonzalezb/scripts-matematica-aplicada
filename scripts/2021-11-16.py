# Programa mejorado
def presioneEnter():
    input("Presione ENTER para continuar...")

a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
c = float(input("Ingrese un valor para el término independiente (c): "))

ini = int(input("Ingrese un valor entero inicial para el rango: "))
fin = int(input("Ingrese un valor entero final para el rango: "))

for x in range(ini,fin+1):
    cuadratica = a*x**2 + b*x + c
    print(f"f({x}) = ({a} * {x}²) + ({b} * {x}) + {c} = {cuadratica}")

Vx = -b / (2*a)
Vy = a*Vx**2 + b*Vx + c
print(f"\nLas coordenadas del vértice son [{Vx}, {Vy}]")
presioneEnter()



# Código compartido por la profe, es de un compañero de otra sección (Jason)
from os import system as sys
sys("cls")

nums=[]
num=float(input("Ingrese un número a buscar: "))

for x in range(0, 100000):
    fx=x**2-180*x+20000     #función
    if fx==num:             #si el número coincide
        nums.append(x)      #agrégalo a la lista

print()
print(f"{num} se encuentra en el(los) lugar(es):", end=" ") 

for i in range(len(nums)):   #el for es solo para que salga con la coma
    if i==(len(nums)-1):    #si el número de la lista es el último
        print(nums[i])     #sin coma
    else:           #si es el último
        print(nums[i], end=", ")  #con coma