from os import system
system("cls")

def errorAlert(message):
    system("cls")
    print(message)

def pause():
    input("Presione ENTER para continuar...")

while True:
    range1=input("Ingrese el número entero inicial del rango: ")
    if range1.isnumeric():
        range1=int(range1)
    else:
        errorAlert("Caracter(es) no válido(s).")
        pause()
    range2=input("Ingrese el número entero final (n+1) del rango: ")
    if range2.isnumeric():
        range2=int(range2)
        break
    else:
        errorAlert("Caracter(es) no válido(s).")
        pause()

for n in range(range1,range2):
    sucesion=(-1)**n
    print(f"El {n}° término es {sucesion}")