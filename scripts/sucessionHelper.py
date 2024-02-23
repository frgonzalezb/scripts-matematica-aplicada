# sucessionHelper: Ayudante de Matemática Aplicada
# v0.1 del 09-09-2021
# ...
# Ideado por: Francisco González (alias: Funko de Vision, Esposo de Wanda, etc.)
# ...
# Desarrollado por:
# -> Francisco González (⌐■_■)
# -> Simón Salinas (⌐■_■)
# -> Maykol Villena (⌐■_■)
# ...
# Inspirado por: Profe Karen o(*^＠^*)o
#
# Todos los derechos e izquierdos bien reservados. (>_O)



# PARTE 0: Librerías (obviar esta parte en IDE basados en web)
from os import system

# PARTE 1: Variables
def limpiaPantalla():
    system("cls")

def menuPrincipal():
    print("""+-*/ SUCESSIONHELPER: TU AYUDANTE DE MATEMÁTICA APLICADA \*-+

¿Qué desea hacer?

(1) Verificar una sucesión
(2) Resolver una sucesión ARITMÉTICA
(3) Resolver una sucesión GEOMÉTRICA
(4) Salir
        """)

def menuValidacion():
    print("""Bienvenide al VERIFICADOR DE SUCESIONES !!! (●'◡'●)

Ingrese 3 términos sucesivos de una secuencia de números para validar el tipo de sucesión (aritmética o geométrica).

POR EJEMPLO: {2, 4, 8} o {1.5, 3.0, 4.5}
                """)

def esAritmetica(n1,n2,n3):
    return(n2-n1==n3-n2)

def esGeometrica(n1,n2,n3):
    return(n2/n1==n3/n2)

def diferencia():
    return(n2-n1)

def razon():
    return(n2/n1)

def pausa():
    input("Presione ENTER para continuar...")

def errorInt():
    limpiaPantalla()
    print("ERROR: Debe ingresar un número ENTERO !!! (╯°□°)╯︵ ┻━┻")
    pausa()

def errorNum():
    limpiaPantalla()
    print("ERROR: Debe ingresar un NÚMERO ENTERO O DECIMAL !!! (╯°□°)╯︵ ┻━┻")
    pausa()

# REMEMBER:
# sucesionAritmetica = a1+(n-1)*d
# sucesionGeometrica = a1*r**(n-1)

# PARTE 2: Programa principal
while True:
    while True:
        limpiaPantalla()
        menuPrincipal()
        opcion=input("Indique el número de su opción: ")
        if opcion=="1":
            while True:
                limpiaPantalla()
                menuValidacion()
                try:
                    n1,n2,n3=[float(input(f"Ingrese el {i}° término de la sucesión: ")) for i in range(1,3+1)]
                    break
                except ValueError as e:
                    errorNum()
            if esAritmetica(n1,n2,n3):
                print(f"\nLa sucesión es ARITMÉTICA.\nLa DIFERENCIA es {diferencia()}")
                retry=input("\n¿Desea volver a intentarlo?\nIndique S o N: ").upper()
                if retry=="S":
                    continue
                elif retry=="N":
                    break
            elif esGeometrica(n1,n2,n3):
                print(f"\nLa sucesión es GEOMÉTRICA.\nLa RAZÓN es {razon()}")
                retry=input("\n¿Desea volver a intentarlo?\nIndique S o N: ").upper()
                if retry=="S":
                    continue
                elif retry=="N":
                    break
            else:
                print("La sucesión ingresada NO es aritmética ni geométrica")
        elif opcion=="2":
            while True:
                limpiaPantalla()
                try:
                    a1=[float(input("Indique el número INICIAL (a1) de la sucesión: ")) for i in range(0,1)]
                    break
                except ValueError as e:
                    errorNum()
            while True:
                try:
                    d=[float(input("Indique la DIFERENCIA (d) de la sucesión: ")) for i in range(0,1)]
                    break
                except ValueError as e:
                    errorNum()
            while True:
                limpiaPantalla()
                r1=input("Ingrese un número entero INICIAL para el rango: ")
                if r1.isnumeric():
                    r1=int(r1)
                    r2=input("Ingrese un número entero FINAL para el rango: ")
                    if r2.isnumeric():
                        r2=int(r2)
                        break
                    else:
                        errorInt()
                else:
                    errorInt()
            for n in range(r1,r2):
                sucesion=a1+(n-1)*d
                print(f"El {n}° término es {sucesion}")
            pausa()
        elif opcion=="3":
            print
        elif opcion=="4":
            print