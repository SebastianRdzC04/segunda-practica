## Siguentes mejoras a realizar:
# 1. No regresar prints. unicamente booleanos pra manejar los resultados
# 2. No agregar una propiedad boleana para saber si la clase es una lista o no
import os
from uuid import UUID

from clases.Alumno import Alumno
from clases.Grupo import Grupo
from clases.Maestro import Maestro
from clases.InterfaceUI import InerfaceAlumno





if __name__ == "__main__":
    alumnos = Alumno()
    grupos = Grupo()
    maestros = Maestro()
    print("INTERFAZ GRAFICA 2")
    print("1. Alumnos")
    print("2. Maestros")
    print("3. Grupos")
    print("para salir presiona cualquier otra tecla")
    opcion = input("Selecciona una opción: ")
    while opcion in ["1", "2", "3"]:
        if opcion == "1":
            if opcion == "1":
                interfaz_alumno = InerfaceAlumno(alumnos)
                interfaz_alumno.menu()

            print("INTERFAZ GRAFICA 2")
            print("1. Alumnos")
            print("2. Maestros")
            print("3. Grupos")
            print("para salir presiona cualquier otra tecla")
            opcion = input("Selecciona una opción: ")









