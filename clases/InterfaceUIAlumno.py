from .Alumno import Alumno
from .InterfaceUI import InterfaceUI


class InterfaceUIAlumno(InterfaceUI):
    def __init__(self, data=None):
        super().__init__()
        if data:
            self.data = data
        else:
            self.data = Alumno()
            self.data.importar("registros/alumnos1.json")

    def menu(self):
        print("INTERFAZ GRAFICA ALUMNO")
        print("1. Agregar Alumno")
        print("2. Leer Alumno")
        print("3. Editar Alumno")
        print("4. Eliminar Alumno")
        print("5. Mostrar Todos los Alumnos")
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

            print("\nINTERFAZ GRAFICA ALUMNO")
            print("1. Agregar Alumno")
            print("2. Leer Alumno")
            print("3. Editar Alumno")
            print("4. Eliminar Alumno")
            print("5. Mostrar Todos los Alumnos")
            print("Para salir, presiona cualquier otra tecla")

            opcion = input("Selecciona una opción: ")



if __name__ == "__main__":
    interface = InterfaceUIAlumno()
    interface.menu()