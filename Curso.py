# Clase Libre Curso
class Curso:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.docente_asignado = None
        self.estudiantes = []  # Agrega esta línea para crear una lista de estudiantes
        self.notas = [] # Almacenar las notas por cada curso

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_codigo(self):
        return self.codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def calcular_promedio(self, notas):
        if len(notas) > 0:
            return sum(notas) / len(notas)
        else:
            print("El tamaño del arreglo es igual a 0")

    def ingresar_notas(self, nota):
        if len(self.notas) < 80: 
            self.notas.append(nota)
        else:
            print("Se registraron todas las notas")

    def asignar_docente(self, docente):
        self.docente_asignado = docente

    def obtener_docente_asignado(self):
        return self.docente_asignado

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def obtener_promedio(self):
        return self.calcular_promedio(self.notas)
    