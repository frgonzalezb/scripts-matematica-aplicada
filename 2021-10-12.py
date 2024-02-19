# Clase de FUNCIONES

# Ejemplo caso multitienda:
hora=11
for t in range(0,9+1): # Siempre agregar el +1 en el range para contar el último número
    gt=-16*t**2+160*t+50 # Esta es la función descrita en el problema
    print(f"A las {t} hora(s) desde la apertura (es decir, son las {hora}:00), hay {gt} personas en la multitienda.")
    hora+=1

# P1: Altura de infante de 0 a 12 meses
for x in range(0,12+1):
    fx=2*x/3+48
    print(f"A los {x} meses, el infante tendrá una altura de {round(fx, 2)} cm.")