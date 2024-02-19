from abc import ABC, abstractmethod


# Clase abstracta, al crear un modulo debe heredar de este e implemetar sus métodos.
class Modulo(ABC):

    @abstractmethod
    def menu_name(self):
        pass

    @abstractmethod
    def execute(self):
        pass


# Modulos, Aquí se pueden definir para luego ir añadiendo al programa
class VerificarSucesion(Modulo):

    def menu_name(self):
        return "Verificar una Sucesión"

    def execute(self):
        while True:
            print("Bienvenide al VERIFICADOR DE SUCESIONES !!! (●'◡'●)")
            print("Ingrese 3 términos sucesivos de una secuencia de números para validar el tipo de sucesión (aritmética o "
                  "geométrica).")
            print("POR EJEMPLO: {2, 4, 8} o {1.5, 3.0, 4.5}")
            try:
                num1, num2, num3 = [float(input(f"Ingrese el {i}° término de la sucesión: ")) for i in range(1, 3 + 1)]
                break
            except ValueError:
                pass

        resultados = {
            '-': f"\nLa sucesión es ARITMÉTICA.\nLa DIFERENCIA es:",
            '/': f"\nLa sucesión es GEOMÉTRICA.\nLa RAZÓN es:",
        }
        value = -1
        msj = 'La sucesión ingresada NO es aritmética ni geométrica.'
        for op in resultados.keys():
            if round(eval(f'{num2} {op} {num1}'), 2) == round(eval(f'{num3} {op} {num2}'), 2):
                value = round(eval(f'{num2} {op} {num1}'), 2)
                msj = resultados.get(op)
                break
        print(msj, value)


class SucesionAritmetica(Modulo):

    def menu_name(self):
        return "Resolver una Sucesión Aritmética"

    def execute(self):
        while True:
            try:
                a1 = float(input("Indique el número INICIAL (a1) de la sucesión: "))
                d = float(input("Indique la DIFERENCIA (d) de la sucesión: "))
                r1 = int(input("Ingrese un número INICIAL para el rango: "))
                r2 = int(input("Ingrese un número FINAL para el rango: "))
                break
            except ValueError:
                pass
        for n in range(r1, r2 + 1):
            sucesion = a1 + (n - 1) * d
            print(f"El {n}° término es {sucesion}")


class SucesionGeometrica(Modulo):

    def menu_name(self):
        return "Resolver una Sucesión Geométrica"

    def execute(self):
        print("Agregar Implementación....")


class Salir(Modulo):

    def menu_name(self):
        return "Salir"

    def execute(self):
        exit()


class Default(Modulo):

    def menu_name(self):
        return "Default Module"

    def execute(self):
        pass


# Clase principal del programa, se encarga de gestionar los modulos y de generar automáticamente la interfase gráfica del menú
# según modulos agregados
#
class Matematicas:
    def __init__(self):
        self.__modules: dict[str, Modulo] = {}

    def add_module(self, module: Modulo):
        self.__modules[str(len(self.__modules) + 1)] = module

    def execute_module(self, pos_module: str):
        self.__modules.get(pos_module, Default()).execute()

    def show_interfase(self):
        for key, module in self.__modules.items():
            print(f'{int(key)}) {module.menu_name()}')


# PUNTO DE ENTRADA, AQUÍ SE CREAR Y EJECUTA EL PROGRAMA Y SE AÑADEN LOS MÓDULOS
def run():
    # CREACIÓN DEL PROGRAMA
    mate = Matematicas()
    # AGREGAR MODULOS, VAN EN ORDEN
    mate.add_module(VerificarSucesion())
    mate.add_module(SucesionAritmetica())
    mate.add_module(SucesionGeometrica())
    mate.add_module(Salir())
    # LOOP PRINCIAPAL
    while True:
        mate.show_interfase()
        opc = input("Seleccione una opcion: ")
        mate.execute_module(opc)


if __name__ == '__main__':
    run()
