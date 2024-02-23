from os import system as sys
import numpy as np

def limpiame():
    sys('cls')

limpiame()

# PARTE 1: CREAR MATRICES
print("- Matriz creada con una lista de listas:")
lista_de_listas=[   [1  ,-4], 
                    [12 , 3], 
                    [7.2, 5]]
matriz = np.array(lista_de_listas)
print(matriz)

print("- Matriz creada con np.zeros:")
dimensiones=(2,3)
matriz_ceros = np.zeros(dimensiones)
print(matriz_ceros)

print("- Matriz creada con np.ones:")
dimensiones=(3,2)
matriz_unos = np.ones(dimensiones)
print(matriz_unos)

# También podemos usar np.copy para copiar una matriz 
print("- Copia de la matriz creada con np.ones:")
matriz_unos_copia=np.copy(matriz_unos)
print(matriz_unos_copia)

# Otro ejemplo sacado de otra parte
print('')
array = np.empty((3, 0), int)
array = np.append(array, np.array([[11], [21], [31]]), axis=1)
array = np.append(array, np.array([[12, 22, 32]]).transpose(), axis=1)
print(array)

# Otro ejemplo más
print('')
a = np.zeros(shape=(5,2))
print(a)
print('')
a[0] = [1,2]
a[1] = [2,3]
print(a)