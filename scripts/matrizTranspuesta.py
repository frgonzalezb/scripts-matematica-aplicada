from os import system as sys
import numpy as np

sys("cls")
c = np.array([[120, 70],
             [150, 110],
              [80,160]])

A = c.T   # .(Matriz).T me generá la matriz Transpuesta

print(A)