def cantidadAbejas():
    for t in range(0,120+1):
        At = -9780*t+997560
        if At >= 0:
            print(f"A los {t} meses, había {At} abejas.")
        else:
            print(f"Ya no quedan más abejas. :(")
            break
    print()