# Generador de matrices con NumPy, versión alpha por Francisco González, 01-10-2021.
# De antemano, agradecido de todas las colaboraciones para hacer de este programa una gran herramienta. 😊

from os import system as sys # Eliminar esta cosa en collab
import numpy as np

# Definiciones útiles:
def limpiame(): # Eliminar esta cosa en collab
    sys('cls')

def error(msg):
    print('\nERROR:\n'+msg)

limpiame() # Eliminar esta cosa en collab

# Pedir nro. de FILAS al usuario:
while True:
    x = input('Ingrese la cantidad de FILAS que necesita para su matriz: ')
    if x.isnumeric():
        x = int(x)
        if x > 0:
            break
        else:
            error('Debe ser un número ENTERO mayor a cero !!!')
    else:
        error('El valor debe ser numérico !!!')

# Pedir nro. de COLUMNAS al usuario:
while True:
    y = input('Ingrese la cantidad de COLUMNAS que necesita para su matriz: ')
    if y.isnumeric():
        y = int(y)
        if y > 0:
            break
        else:
            error('Debe ser un número ENTERO mayor a cero !!!')
    else:
        error('El valor debe ser numérico !!!')

print('\nSe generará una matriz base con ceros:\n')
matriz = np.zeros(shape=(x,y))
print(matriz)

print('')
for i in range(x):
    matriz = np.append(matriz, np.array(matriz), axis=0)
    for j in range(y):
        num = int(input(f'Ingrese un valor ENTERO para [{i+1}, {j+1}]: '))
        matriz[i:j] = [num]

# matriz[0] = [1,2] # Se reemplaza la primera fila de [0. 0.] con [1. 2.]
print('La nueva matriz es:\n')
print(matriz)