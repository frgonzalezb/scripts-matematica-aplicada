from os import system as sys
import numpy as np

def limpiaPantalla():
    sys("cls")

def espacio():
    print(" ")

limpiaPantalla()
A = np.array([[2.6,  4.8,  1.8,  0.9],
              [3.2,  4.4,  2.5,  2.8],
              [2.4,  3.6,  3.8,  2.5]])

B = np.array([[3.6,  2.5,  3.0,  2.5],
              [4.5, 5, 3.5, 3.8],
              [2.9, 3.0, 4.6, 4]])

S = A+B # Definir la suma (La LETRA a ocupar no importa)
print("La matriz A + B es:")
print(S)
espacio()
# NUEVO EJERCICIO 21-09-2021
V = np.array([[30,34,20],
              [45,20,16],
              [14,26,25]])

T = np.array([[35,30,26],
              [52,25,18],
              [23,24,32]])

Suma = V+T # Definir la suma (La LETRA a ocupar no importa)
print("La matriz V + T es:")
print(Suma)
espacio()
print("La letra B se responde con:")
print((V*1.3)+(T*0.9))
espacio()

# Multiplicaciones de matrices 22-09-2021
Alpha = np.array([[1, 2],
                  [3, 2]])

Beta = np.array([[290, 312],
                 [345, 413]])

Gamma = Alpha.dot(Beta) # La función .dot() es para multiplicar en numpy !!!
print("La matriz Alpha * Beta es:")
print(Gamma)
espacio()

# Otro ejercicio
Ventas = np.array([[1300, 900, 800],
                  [2100, 1700, 1500],
                  [1500, 1200, 900]])

Precio = np.array([[3600, 900, 1500]])

I = Precio.dot(Ventas)
print("La matriz Ventas * Precio es:")
print(I)
espacio()