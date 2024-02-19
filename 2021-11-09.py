# Funciones cuadráticas
# f(x) = a*x**2 + b*x + c
#
# Si (a) es positivo, la parábola va hacia arriba; si negativo, hacia abajo.
# El término independiente (c) es el punto donde intersecta el eje y.
# ༼;´༎ຶ ۝ ༎ຶ༽

print("GOOGLE COLAB")
a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
c = float(input("Ingrese un valor para el término independiente (c): "))

for x in range(1,10+1):
    cuadratica = a*x**2 + b*x + c
    print(f"f({x}) = ({a} * {x}²) + ({b} * {x}) + {c} = {cuadratica}")

input("\nAhora, veremos un gráfico elaborado con MATPLOTLIB.\nPresione ENTER para continuar...")

import matplotlib.pyplot as plt

ag=[]
bg=[]

for x in range(-10,10,1):
    y = a*x**2+b*x+c
    ag.append(x)
    bg.append(y)
    # x = x+1

fig = plt.figure()
axes = fig.add_subplot(111)
axes.plot(ag,bg)
plt.grid()
plt.show()