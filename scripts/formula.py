from colorama import Fore, Style
from os import system
system("cls")

# Otro algoritmo: a1+(n-1)+d, donde a1 es el primer término y d indica la diferencia entre los elementos de la sucesión (decreciente es negativo).
system("cls")
for n in range(21,22):
    sucesion=30+(n-1)*-3
    print(f"El {n}° término es {sucesion}")