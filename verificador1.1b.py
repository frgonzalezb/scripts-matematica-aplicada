# LÉEME (POR FAVOR):
#
# "VERIFICADOR DE SUCESIONES" (versión 1.1b) para la clase de MATEMÁTICA APLICADA.
#
# Autor original v1.0: Francisco González (alias: Funko de Vision, Esposo de Wanda, etc.)
# v.1.1 hecha en colaboración con mi colega Simón Salinas (alias: 3l_s1m0n). UwU
#
# Todos los derechos e izquierdos bien puestos: Mejore este código según lo estime pertinente,
# favor dando créditos al autor original y colaboradores sucesivos (no sea ingrato). UwU
#
# CHANGELOG (actualice según conveniencia):
# v.1.1b (09-09-2021):
# - Acepta números enteros y decimales.
# - Simplificación de código en la parte 1.
# - Mejoras en el procesamiento de la parte 2.
# - Añadido de etiquetas al código para mejor análisis del mismo.
# - Función RETRY para continuar usando el programa o cerrarlo a voluntad del usuario.
#
# v1.0 (08-09-2021):
# - Programa base creado: Código simple, funcionalidad restringida a sucesiones de números enteros, y sin opción de retry.
#
# Fin del LÉEME.

# PARTE 0: Limpiapantallas para VSC y similares, puede obviarse en IDE webs:
from os import system
system("cls")

# PARTE 1: Ingreso de números con validador
while True:
    while True:
        system("cls")
        print("""Bienvenide al VERIFICADOR DE SUCESIONES !!! (●'◡'●)

INSTRUCCIONES: Ingrese 3 términos sucesivos de una secuencia de números para validar el tipo de sucesión.

POR EJEMPLO: {2, 4, 8} o {1.5, 3.0, 4.5}
        """)
        try:
            n1,n2,n3=[float(input(f"Ingrese el {i}° término de la sucesión: ")) for i in range(1,3+1)]
            break
        except ValueError as e:
            print(f"Error, valores deben ser numéricos. {e}")

# PARTE 2: Comparación de números
    resultados={
    "-":"Sucesión ARITMÉTICA. La DIFERENCIA es: ",
    "/":"Sucesión GEOMÉTRICA. La RAZÓN es: "
}
    for op in resultados.keys():
        var=round(eval(f"{n2} {op} {n1}"),2)
        if var==round(eval(f"{n3} {op} {n2}"),2):
            input(f"{resultados.get(op)} {var}")
            break
        else:
            print("No es una sucesión aritmética ni geométrica")
    # if round(n2-n1,4)==round(n3-n2,4):
    #     print(f"\nLa sucesión es ARITMÉTICA. La diferencia es: {round(n2-n1,4)}")
    #     retry=input("¿Desea volver a usar este programa? S/N: ").upper()
    #     if retry=='N':
    #         break
    # elif round(n2/n1,4)==(n3/n2,4):
    #     print(f"\nLa sucesión es GEOMÉTRICA. La razón es: {round(n2/n1,4)}")
    #     retry=input("¿Desea volver a usar este programa? S/N: ").upper()
    #     if retry=='N':
    #         break
    # else:
    #     print("\nSUCESIÓN NO VÁLIDA !!! (ノಠ益ಠ)ノ彡┻━┻")
    #     retry=input("¿Desea volver a usar este programa? S/N: ").upper()
    #     if retry=='N':
    #         break

# PARTE 3: Cierre y créditos
print("\nGracias por usar este programa. (●'◡'●)")
print("Créditos: Francisco González (autor original) y Simón Salinas (colaborador). UwU")