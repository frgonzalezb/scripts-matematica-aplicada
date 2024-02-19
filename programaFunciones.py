# Programa para trabajar con funciones lineales y cuadráticas.
# Elaborado entre el 16-11-2021 y el 17-11-2021 por Francisco González.

# Permitido modificar y compartir, dando créditos al autor original (y sucesivos, si hay).

# Diccionario de funciones:
def funcionLineal(x,m,n):
    lineal = m*x + n
    print(f"f({x}) = {m} * {x} + {n} = {lineal}")

def funcionCuadratica(x,a,b,c):
    cuadratica = a*x**2 + b*x + c
    print(f"f({x}) = ({a} * {x}²) + ({b} * {x}) + {c} = {cuadratica}")



# Diccionario de partes de funciones:
def valorPendiente(x1,y1,x2,y2):
    pendiente = (y2 - y1) / (x2 - x1)
    return pendiente

def valorCoeficientePos(x1,y1,m):
    n = y1-(m*x1)
    return n

def verticeParabola(a,b,c):
    Vx = -b / (2*a)
    Vy = a*Vx**2 + b*Vx + c
    print(f"\nEl vértice se encuentra en las coordenadas [{Vx}, {Vy}]\n")



# Diccionario de elementos funcionales del programa:
def pausa():
    input("Presione ENTER para continuar...")
    print()

def error(mensaje):
    print("\nERROR: " + mensaje)
    pausa()

def menuPrincipal():
    print("############################")
    print("# CALCULADORA DE FUNCIONES #")
    print("#  LINEALES Y CUADRÁTICAS  #")
    print("############################")
    print("\nOpciones:\n")
    print("1. Menú función lineal")
    print("2. Menú función cuadrática")
    print("0. Salir\n")

def menuLineal():
    while True:
        print("\nUna función lineal se describe como:\n\nf(x) = m*x + n\n")
        print("¿Qué desea hacer?:\n")
        print("1. Calcular una función lineal")
        print("2. Obtener el valor de la pendiente (m) y del coeficiente de posición (n)")
        print("0. Volver al menú principal\n")
        opcion = input("Indique el dígito de su opción: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 0:
                print()
                break
            if opcion == 1:
                print("\nUd. ha escogido la opción 1: 'Calcular una función lineal'\n")
                m = float(input("Indique el valor de la pendiente (m): "))
                n = float(input("Indique el valor del coeficiente de posición (n): "))
                ini = int(input("Ingrese un valor entero inicial para el rango: "))
                fin = int(input("Ingrese un valor entero final para el rango: "))
                for x in range(ini,fin+1):
                    funcionLineal(x,m,n)
                pausa()
            elif opcion == 2:
                print("\nUd. ha escogido la opción 2: 'Obtener el valor de la pendiente (m) y del coeficiente de posición (n)'\n")
                x1 = float(input("Ingrese el valor x1: "))
                y1 = float(input("Ingrese el valor y1: "))
                x2 = float(input("Ingrese el valor x2: "))
                y2 = float(input("Ingrese el valor y2: "))
                m = valorPendiente(x1,y1,x2,y2)
                n = valorCoeficientePos(x1,y1,m)
                print(f"El valor de la pendiente (m) es {m}")
                print(f"El valor del coeficiente de posición (n) es {n}")
                pausa()
            else:
                error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
        else:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

def menuCuadratica():
    while True:
        print("\nUna función cuadrática se describe como:\n\nf(x) = a*x**2 + b*x + c\n")
        print("¿Qué desea hacer?:\n")
        print("1. Calcular una función cuadrática + vértice")
        print("0. Volver al menú principal\n")
        opcion = input("Indique el dígito de su opción: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 0:
                print()
                break
            if opcion == 1:
                print("\nUd. ha escogido la opción 1: 'Calcular una función cuadrática + vértice'\n")
                a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
                b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
                c = float(input("Ingrese un valor para el término independiente (c): "))
                ini = int(input("Ingrese un valor entero inicial para el rango: "))
                fin = int(input("Ingrese un valor entero final para el rango: "))
                for x in range(ini,fin+1):
                    funcionCuadratica(x,a,b,c)
                verticeParabola(a,b,c)
                pausa()
            else:
                error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
        else:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

def mensajeSalida():
    print("\n¡Muchas gracias por usar este programa! ヾ(￣▽￣) Bye~Bye~")
    print("\nPrograma elaborado por Francisco González. Noviembre 2021.\n")



# Programa principal:
while True:
    menuPrincipal()
    opcion = input("Indique el dígito de su opción: ")
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion == 1:
            menuLineal()
        elif opcion == 2:
            menuCuadratica()
        else:
            error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
    else:
        error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

# Capitulación
mensajeSalida()