# Algoritmo de Maykol modificado por Francisco G. v0.3a
# Créditos a Maykol Villena por el código original y a la profe Karen Venegas por su ayuda. UwU

# Limpia-consolas de bajo presupuesto:
from os import system
system("cls")

# Número a buscar en el ciclo FOR:
while True:
    buscar=input("Ingrese un número a buscar: ")
    if buscar.isnumeric(): # Este if/else es un validador (de que el input sea efectivamente numérico entero)
        buscar=int(buscar)
        break
    else:
        input("ERROR: Caracter(es) no válido(s) !!! (╯°□°)╯︵ ┻━┻\n\nPresione ENTER para continuar...")

# Definir rangos del ciclo FOR:
while True:
    range1=input("Ingrese un número entero INICIAL para el rango: ")
    if range1.isnumeric():
        range1=int(range1)
        range2=input("Ingrese un número entero FINAL para el rango: ")
        if range2.isnumeric():
            range2=int(range2)
            break
        else:
            input("ERROR: Caracter(es) no válido(s) !!! (╯°□°)╯︵ ┻━┻\n\nPresione ENTER para continuar...")
    else:
        input("ERROR: Caracter(es) no válido(s) !!! (╯°□°)╯︵ ┻━┻\n\nPresione ENTER para continuar...")

# SUGERENCIA SIMÓN:
# resultados={
#     "-":"Sucesión ARITMÉTICA. La DIFERENCIA es: ",
#     "/":"Sucesión GEOMÉTRICA. La RAZÓN es: "
# }
# for op in resultados.keys():
#     var=round(eval(f"{num2} {op} {num1}"),2)
#     if var==round(eval(f"{num3} {op} {num2}"),2):
#         print(f"{resultados.get(op)} {var}")
#         break
#     else:
#         print("No es una sucesión aritmética ni geométrica")

for n in range(range1,range2):
    sucesion=3*n # AQUÍ VA LA FÓRMULA !!! Cámbiela si quiere :)
    if sucesion==buscar:
        input(f"En el {n}° término se encuentra {sucesion} !!!\n\nMuy bien !!! UwU")
        break
    elif sucesion!=buscar and n<range2:
        continue
    elif sucesion!=buscar and n==range2:
        print("El número no se encuentra en la sucesión !!! (╯°□°)╯︵ ┻━┻")