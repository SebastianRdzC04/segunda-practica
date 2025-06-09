from .Lista import Lista
from .Alumno import Alumno
from .Maestro import Maestro

class Grupo(Lista):
    def __init__(self,id=None, Nombre = None, Maestro = None, Alumnos=None):
        if Nombre and id:
            self.id = id
            self.Nombre = Nombre
            self.Maestro = Maestro
            self.Alumnos = Alumnos
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()

    def __str__(self):
        if hasattr(self, 'Nombre'):
            return f"(Grupo: {self.Nombre}), (Maestro: {self.Maestro}), (Alumnos: {self.Alumnos})"
        else:
            return "Numero de Grupos " + str(len(self.lista))

    def convertir_json_objeto(self, data):
        if self.es_lista:
            self.lista = []
            for item in data:
                nuevo_grupo = Grupo()
                nuevo_grupo.es_lista = False
                nuevo_grupo = nuevo_grupo.convertir_json_objeto(item)
                self.lista.append(nuevo_grupo)
            return self
        else:
            # Asegurar que tenemos todas las propiedades necesarias
            self.id = data.get('id')
            self.Nombre = data.get('Nombre')

            # Configurar el maestro
            maestro_dict = data.get('Maestro', {})
            self.Maestro = Maestro()
            self.Maestro.es_lista = False
            self.Maestro.convertir_json_objeto(maestro_dict)

            # Configurar los alumnos
            alumnos_data = data.get('Alumnos', [])
            self.Alumnos = Alumno()
            self.Alumnos.es_lista = True
            self.Alumnos.convertir_json_objeto(alumnos_data)
            
            return self

    def convertir_a_diccionario(self):
        if self.lista:
            grupos_diccionario = []
            for item in self.lista:
                grupos_diccionario.append(item.convertir_a_diccionario())
            return grupos_diccionario

        else:
            alumnos_diccionario = []
            if self.Alumnos is not None:
                alumnos_diccionario = self.Alumnos.convertir_a_diccionario()

            maestro_diccionario = {}
            if self.Maestro is not None:
                maestro_diccionario = self.Maestro.convertir_a_diccionario()

            return {
                "id": self.id,
                "Nombre": self.Nombre,
                "Maestro": maestro_diccionario,
                "Alumnos": alumnos_diccionario
            }



if __name__ == "__main__":
    # Crear 10 alumnos
    alumno1 = Alumno("1", "Juan", "Pérez", "20", "A12345")
    alumno2 = Alumno("2", "María", "González", "21", "A12346")
    alumno3 = Alumno("3", "Carlos", "Rodríguez", "19", "A12347")
    alumno4 = Alumno("4", "Ana", "Martínez", "22", "A12348")
    alumno5 = Alumno("5", "Luis", "Sánchez", "20", "A12349")
    alumno6 = Alumno("6", "Laura", "Díaz", "21", "A12350")
    alumno7 = Alumno("7", "Pedro", "Ramírez", "19", "A12351")
    alumno8 = Alumno("8", "Sofía", "Torres", "22", "A12352")
    alumno9 = Alumno("9", "Miguel", "Fernández", "20", "A12353")
    alumno10 = Alumno("10", "Carmen", "López", "21", "A12354")
    
    # Crear 5 profesores
    maestro1 = Maestro("1", "Roberto", "Gómez", "45", "Matemáticas")
    maestro2 = Maestro("2", "Elena", "Vázquez", "38", "Física")
    maestro3 = Maestro("3", "Jorge", "Hernández", "42", "Programación")
    maestro4 = Maestro("4", "Lucía", "Morales", "39", "Base de Datos")
    maestro5 = Maestro("5", "Javier", "Castro", "47", "Redes")
    
    # Crear grupos y asignar alumnos a cada grupo
    # Grupo 1
    alumnos_grupo1 = Alumno()
    alumnos_grupo1.agregar(alumno1)
    alumnos_grupo1.agregar(alumno2)
    grupo1 = Grupo("1", "Grupo A", maestro1, alumnos_grupo1)
    
    # Grupo 2
    alumnos_grupo2 = Alumno()
    alumnos_grupo2.agregar(alumno3)
    alumnos_grupo2.agregar(alumno4)
    grupo2 = Grupo("2", "Grupo B", maestro2, alumnos_grupo2)
    
    # Grupo 3
    alumnos_grupo3 = Alumno()
    alumnos_grupo3.agregar(alumno5)
    alumnos_grupo3.agregar(alumno6)
    grupo3 = Grupo("3", "Grupo C", maestro3, alumnos_grupo3)
    
    # Grupo 4
    alumnos_grupo4 = Alumno()
    alumnos_grupo4.agregar(alumno7)
    alumnos_grupo4.agregar(alumno8)
    grupo4 = Grupo("4", "Grupo D", maestro4, alumnos_grupo4)
    
    # Grupo 5
    alumnos_grupo5 = Alumno()
    alumnos_grupo5.agregar(alumno9)
    alumnos_grupo5.agregar(alumno10)
    grupo5 = Grupo("5", "Grupo E", maestro5, alumnos_grupo5)
    
    # Crear lista de grupos
    grupos = Grupo()
    grupos.agregar(grupo1)
    grupos.agregar(grupo2)
    grupos.agregar(grupo3)
    grupos.agregar(grupo4)
    grupos.agregar(grupo5)
    
    print("Grupos creados:")
    grupos.mostrar()
    
    # Exportar la lista de grupos a JSON
    grupos.exportar("registros/grupos.json")
    grupos2 = Grupo()
    grupos2.importar("registros/grupos.json")
    print("Grupos importados desde registros/grupos.json:")
    grupos2.mostrar()
    grupos2.exportar("registros/grupos2.json")
    print("Grupos exportados a registros/grupos.json")