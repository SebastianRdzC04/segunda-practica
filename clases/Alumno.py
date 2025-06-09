from .Lista import Lista

class Alumno(Lista):
    def __init__(self,id = None, nombre=None, apellido=None, edad=None, matricula=None):

        if nombre is not None and apellido is not None and edad is not None and matricula is not None and id is not None:
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.matricula = matricula
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()

    def __str__(self):
        if hasattr(self, 'nombre'):
            return f"Alumno: {self.nombre} {self.apellido}, Edad: {self.edad}, Matrícula: {self.matricula}"
        else:
            return "Numero de Alumnos " + str(len(self.lista))

if __name__ == "__main__":
    """
    alumno = Alumno(1,"Juan", "Pérez", 20, "123456")
    alumno2 = Alumno(2,"Ana", "Gómez", 22, "654321")
    alumno3 = Alumno(3,"Luis", "Martínez", 21, "789012")
    """
    alumnos = Alumno()
    """
    alumnos.agregar(alumno)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno3)
    alumno.mostrar()
    alumnos.mostrar()
    alumnos.mostrar_uno(3)
    alumno.exportar("registros/alumno1.json")
    alumnos.exportar("registros/alumnos1.json")
    nuevo_alumno = Alumno(4, "Maria", "Lopez", 19, "345678")
    print("el nuevo alumno es")
    nuevo_alumno.importar("registros/alumno1.json")
    print(nuevo_alumno)
    """
    nuevos_alumnos = Alumno()
    nuevos_alumnos.importar("registros/alumnos1.json")
    print("los nuevos alunos son")
    nuevos_alumnos.mostrar()
    alumno = Alumno(1,"Juan", "Pérez", 20, "123456")
    nuevos_alumnos.agregar(alumno)
    nuevos_alumnos.exportar("registros/alumnos2.json")



