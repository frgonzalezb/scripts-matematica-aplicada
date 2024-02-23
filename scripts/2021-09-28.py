from os import system
import numpy as np

def pausa():
    input("\nPresione ENTER para continuar...")

system("cls")

M = np.array([[4.04,0.39],
              [69,4],
              [61,2],
              [804, 66],
              [73,11]])

G = np.array([[30,45,50],
              [45,60,75]])
              
R=M.dot(G) # .dot() sirve para multiplicar matrices en este caso MxG
print(R)

pausa()

# FUNCIÓN LAMBDA PARA INGRESAR DATOS EN MATRICES:
# import numpy as np
T=np.fromfunction(lambda i,j:100*(i+1)*(j+1),(4,5)) #Vamos a tener que sumar 1 al i y al j
print(T)