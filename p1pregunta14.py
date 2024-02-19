'''
PREGUNTA 14
Una compañía que fabrica exclusivamente un solo tipo de producto, tiene 2 plantas de producción y 3 bodegas de almacenamiento.
La matriz T igual paréntesis izquierdo t subíndice i j fin subíndice paréntesis derecho nos detalla las unidades producidas
mensualmente en la planta i y que son transportadas a la bodega j para ser almacenadas durante su respectivo mes de producción.
Por otra parte, la matriz U igual paréntesis izquierdo u subíndice i j fin subíndice paréntesis derecho nos indica
el costo en dólares de almacenar 1 unidad de este producto durante el mes j en la bodega i.
Esta información es sólo para los 4 primeros meses del presente año.
'''

import numpy as np

print("")
# a) Si t subíndice i j fin subíndice igual 70 por i por j, calcule completamente la matriz T    (2 puntos).
T=np.fromfunction(lambda i,j:70*(i+1)*(j+1),(2,3))
print("a) RESPUESTA: La matriz T es:")
print(T)
print("")

# b) Si u subíndice i j fin subíndice igual 2 i más 4 j, calcule completamente la matriz U    (2 puntos).
U=np.fromfunction(lambda i,j:1*(2*i+1)*(4*j+1),(2,3))
print("b) RESPUESTA: La matriz U es:")
print(U)
print("")

# c) Si A igual T por U, calcule solamente el elemento a subíndice 21 y además interprete este resultado.    (2 puntos).