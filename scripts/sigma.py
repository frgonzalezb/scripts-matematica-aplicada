from os import system
system("cls")

suma=0
for n in range(1,1764+1): # range puede cambiar a lo usted quiera
    sucesion = 226+(n-1)*-12 #La sucesión se va modificando
    suma = sucesion + suma # sirve para ir haciendo un bucle con la suma
    print (f' El término {n} es = {sucesion}') # corroborar que terminos se estan sumando
print (f'La suma de los términos es = {round(suma)}')