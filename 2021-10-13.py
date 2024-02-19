# CLASE DE FUNCIONES

# Ejercicio de la regla de Young.

# Versión con ciclo FOR para obtener todas las dosis del rango de edades.
for x in range(1,12+1):
    fx = 500*x/(x+12)
    print(f"Según la regla de Young, un niño de {x} años debe tomar una dosis de {round(fx, 2)} mg.")
print()

# Versión con ciclo WHILE para obtener la dosis para una determinada edad dentro del rango anterior.
while True:
    edadNiño = int(input("Ingrese la edad del niño en años (valor entero, sin aproximar): "))
    if edadNiño < 1:
        print("ERROR: La edad del niño es insuficiente para aplicar la regla de Young.")
    elif edadNiño > 12:
        print("ERROR: La edad del niño es demasiado alta para aplicar la regla de Young.")
    else:
        break

reglaYoung = 500*edadNiño / (edadNiño+12)
print(f"Según la regla de Young, un niño de {edadNiño} años debe tomar una dosis de {round(reglaYoung, 2)} mg.")