# VERIFICADOR DE SUCESIONES para MATEMÁTICA APLICADA, versión 1.0
# Autor original: Francisco González (aka: Funko de Vision, Esposo de Wanda, etc.)
# Todos los derechos e izquierdos bien puestos: Mejore este código según lo estime pertinente,
# dando créditos al autor original y editores sucesivos. UwU

from os import system
system("cls")

while True:
    while True:
        system("cls")
        print("""Bienvenide al VERIFICADOR DE SUCESIONES !!! (●'◡'●)

INSTRUCCIONES: Sólo usar números enteros.
        """)
        n1=input("Inserte el 1° término: ")
        if n1.isnumeric():
            n1=int(n1)
            n2=input("Inserte el 2° término: ")
            if n2.isnumeric():
                n2=int(n2)
                n3=input("Inserte el 3° término: ")
                if n3.isnumeric():
                    n3=int(n3)
                    break
                else:
                    print("Debe ser un NÚMERO ENTERO. (╯°□°）╯︵ ┻━┻")
            else:
                print("Debe ser un NÚMERO ENTERO. (╯°□°）╯︵ ┻━┻")
        else:
            print("Debe ser un NÚMERO ENTERO. (╯°□°）╯︵ ┻━┻")

    if n2-n1==n3-n2:
        print(f"La sucesión es ARITMÉTICA. La diferencia es: {n2-n1}")
        input("Presione ENTER para terminar...")
        break
    elif n2/n1==n3/n2:
        print(f"La sucesión es GEOMÉTRICA. La razón es: {n2/n1}")
        input("Presione ENTER para terminar...")
        break
    else:
        print("SUCESIÓN NO VÁLIDA !!! (ノಠ益ಠ)ノ彡┻━┻")
        input("Presione ENTER para terminar...")
        break