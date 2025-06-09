from .Lista import Lista

class Maestro(Lista):
    def __init__(self, id=None, nombre=None, apellido=None, edad=None, especialidad=None):
        if nombre and apellido and edad and especialidad and id:
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.especialidad = especialidad
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()


    def __str__(self):
        if hasattr(self, 'nombre'):
            return f"Maestro: {self.nombre} {self.apellido}, Edad: {self.edad}, Especialidad: {self.especialidad}"
        else:
            return "Numero de Maestros " + str(len(self.lista))


if __name__ == "__main__":
    maestro = Maestro(1, "Carlos", "Sánchez", 35, "Matemáticas")
    maestro2 = Maestro(2, "Ana", "Gómez", 30, "Física")
    maestro3 = Maestro(3, "Luis", "Martínez", 40, "Química")
    maestros = Maestro()
    maestros.agregar(maestro)
    maestros.agregar(maestro2)
    maestros.agregar(maestro3)
    maestros.mostrar_uno(3)
    maestros.exportar("registros/maestros.json")