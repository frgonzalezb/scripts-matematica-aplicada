from colorama import Fore, Style
from os import system
system("cls")

'''
# Otro algoritmo:
system("cls")
for n in range(1,501):
    sucesion=1/n
    print(f"El {n}° término es {sucesion}")
'''

system("cls")
suma=0
for n in range(1,60+1):
    sucesion=400+(n-1)*12
    suma+=sucesion # Acumulador !!!
    print(f"El {n}° término es {sucesion}")
print(f"La sumatoria de este grupo es: {suma}")