from Persona import Persona # Importar Persona para la clase Alumno
# Clase Alumnos que deriva de la clase Persona
class Alumno(Persona):
    codigo = ''
    facultad = ''
    anio_ingreso = 0

    def __init__(self, nombre, ap_paterno, ap_materno, dni, codigo, facultad, anio_ingreso):
        super().__init__(nombre, ap_paterno, ap_materno, dni)
        self.codigo = codigo
        self.facultad = facultad
        self.anio_ingreso = anio_ingreso
        self.Curso = []

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_facultad(self):
        return self.facultad

    def set_facultad(self, facultad):
        self.facultad = facultad

    def get_anio_ingreso(self):
        return self.anio_ingreso

    def set_anio_ingreso(self, anio):
        self.anio_ingreso = anio

    def imprimir(self):
        per_data = super().imprimir()
        codigo = self.codigo
        facultad = self.facultad
        anio = self.anio_ingreso
        cursos = [curso.get_nombre() for curso in self.Curso]  # Obtener los nombres de los cursos matriculados
        cursos_str = ", ".join(cursos)  # Convertir la lista de cursos a una cadena separada por comas
        return f"""{per_data}, """ \
            f"""Código de ingreso: {codigo}, """ \
            f"""{facultad=}, """ \
            f"""Cursos matriculados: {cursos_str}"""


    def agregar_curso(self, curso): # Agregamos los cursos
        self.Curso.append(curso)

    def remover_curso(self, curso_eliminar): # Quitar los cursos ingresando el codigo 
        for curso in self.Curso:
            if curso_eliminar.get_codigo() == curso.get_codigo():
                self.Curso.remove(curso)
            else:
                print('No se encuentra registrado el curso a eliminar')

        if curso_eliminar in self.Curso:
            self.Curso.remove(curso_eliminar)
    
def agregar_curso(self, codigo, nombre):
    curso = Curso(codigo, nombre)
    self.Curso.append(curso)

