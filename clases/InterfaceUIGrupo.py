from .Grupo import Grupo
from .InterfaceUIAlumno import InterfaceUIAlumno
from.Maestro import Maestro
from .Alumno import Alumno
from .InterfaceUIMaestro import InterfaceUIMaestro
# from db.session import MongoSession

class InterfaceUIGrupo:
    def __init__(self, grupos=None):
        # self.session = MongoSession()
        if grupos:
            self.grupos = grupos
        else:
            self.grupos = Grupo()
            self.grupos.importar("registros/grupos.json")
            self.grupos_offline = Grupo()
            self.grupos_offline.importar("offline/grupos.json")
        self.interfaceMaestro = InterfaceUIMaestro()
    
    def crear(self):
        print("Creando un grupo")
        id_input = input("Ingrese el ID del grupo: ")
        nombre_input = input("Ingrese el nombre del grupo: ")
        grupo = Grupo(id=id_input, Nombre=nombre_input)
        
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
            # ✅ INICIALIZAR correctamente
            grupo.Alumnos = Alumno()
            grupo.Alumnos.es_lista = True
            
            interfaz_alumno = InterfaceUIAlumno(grupo.Alumnos)
            while True:
                alumno = interfaz_alumno.crear()
                
                if alumno:
                    print(f"ALUMNO AGREGADO: {alumno}")
                    # ✅ USAR el método del grupo - automáticamente extrae la calificación
                    grupo.agregar_alumno(alumno)
                    print(f"Calificaciones del grupo {grupo.Nombre}: {grupo.Calificaciones}")
                
                continuar = input("¿Desea agregar otro alumno? (si/no): ")
                if continuar.lower() != "si":
                    break
        else:
            print("No se agregaron Alumnos al grupo")
            grupo.Alumnos = Alumno()
            grupo.Alumnos.es_lista = True
        
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
        nombre = input("Ingrese el Id del grupo: ")
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
                    calificacion = getattr(alumno, 'calificacion', 0)
                    print(f"  {i}. {alumno.nombre} {alumno.apellido} - Calificación: {calificacion}")
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

    def obtener_estadisticas_grupo(self, id):
        """Obtiene todas las estadísticas del grupo usando el método del grupo"""
        grupo = self.grupos.mostrar_uno(id)
        if not grupo:
            print("Grupo no encontrado.")
            return None
            
        estadisticas = grupo.obtener_estadisticas()
        
        if estadisticas:
            print(f"\n📊 ESTADÍSTICAS DEL GRUPO: {grupo.Nombre}")
            print("="*50)
            print(f"Calificaciones: {grupo.Calificaciones}")
            print(f"Total de calificaciones: {estadisticas['total_calificaciones']}")
            print(f"Calificación máxima: {estadisticas['maximo']}")
            print(f"Calificación mínima: {estadisticas['minimo']}")
            print(f"Promedio del grupo: {estadisticas['promedio']:.1f}")
            print(f"Alumnos aprobados (≥70): {estadisticas['aprobados']}")
            print(f"Alumnos reprobados (<70): {estadisticas['reprobados']}")
            
            promedio = estadisticas['promedio']
            debajo_promedio = 0
            sobre_promedio = 0
            
            if grupo.Alumnos and hasattr(grupo.Alumnos, 'lista') and grupo.Alumnos.lista:
                for alumno in grupo.Alumnos.lista:
                    if hasattr(alumno, 'calificacion'):
                        if alumno.calificacion < promedio:
                            debajo_promedio += 1
                        elif alumno.calificacion > promedio:
                            sobre_promedio += 1
            
            print(f"Alumnos debajo del promedio: {debajo_promedio}")
            print(f"Alumnos sobre el promedio: {sobre_promedio}")
            return estadisticas
        else:
            print("No se encontraron calificaciones para el grupo.")
            return None

    def menu(self):
        while True:
            print("\n" + "="*50)
            print("            GESTIÓN DE GRUPOS")
            print("              Sistema 0-100 pts")
            print("            Aprobación mínima: 70")
            print("="*50)
            print("1. Agregar Grupo")
            print("2. Ver estadísticas completas del grupo")
            print("3. Leer Grupo")
            print("4. Editar Grupo")
            print("5. Eliminar Grupo")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear()
            elif opcion == "2":
                id = input("Ingrese el ID del grupo: ")
                self.obtener_estadisticas_grupo(id)
            elif opcion == "3":
                self.leer()
            elif opcion == "4":
                self.editar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    interface = InterfaceUIGrupo()
    interface.menu()