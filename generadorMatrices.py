# Todos los créditos del código original a Maykol Villena el 28-09-2021. Un crack! (⌐■_■)

# Importando algunas utilidades (obviar en collab)
from os import system

# ------------------------------ Separador de bajo presupuesto ------------------------------

# Definiendo funciones:
def limpiame(): # Eliminar esta def en collab
    system("cls")

def pausa():
    input("Pulsa ENTER para continuar...\n")

def error(msg):
    print("ERROR !!!\n"+msg)
    pausa()

def holiwi():
    print("Amigo Python presenta...\n")
    print("*-----------------------*")
    print("| GENERADOR DE MATRICES |")
    print("*-----------------------*\n")
    print("Genera dos matrices, verifica su orden y otras sorpresas más !!! o(*￣▽￣*)o\n")

# ------------------------------ Separador de bajo presupuesto ------------------------------

# INTRO
limpiame() # Obviar esto en collab
holiwi()
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PASO 1: Definir nombre (letra) de la primera matriz
while True:
    limpiame() # Obviar esto en collab
    nomMatrizA = input("Ingresa una letra para nombrar la primera matriz: ")
    if nomMatrizA.isnumeric():
        error("Debe ser una LETRA !!! (╯‵□′)╯︵┻━┻")
    else:
        if len(nomMatrizA) > 1 or len(nomMatrizA) == 0:
            error("Debe ser UNA SOLA LETRA !!! (╯‵□′)╯︵┻━┻")
            pausa()
        else:
            nomMatrizA = str(nomMatrizA).upper()
            break

# PASO 2: Definir el número de filas (i) de la primera matriz
while True:
    limpiame() # Obviar esto en collab
    filaA=input(F"Ingresa la cantidad de filas (i) para la matriz {nomMatrizA}: ")
    if filaA.isnumeric():
        filaA = int(filaA)
        if filaA == 0:
            error("La cantidad de filas debe ser igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")
        else:
            break
    else:
        error("Debe ser un valor ENTERO igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")

# PASO 3: Definir el número de columnas (j) de la primera matriz
while True:
    limpiame() # Obviar esto en collab
    columnaA=input(F"Ingresa la cantidad de columnas (j) para la matriz {nomMatrizA}: ")
    if columnaA.isnumeric():
        columnaA = int(columnaA)
        if columnaA == 0:
            error("La cantidad de columnas debe ser igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")
        else:
            break
    else:
        error("Debe ser un valor ENTERO igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")

# PASO 4: Ingresar valores en la primera matriz
matrizA = []
limpiame() # Obviar esto en collab
print(f"Matriz {nomMatrizA}")
for i in range(filaA): # Remember: i = FILAS
    matrizA.append([])
    for j in range(columnaA): # Remember: j = COLUMNAS
        num = input(f"Ingresa un valor para Fila {i+1} Columna {j+1}: ")
        if num.isnumeric():
            num = int(num)
            matrizA[i].append(num)
        else:
            error("Debe ser un valor ENTERO !!! (╯‵□′)╯︵┻━┻")
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PASO 5: Definir nombre (letra) de la segunda matriz
while True:
    limpiame() # Obviar esto en collab
    nomMatrizB = input("Ingresa una letra para nombrar la segunda matriz: ")
    if nomMatrizB.isnumeric():
        error("Debe ser una LETRA !!! (╯‵□′)╯︵┻━┻")
    else:
        if len(nomMatrizB) > 1 or len(nomMatrizB) == 0:
            error("Debe ser UNA SOLA LETRA !!! (╯‵□′)╯︵┻━┻")
        else:
            nomMatrizB = str(nomMatrizB).upper()
            break

# PASO 6: Definir el número de filas (i) de la segunda matriz
while True:
    limpiame() # Obviar esto en collab
    filaB=input(F"Ingrese la cantidad de filas (i) para la matriz {nomMatrizB}: ")
    if filaB.isnumeric():
        filaB = int(filaB)
        if filaB == 0:
            error("La cantidad de filas debe ser igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")
        else:
            break
    else:
        error("Debe ser un valor ENTERO igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")

# PASO 7: Definir el número de columnas (j) de la segunda matriz
while True:
    limpiame() # Obviar esto en collab
    columnaB=input(F"Ingrese la cantidad de columnas (j) para la matriz {nomMatrizB}: ")
    if columnaB.isnumeric():
        columnaB = int(columnaB)
        if columnaB == 0:
            error("La cantidad de columnas debe ser igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")
        else:
            break
    else:
        error("Debe ser un valor ENTERO igual o mayor a 1 !!! (╯‵□′)╯︵┻━┻")

# PASO 8: Ingresar valores en la segunda matriz
matrizB = []
limpiame() # Obviar esto en collab
print(f"Matriz {nomMatrizB}")
for i in range(filaB): #FILAS
    matrizB.append([])
    for j in range(columnaB): #COLUMNAS
        num = input(f"Ingrese valor para Fila {i+1} Columna {j+1}: ")
        if num.isnumeric():
            num = int(num)
            matrizB[i].append(num)
        else:
            error("Debe ser un valor ENTERO !!! (╯‵□′)╯︵┻━┻")
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PARTE 9: RESULTADOS !!!
limpiame() # Obviar esto en collab
print("\nENHORABUENA !!!")
print(f"\nMatriz {nomMatrizA}: ")
for x in range(matrizA.__len__()): #SOLO PARA MOSTRAR VALORES DE LA MATRIZ
    print(matrizA[x])
print(f"Orden de la matriz {nomMatrizA}: {filaA}x{columnaA}")
print(f"\nMatriz {nomMatrizB}: ")
for x in range(matrizB.__len__()): #SOLO PARA MOSTRAR VALORES DE LA MATRIZ
    print(matrizB[x])
print(f"Orden de la matriz {nomMatrizB}: {filaB}x{columnaB}\n")

# PARTE 10: MÁS RESULTADOS !!!
print("Además...")
if filaA == filaB and columnaA == columnaB:
    print(f"Las matrices {nomMatrizA} y {nomMatrizB} se pueden sumar.")
else:
    print(f"Las matrices {nomMatrizA} y {nomMatrizB} no se pueden sumar.")

if columnaA == filaB:
    print(f"Las matrices {nomMatrizA} y {nomMatrizB} se pueden multiplicar.")
else:
    print(f"Las matrices {nomMatrizA} y {nomMatrizB} no se pueden multiplicar.\n")
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# CRÉDITOS:
print("*** CRÉDITOS ***")
print("\nCódigo original: Maykol Villena, 28-09-2021. (⌐■_■)")
print("\nSegunda edición: Francisco González, 29-09-2021. (⌐■_■)")
print("\nTodos los derechos e izquierdos bien puestos. (⌐■_■) (⌐■_■)\n")