# Archivo para testear cosas chicas:

funciones = []

while True:
    elementos = []
    a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
    elementos.append(a)
    b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
    elementos.append(b)
    c = float(input("Ingrese un valor para el término independiente (c): "))
    elementos.append(c)
    funciones.append(elementos)
    otra = input("¿Agregar más elementos? s/n: ").upper()
    if otra == "N":
        break

ini = int(input("Ingrese un valor entero inicial para el rango: "))
fin = int(input("Ingrese un valor entero final para el rango: "))
for x in range(ini,fin+1):
    cuadratica = a*x**2 + b*x + c
    print(f"f({x}) = ({a} * {x}²) + ({b} * {x}) + {c} = {cuadratica}")