# Clase de funciones LINEALES

# Función lineal algebraicamente: f(x) = mx + n
# m = pendiente (ascenso o disminución de la función)
# m != 0, obligatorio
# n = coeficiente de posición (aka: base, punto de inicio, corte con eje y)

# Ejemplo de consumo de luz
def consumoLuz():
    while True:
        print("La cuenta de luz se modela mediante la siguiente función:")
        print("f(k) = 300k + 1000")
        print("donde k son los kW/h de consumo")
        k = float(input("\nIngrese la cantidad de kW/h que Ud. ha consumido: "))
        fk = 300*k+1000
        print(f"Ud. debe pagar ${fk} por {k} kW/h consumido")
        retry = input("\n¿Reintentar? s/n:\n").upper()
        if retry == 'N':
            break

# P1: Altura promedio en cm H(a) de un niño durante su primer año de edad
def alturaNino():
    for a in range(0,12+1):
        ha = 2.3*a+48
        print(f"A los {a} meses, la altura del niño será de {ha} cm.")
    print()