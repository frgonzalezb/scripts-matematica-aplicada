# Fórmula general

a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
c = float(input("Ingrese un valor para el término independiente (c): "))
fx = float(input("Ingrese el valor a buscar 'f(x)': "))

xPos = (-b + (b**2 - 4*a*(c-fx))**0.5) / (2*a)
xNeg = (-b - (b**2 - 4*a*(c-fx))**0.5) / (2*a)

print(f"x (pos) = {xPos}")
print(f"x (neg) = {xNeg}")