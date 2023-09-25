from openpyxl import Workbook, load_workbook
import pandas as pd
import os
from Curso import Curso
from Docente import Docente
from Alumno import Alumno

class Curso_negocio:
    def __init__(self):
        self.listado_curso = []  # Lista para almacenar objetos Curso
        self.registro_curso = "DatosDeCursos.xlsx"  # Archivo Excel para almacenar datos de cursos
    
    def obtener_cursos(self):
        full_path = os.path.join(os.getcwd(), self.registro_curso)

        if not os.path.isfile(full_path):
            return []

        df = pd.read_excel(full_path)
        listado_curso = []

        for index, row in df.iterrows():
            codigo = row["Código"]
            nombre = row["Nombre"]
            docente_nombre = row["Nombre del Docente"]
            estudiantes = row["Estudiantes"].split(', ') if row["Estudiantes"] else []

            curso = Curso(codigo, nombre)
            
            # Asignar el docente al curso
            docente = Docente(docente_nombre, "", "", "", "", "") # Inializa el objeto docente y solo recupera el nombre
            curso.asignar_docente(docente)

            # Asignar la lista de estudiantes al curso
            curso.estudiantes = estudiantes

            listado_curso.append(curso)

        return listado_curso
    
    def guardar_cursos(self):
        if len(self.listado_curso) > 0:
            data = []
            for curso in self.listado_curso:
                data.append([curso.get_codigo(), curso.get_nombre(), curso.docente_asignado.get_nombre() if curso.docente_asignado else "No asignado", ", ".join(curso.estudiantes)])
            columnas = ["Código", "Nombre", "Nombre del Docente", "Estudiantes"]
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registro_curso, index=False, engine='openpyxl')
            print("Cursos guardados en el archivo", self.registro_curso)
        else:
            print("No hay cursos para guardar.")

    def registrar_curso(self, codigo, nombre, nombre_docente, estudiantes):
        self.listado_curso = self.obtener_cursos()
        curso_existente = next((c for c in self.listado_curso if c.get_codigo() == codigo), None)

        if curso_existente is None:
            # Crear una instancia de Curso
            nuevo_curso = Curso(codigo, nombre)

            # Asignar el docente al curso
            docente = Docente(nombre_docente, "", "", "", "", "")  # Debes modificar esto para crear un docente válido
            nuevo_curso.asignar_docente(docente)

            # Asignar la lista de estudiantes al curso
            nuevo_curso.estudiantes = estudiantes

            self.listado_curso.append(nuevo_curso)
            print(f"Curso {nombre} registrado con éxito.")
            self.guardar_cursos()
        else:
            print(f"El curso con código {codigo} ya existe en el sistema.")
            
    def mostrar_cursos(self):
        cursos = self.obtener_cursos()
        if len(cursos) > 0:
            for curso in cursos:
                print(f"Código: {curso.get_codigo()}")
                print(f"Nombre: {curso.get_nombre()}")
                if curso.docente_asignado:
                    print(f"Docente: {curso.docente_asignado.get_nombre()}")
                else:
                    print("Docente: No asignado")
                if curso.estudiantes:
                    print(f"Estudiantes: {', '.join(curso.estudiantes)}")
                else:
                    print("Estudiantes: No asignados")
                print("\n")
        else:
            print("No hay cursos registrados.")
    
    def eliminar_curso(self, nombre_curso):
        cursos = self.obtener_cursos()

        curso_a_eliminar = None

        for curso in cursos:
            if curso.get_nombre() == nombre_curso:
                curso_a_eliminar = curso
                break

        if curso_a_eliminar:
            cursos.remove(curso_a_eliminar)
            self.listado_curso = cursos
            self.guardar_cursos()
            print(f"El curso '{nombre_curso}' ha sido eliminado.")
            
            # Eliminar al docente asignado
            docente_asignado = curso_a_eliminar.obtener_docente_asignado()
            if docente_asignado:
                curso_a_eliminar.asignar_docente(None)
                print(f"El docente '{docente_asignado.get_nombre()}' también ha sido eliminado.")

            # Eliminar a los estudiantes
            estudiantes = curso_a_eliminar.estudiantes
            if estudiantes:
                curso_a_eliminar.estudiantes = []
                print("Los estudiantes del curso también han sido eliminados.")
        else:
            print(f"No se encontró ningún curso con el nombre '{nombre_curso}' en la lista de cursos.")
