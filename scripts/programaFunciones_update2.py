# Programa para trabajar con funciones lineales y cuadráticas.
# Original elaborado entre el 16-11-2021 y el 17-11-2021 por Francisco González.
# Update 1 con fecha del 24-11-2021 por Francisco González.
# Update 2 con fecha del 02-12-2021 por Francisco González.



# Diccionario de funciones:
def funcionLineal(x,m,n):
    lineal = m*x + n
    print(f"f({x}) = {m} × {x} + {n} = {lineal}")

def funcionCuadratica(x,a,b,c):
    cuadratica = a*x**2 + b*x + c
    print(f"f({x}) = ({a} × {x}²) + ({b} × {x}) + {c} = {cuadratica}")



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
    print("3. Tip de uso en evaluaciones")
    print("4. Acerca de este programa")
    print("0. Salir\n")

def valorPendiente(x1,y1,x2,y2):
    pendiente = (y2 - y1) / (x2 - x1)
    return pendiente

def valorCoeficientePos(x1,y1,m):
    n = y1-(m*x1)
    return n

def calcuLineal():
    while True:
        try:
            m = float(input("Indique el valor de la pendiente (m): "))
            n = float(input("Indique el valor del coeficiente de posición (n): "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    while True:
        try:
            ini = int(input("Ingrese un valor entero inicial para el rango: "))
            fin = int(input("Ingrese un valor entero final para el rango: "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    for x in range(ini,fin+1):
        funcionLineal(x,m,n)
    print()
    pausa()

def calcuPendiente():
    while True:
        try:
            x1 = float(input("Ingrese el valor x1: "))
            y1 = float(input("Ingrese el valor y1: "))
            x2 = float(input("Ingrese el valor x2: "))
            y2 = float(input("Ingrese el valor y2: "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    m = valorPendiente(x1,y1,x2,y2)
    n = valorCoeficientePos(x1,y1,m)
    print(f"El valor de la pendiente (m) es {m}")
    print(f"El valor del coeficiente de posición (n) es {n}")
    pausa()

def ecuacionLineal():
    while True:
        try:
            m = float(input("Indique el valor de la pendiente (m): "))
            n = float(input("Indique el valor del coeficiente de posición (n): "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    x = -n / m
    print(f"El valor de la incógnita (x) es: {x}\n")
    pausa()

def menuLineal():
    while True:
        print("\nRECUERDA: Una función lineal se describe como:\n\nf(x) = mx + n\n")
        print("¿Qué desea hacer?:\n")
        print("1. Calcular una función lineal")
        print("2. Obtener el valor de la pendiente (m) y del coeficiente de posición (n)")
        print("3. Resolver una ecuación lineal y obtener la incógnita (x)")
        print("0. Volver al menú principal\n")
        opcion = input("Indique el dígito de su opción: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 0:
                print()
                break
            if opcion == 1:
                print("\nUd. ha escogido la opción 1: 'Calcular una función lineal'\n")
                calcuLineal()
            elif opcion == 2:
                print("\nUd. ha escogido la opción 2: 'Obtener el valor de la pendiente (m) y del coeficiente de posición (n)'\n")
                calcuPendiente()
            elif opcion == 3:
                print("\nUd. ha escogido la opción 3: 'Resolver una ecuación lineal y obtener la incógnita (x)'\n")
                ecuacionLineal()
            else:
                error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
        else:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

def calCuadratica():
    while True:
        try:
            a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
            b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
            c = float(input("Ingrese un valor para el término independiente (c): "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    while True:
        try:
            ini = int(input("Ingrese un valor entero inicial para el rango: "))
            fin = int(input("Ingrese un valor entero final para el rango: "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    for x in range(ini,fin+1):
        funcionCuadratica(x,a,b,c)
    print()
    pausa()

def verticeParabola():
    while True:
        try:
            a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
            b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
            c = float(input("Ingrese un valor para el término independiente (c): "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    Vx = -b / (2*a)
    Vy = a*Vx**2 + b*Vx + c
    print(f"\nEl vértice se encuentra en las coordenadas [{Vx}, {Vy}]\n")
    pausa()

def ecuacionCuadratica():
    while True:
        try:
            a = float(input("Ingrese un valor para el coeficiente cuadratico (a): "))
            b = float(input("Ingrese un valor para el coeficiente lineal (b): "))
            c = float(input("Ingrese un valor para el término independiente (c): "))
            fx = float(input("Ingrese el valor de 'f(x)': "))
            break
        except:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")
    x1 = (-b - (b**2 - 4*a*(c-fx))**0.5) / (2*a)
    x2 = (-b + (b**2 - 4*a*(c-fx))**0.5) / (2*a)
    print(f"\nx1 = {x1}")
    print(f"x2 = {x2}\n")
    pausa()

def menuCuadratica():
    while True:
        print("\nRECUERDA: Una función cuadrática se describe como:\n\nf(x) = ax² + bx + c\n")
        print("¿Qué desea hacer?:\n")
        print("1. Calcular una función cuadrática")
        print("2. Determinar el vértice de una función")
        print("3. Resolver una ecuación cuadrática y obtener los valores x1 y x2 de una 'f(x)' dada")
        print("0. Volver al menú principal\n")
        opcion = input("Indique el dígito de su opción: ")
        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 0:
                print()
                break
            elif opcion == 1:
                print("\nUd. ha escogido la opción 1: 'Calcular una función cuadrática'\n")
                calCuadratica()
            elif opcion == 2:
                print("\nUd. ha escogido la opción 2: 'Determinar el vértice de una función'\n")
                verticeParabola()
            elif opcion == 3:
                print("\nUd. ha escogido la opción 3: 'Resolver una ecuación cuadrática y obtener los valores x1 y x2 de una 'f(x)' dada'\n")
                ecuacionCuadratica()
            else:
                error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
        else:
            error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

def tipUso():
    print("\nTIP DE USO EN EVALUACIONES:\n")
    print("Antes que todo, revise completamente el cuestionario o prueba, dado que en algunos ejercicios pueden reiterarse casos y funciones.")
    print("Resuelva primero todos los ejercicios que hagan uso del mismo caso, luego avance a los que ocupen otro, y así sucesivamente.")
    print("De esta forma, Ud. se evita la molestia de reingresar la misma información una y otra vez.\n")
    print("¡SEA EFICIENTE! ¡AHORRE SU VALIOSO TIEMPO! 😉\n")
    pausa()

def acercaDe():
    print("\nACERCA DE:\n")
    print("Programa para trabajar con funciones lineales y cuadráticas.\n")
    print("Original elaborado entre el 16-11-2021 y el 17-11-2021 por Francisco González.")
    print("Update 1 con fecha del 24-11-2021 por Francisco González.\n")
    print("LICENCIA: Sí, está permitido modificar y compartir, siempre dando créditos al autor original (y sucesivos editores, si los hay).")
    print("Si quiere mandarme sus ediciones, sugerencias o reclamos, puede hacerlo al correo fr.gonzalezb@duocuc.cl 📩\n")
    print("¡NO SEA INGRATO! ¡SEA BUENA ONDA! 😎\n")
    pausa()

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
        elif opcion == 3:
            tipUso()
        elif opcion == 4:
            acercaDe()
        else:
            error("¡La opción ingresada no es válida! (╯°□°）╯︵ ┻━┻")
    else:
        error("¡Debe ingresar un valor numérico! (╯°□°）╯︵ ┻━┻")

# Capitulación
mensajeSalida()