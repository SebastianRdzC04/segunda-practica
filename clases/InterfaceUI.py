from .Alumno import Alumno
import inspect

class InerfaceAlumno:
    def __init__(self, alumnos=None):
        if alumnos is None:
            self.data = Alumno()
            self.data.importar("registros/alumnos1.json")
        else:
            self.data = alumnos

    def crear_alumno(self):

        atributos = list(inspect.signature(self.data.__class__.__init__).parameters.keys())
        atributos.remove('self')
        print("Ingresa los datos del nuevo alumno:")
        print(atributos)
        datos = {}
        for atributo in atributos:
            valor = input(f"Ingresa el {atributo} del alumno: ")
            datos[atributo] = valor

        nuevo = self.data.__class__(**datos)
        se_agrego = self.data.agregar(nuevo)
        if not se_agrego:
            print(f"El alumno con ID {nuevo.id} ya existe.")
        else:
            print(f"Alumno {nuevo.nombre} creado y guardado.")








    def menu(self):
        print("1. Crear alumno")
        print("[s] Salir")
        opcion_alumno = input("Selecciona una opción: ").strip().lower()
        while opcion_alumno != "s":
            if opcion_alumno == "1":
                self.crear_alumno()
            else:
                print("Opción no válida. Inténtalo de nuevo.")
            print("1. Crear alumno")
            print("[s] Salir")
            opcion_alumno = input("Selecciona una opción: ").strip().lower()

        print("Saliendo del menú de alumnos.")


if __name__ == "__main__":
    interfaz_alumno = InerfaceAlumno()
    interfaz_alumno.menu()