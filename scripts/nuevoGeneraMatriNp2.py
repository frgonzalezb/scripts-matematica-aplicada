# Generador de matrices v.3.0. NUMPY-COMPATIBLE !!!
# Todos los créditos del código original a Maykol Villena el 28-09-2021. Un crack! (⌐■_■)

# Importando amigo Numpy
import numpy as np

# ------------------------------ Separador de bajo presupuesto ------------------------------

# Definiendo funciones:
def separador():
    print("---------------------------------------------------------------------------\n")

def pausa():
    input("Pulsa ENTER para continuar...\n")

def error(msg):
    print("\nERROR !!!\n"+msg)
    pausa()

def holiwi():
    print("Amigo Python presenta...\n")
    print("*-----------------------*")
    print("| GENERADOR DE MATRICES |")
    print("*-----------------------*")
    print("    (Colab Edition)\n")

def pantallaMenu1():
    print("*--------------*")
    print("| MENÚ INICIAL |")
    print("*--------------*\n")
    print("¿Qué desea hacer?\n")
    print("1. Crear dos matrices con la función lambda")
    print("2. Crear dos matrices personalizadas elemento-a-elemento")
    print("0. Salir\n")

def pantallaMenu2():
    print("*------------------*")
    print("| MENÚ DE OPCIONES |")
    print("*------------------*\n")
    print("¿Qué desea hacer con las matrices generadas?\n")
    print("1. Sumar matrices")
    print("2. Multiplicar matrices")
    print("3. Transponer una matriz")
    print("0. Salir\n")

# ------------------------------ Separador de bajo presupuesto ------------------------------

# INTRO
separador()
holiwi()
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

'''
# PASO 1: Definir nombre (letra) de la primera matriz
separador()
while True:
    nomMatrizA = input("Ingresa una letra para nombrar la primera matriz: ")
    if nomMatrizA.isnumeric():
        error("Debe ser una LETRA !!! (╯‵□′)╯︵┻━┻")
        pausa()
    else:
        if len(nomMatrizA) > 1 or len(nomMatrizA) == 0:
            error("Debe ser UNA SOLA LETRA !!! (╯‵□′)╯︵┻━┻")
            pausa()
        else:
            nomMatrizA = str(nomMatrizA).upper()
            break

# PASO 2: Definir el número de filas (i) de la primera matriz
while True:
    filaA=input(f"Ingresa la cantidad de FILAS para la matriz {nomMatrizA}: ")
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
    columnaA=input(f"Ingresa la cantidad de COLUMNAS para la matriz {nomMatrizA}: ")
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
print(f"\nMatriz {nomMatrizA}")
for i in range(filaA): # Remember: i = FILAS
    matrizA.append([])
    for j in range(columnaA): # Remember: j = COLUMNAS
        num = float(input(f"Ingresa un valor numérico POSITIVO para las coordenadas [{i+1}, {j+1}]: "))
        matrizA[i].append(num)
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PASO 5: Definir nombre (letra) de la segunda matriz
separador()
while True:
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
    filaB=input(f"Ingrese la cantidad de FILAS para la matriz {nomMatrizB}: ")
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
    columnaB=input(f"Ingrese la cantidad de COLUMNAS para la matriz {nomMatrizB}: ")
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
print(f"\nMatriz {nomMatrizB}")
for i in range(filaB): #FILAS
    matrizB.append([])
    for j in range(columnaB): #COLUMNAS
        num = float(input(f"Ingresa un valor numérico POSITIVO para las coordenadas [{i+1}, {j+1}]: "))
        matrizB[i].append(num)
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PARTE 9: RESULTADOS !!!
separador()
print("\n--- ENHORABUENA !!! ---")

print(f"\nMatriz {nomMatrizA}: ")
matrizA = np.array(matrizA) # Convierte la primera matriz a NumPy !!!
print(matrizA)
print(f"Orden de la matriz {nomMatrizA}: {filaA}x{columnaA}")

print(f"\nMatriz {nomMatrizB}: ")
matrizB = np.array(matrizB) # Convierte la primera matriz a NumPy !!!
print(matrizB)
print(f"Orden de la matriz {nomMatrizB}: {filaB}x{columnaB}")

# PARTE 10: MÁS INFORMACIÓN !!!
print("\nAdemás...")
if filaA == filaB and columnaA == columnaB:
    print(f"✔  Las matrices {nomMatrizA} y {nomMatrizB} se pueden sumar.")
else:
    print(f"❌ Las matrices {nomMatrizA} y {nomMatrizB} no se pueden sumar.")

if columnaA == filaB:
    print(f"✔  Las matrices {nomMatrizA} y {nomMatrizB} se pueden multiplicar.\n")
else:
    print(f"❌ Las matrices {nomMatrizA} y {nomMatrizB} no se pueden multiplicar.\n")
pausa()

# ------------------------------ Separador de bajo presupuesto ------------------------------

# PARTE 11: Menú de opciones para las matrices generadas
separador()
while True:
    pantallaMenu2()
    opcion = input("Indique el nro. de la opción que desea realizar: ")
    if opcion.isnumeric():
        opcion = int(opcion)
        if opcion == 1: # Sumar matrices
            if filaA == filaB and columnaA == columnaB:
                suma = matrizA + matrizB
                print(f"\nLa suma de las matrices {nomMatrizA} y {nomMatrizB} es:")
                print(suma)
                pausa()
            else:
                error(f"Recuerda que las matrices {nomMatrizA} y {nomMatrizB} no se pueden sumar !!! (╯‵□′)╯︵┻━┻")
        elif opcion == 2: # Multiplicar matrices
            if columnaA == filaB:
                multi = matrizA.dot(matrizB)
                print(f"\nLa multiplicación de las matrices {nomMatrizA} y {nomMatrizB} es:")
                print(multi)
                pausa()
            else:
                error(f"Recuerda que las matrices {nomMatrizA} y {nomMatrizB} no se pueden multiplicar !!! (╯‵□′)╯︵┻━┻")
        elif opcion == 3: # Transponer una matriz
            print("\n¿Qué matriz desea transponer?\n")
            print(f"1. Matriz {nomMatrizA}")
            print(f"2. Matriz {nomMatrizB}")
            op = input("\nSeleccione el nro. de la opción de la matriz a transponer: ")
            if op == '1':
                matriz = matrizA.T
                print(f"\nLa matriz {nomMatrizA} transpuesta es:")
                print(matriz)
                pausa()
            elif op == '2':
                matriz = matrizB.T
                print(f"\nLa matriz {nomMatrizB} transpuesta es:")
                print(matriz)
                pausa()
            else:
                error("Opción no válida !!! (╯‵□′)╯︵┻━┻")
        elif opcion == 0: # Salir
            print("")
            break
        else:
            error("Opción no válida !!! (╯‵□′)╯︵┻━┻")
    else:
        error("Debe indicar un NÚMERO de opción !!! (╯‵□′)╯︵┻━┻")

# CRÉDITOS:
separador()
print("*** CRÉDITOS ***\n")
print("Código original: Maykol Villena, 28-09-2021. (⌐■_■)")
print("Segunda edición: Francisco González, 29-09-2021. (⌐■_■)")
print("Tercera edición: Francisco González, 01-10-2021. (⌐■_■)")
print("\nTodos los derechos e izquierdos bien puestos. (⌐■_■) (⌐■_■)\n")
separador()
'''