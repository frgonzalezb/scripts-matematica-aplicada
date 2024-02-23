# Determinar la FORMA ALGEBRAICA de la función que mejor se ajusta a un gráfico:
# Valor de m = (y2 - y1) / (x2 - x1)

# Para encontrar pendiente (m)
x1 = float(input("Ingrese el valor x1: "))
y1 = float(input("Ingrese el valor y1: "))
x2 = float(input("Ingrese el valor x2: "))
y2 = float(input("Ingrese el valor y2: "))

m = (y2 - y1) / (x2 - x1)

print(f"El valor de la pendiente (m) es {m}")

# Para encontrar coeficiente de posición (n)
if y1-(m*x1) == y2-(m*x2):
    print(f"El valor del coeficiente de posición (n) es {y1-(m*x1)}")
else:
    print("ERROR: No se puede obtener el coefieciente de posición (n)")