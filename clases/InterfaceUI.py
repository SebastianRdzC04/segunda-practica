from clases.Lista import Lista
import inspect
from db.session import MongoSession

class InterfaceUI:
    def __init__(self):
        self.data = Lista()
        self.session = MongoSession()


    def crear(self):

        atributos = list(inspect.signature(self.data.__class__.__init__).parameters.keys())
        atributos.remove('self')
        print(atributos)
        datos = {}
        for atributo in atributos:
            valor = input(f"Ingresa el {atributo}: ")
            datos[atributo] = valor

        nuevo = self.data.__class__(**datos)
        se_agrego = self.data.agregar(nuevo)
        if not se_agrego:
            print(f"El registro con ID {nuevo.id} ya existe.")
            return None
        else:
            print(f"registro {nuevo.nombre} creado y guardado.")
            self.data.exportar()
            self.session.exportar(self.data.__class__.__name__.lower(), nuevo.convertir_a_diccionario())
            return nuevo

    def leer(self):
        print("Mostrar Datos")
        id = input("Ingresa el ID: ")
        dato = self.data.mostrar_uno(id)
        if dato:
            print(f"ID: {dato.id}, Nombre: {dato.nombre}, Edad: {dato.edad}")
            return dato
        else:
            print(f"No se encontró un dato con ID {id}.")
        return None

    def editar(self):
        print("Editar Datos")
        id = input("Ingresa el ID a editar: ")
        alumno = self.data.mostrar_uno(id)
        if alumno:
            atributos = list(inspect.signature(alumno.__class__.__init__).parameters.keys())
            atributos.remove('self')
            for atributo in atributos:
                valor = input(f"Ingresa el nuevo valor para {atributo} (actual: {getattr(alumno, atributo)}): ")
                if valor:
                    setattr(alumno, atributo, valor)
            se_edito = self.data.editar(id, alumno)
            if se_edito:
                print(f"Dato con ID {id} editado correctamente.")
                self.data.exportar()
                return alumno
            else:
                print(f"No se pudo editar el dato con ID {id}.")
                return None
        else:
            print(f"No se encontró un dato con ID {id}.")
            return None

    def eliminar(self):
        print("Eliminar Datos")
        id = input("Ingresa el ID del dat a eliminar: ")
        se_elimino = self.data.eliminar(id)
        if se_elimino:
            print(f"Dato con ID {id} eliminado correctamente.")
            self.data.exportar()
        else:
            print(f"No se encontró un dato con ID {id} o no se pudo eliminar.")

