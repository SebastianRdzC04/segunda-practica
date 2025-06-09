from .Grupo import Grupo
from .InterfaceUIAlumno import InterfaceUIAlumno
from.Maestro import Maestro
from .Alumno import Alumno
from .InterfaceUIMaestro import InterfaceUIMaestro


class InterfaceUIGrupo:
    def __init__(self, grupos=None):
        if grupos:
            self.grupos = grupos
        else:
            self.grupos = Grupo()
            self.grupos.importar("registros/grupos.json")
        self.interfaceMaestro = InterfaceUIMaestro()

    def crear(self):
        print("Creando un grupo")
        id_input = input("Ingrese el ID del grupo: ")
        nombre_input = input("Ingrese el nombre del grupo: ")
        grupo = Grupo(id=id_input,Nombre=nombre_input)
        print("Agregar Maestro al grupo")
        input_maestro = input("Si o no? si/no: ")
        if input_maestro.lower() == "si":
            maestro = self.interfaceMaestro.crear()
            grupo.Maestro = maestro
        else:
            print("No se agrego Maestro al grupo")

        print("Agregar Alumnos al grupo")
        input_alumno = input("Si o no? si/no: ")
        if input_alumno.lower() == "si":
            grupo.Alumnos = Alumno()
            interfaz_alumno = InterfaceUIAlumno(grupo.Alumnos)
            while True:
                alumno = interfaz_alumno.crear()
                if alumno:
                    grupo.Alumnos.agregar(alumno)
                continuar = input("¿Desea agregar otro alumno? (si/no): ")
                if continuar.lower() != "si":
                    break
        else:
            print("No se agregaron Alumnos al grupo")
            grupo.Alumnos = Alumno()
        se_agrego = self.grupos.agregar(grupo)
        if not se_agrego:
            print(f"El grupo con nombre {grupo.Nombre} ya existe.")
            return None
        else:
            print(f"Grupo {grupo.Nombre} creado y guardado.")
            self.grupos.exportar()
            return grupo
    def leer(self):
        print("Leer un grupo")
        nombre = input("Ingrese el nombre del grupo: ")
        grupo = self.grupos.mostrar_uno(nombre)
        if grupo:
            print(f"Grupo: {grupo.Nombre} (ID: {grupo.id})")
            
            if grupo.Maestro:
                print(f"Maestro: {grupo.Maestro.nombre} {grupo.Maestro.apellido}")
            else:
                print("No hay maestro asignado")
            
            if grupo.Alumnos and hasattr(grupo.Alumnos, "lista") and grupo.Alumnos.lista:
                print("Alumnos:")
                for i, alumno in enumerate(grupo.Alumnos.lista, 1):
                    print(f"  {i}. {alumno.nombre} {alumno.apellido}")
            else:
                print("No hay alumnos registrados")
                
            return grupo
        else:
            print(f"No se encontró un grupo con nombre {nombre}.")
        return None

    def editar(self):
        print("Editar un grupo")
        id_input = input("Ingrese el nombre del grupo a editar: ")
        grupo = self.grupos.mostrar_uno(id_input)
        if grupo:
            nuevo_nombre = input(f"Nuevo nombre para el grupo (actual: {grupo.Nombre}, deje en blanco para mantener): ")
            if nuevo_nombre:
                grupo.Nombre = nuevo_nombre
            
            print("Editar Maestro del grupo")
            editar_maestro = input("¿Desea editar el maestro? (si/no): ")
            if editar_maestro.lower() == "si":
                maestro = self.interfaceMaestro.editar()
                if maestro:
                    grupo.Maestro = maestro
            
            print("Editar Alumnos del grupo")
            editar_alumnos = input("¿Desea editar los alumnos? (si/no): ")
            if editar_alumnos.lower() == "si":
                # Si no tiene alumnos, inicializamos
                if not grupo.Alumnos:
                    grupo.Alumnos = Alumno()
                
                interfaz_alumno = InterfaceUIAlumno(grupo.Alumnos)
                
                interfaz_alumno.menu()
            
            se_edito = self.grupos.editar(id_input, grupo)
            if se_edito:
                print(f"Grupo con id {id_input} editado correctamente.")
                self.grupos.exportar()
                return grupo
            else:
                print(f"No se pudo editar el grupo con id {id_input}.")
                return None
        else:
            print(f"No se encontró un grupo con id {id_input}.")
            return None
    def eliminar(self):
        print("Eliminar un grupo")
        nombre = input("Ingrese el nombre del grupo a eliminar: ")
        se_elimino = self.grupos.eliminar(nombre)
        if se_elimino:
            print(f"Grupo con nombre {nombre} eliminado correctamente.")
            self.grupos.exportar()
        else:
            print(f"No se encontró un grupo con nombre {nombre} o no se pudo eliminar.")


    def menu(self):
        print("\nInterfaz de Grupos")
        print("1. Agregar Grupo")
        print("2. Leer Grupo")
        print("3. Editar Grupo")
        print("4. Eliminar Grupo")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")
        while opcion != "5":
            if opcion == "1":
                self.crear()
            elif opcion == "2":
                self.leer()
            elif opcion == "3":
                self.editar()
            elif opcion == "4":
                self.eliminar()
            else:
                print("Opción no válida. Intente de nuevo.")

            print("\nInterfaz de Grupos")
            print("1. Agregar Grupo")
            print("2. Leer Grupo")
            print("3. Editar Grupo")
            print("4. Eliminar Grupo")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")
        
        print("¡Hasta pronto!")

if __name__ == "__main__":
    interface = InterfaceUIGrupo()
    interface.menu()