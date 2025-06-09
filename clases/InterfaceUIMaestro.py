from .Maestro import Maestro
from .InterfaceUI import InterfaceUI

class InterfaceUIMaestro(InterfaceUI):
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.data = data
        else:
            self.data = Maestro()
            self.data.importar("registros/maestros.json")

    def menu(self):
        print("INTERFAZ GRAFICA MAESTRO")
        print("1. Agregar Maestro")
        print("2. Leer Maestro")
        print("3. Editar Maestro")
        print("4. Eliminar Maestro")
        print("5. Mostrar Todos los Maestros")
        print("Para salir, presiona cualquier otra tecla")

        opcion = input("Selecciona una opción: ")
        while opcion in ["1", "2", "3", "4", "5"]:
            if opcion == "1":
                self.crear()
            elif opcion == "2":
                self.leer()
            elif opcion == "3":
                self.editar()
            elif opcion == "4":
                self.eliminar()
            elif opcion == "5":
                self.data.mostrar()

            print("\nINTERFAZ GRAFICA MAESTRO")
            print("1. Agregar Maestro")
            print("2. Leer Maestro")
            print("3. Editar Maestro")
            print("4. Eliminar Maestro")
            print("5. Mostrar Todos los Maestros")
            print("Para salir, presiona cualquier otra tecla")

            opcion = input("Selecciona una opción: ")



if __name__ == "__main__":
    maestro = Maestro()
    interface = InterfaceUIMaestro(maestro)
    interface.menu()