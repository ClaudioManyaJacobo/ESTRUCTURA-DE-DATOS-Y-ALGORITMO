from openpyxl import Workbook, load_workbook
import pandas as pd
import os
from Curso import Curso
from Docente import Docente
from Alumno import Alumno
from Curso_Negocio import Curso_negocio

# Crear una instancia de Curso_negocio
negocio_cursos = Curso_negocio()

def registrar_cursos():
    codigo = input("Ingrese el código del curso: ")
    nombre = input("Ingrese el nombre del curso: ")
    nombre_docente = input("Ingrese el nombre del docente del curso: ")
    # Crear una instancia de Curso_negocio
    negocio_cursos = Curso_negocio()
    # Obtener la lista de estudiantes para este curso (hasta un máximo de 5)
    estudiantes = []
    while True:
        if len(estudiantes) < 5:
            nombre_estudiante = input("Ingrese el nombre del estudiante (o 'q' para terminar): ")
            if nombre_estudiante.lower() == 'q':
                break
            estudiantes.append(nombre_estudiante)
        else:
            break
    # Registrar el curso en el negocio de cursos
    negocio_cursos.registrar_curso(codigo, nombre, nombre_docente, estudiantes)
    print("Curso registrado con éxito.")

def mostrar_cursos():
    # Crear una instancia de Curso_negocio
    negocio_cursos = Curso_negocio()
    # Mostrar los cursos
    negocio_cursos.mostrar_cursos()
    
def editar_curso():
        nombre_curso = input("Ingrese el nombre del curso que desea editar: ")

        # Crear una instancia de Curso_negocio
        negocio_cursos = Curso_negocio()

        cursos = negocio_cursos.obtener_cursos()

        curso_a_editar = None

        for curso in cursos:
            if curso.get_nombre() == nombre_curso:
                curso_a_editar = curso
                break

        if curso_a_editar:
            print("Editar curso:")
            nuevo_nombre = input("Nuevo nombre del curso: ")
            nuevo_nombre_docente = input("Nuevo nombre del docente: ")

            # Editar el nombre del curso
            curso_a_editar.set_nombre(nuevo_nombre)

            # Crear una instancia de Docente con el nuevo nombre del docente
            nuevo_docente = Docente(nuevo_nombre_docente, "", "", "", "", "")
            curso_a_editar.asignar_docente(nuevo_docente)

            # Editar la lista de estudiantes (hasta un máximo de 5)
            nueva_lista_estudiantes = []
            while True:
                if len(nueva_lista_estudiantes) < 5:
                    nombre_estudiante = input("Ingrese el nombre del estudiante (o 'q' para terminar): ")
                    if nombre_estudiante.lower() == 'q':
                        break
                    nueva_lista_estudiantes.append(nombre_estudiante)
                else:
                    print("Se han alcanzado el máximo de estudiantes en este curso.")
                    break

            curso_a_editar.estudiantes = nueva_lista_estudiantes

            print("Curso editado con éxito.")
            
            # Guardar los cambios en el archivo XLSX
            negocio_cursos.listado_curso = cursos
            negocio_cursos.guardar_cursos()
        else:
            print(f"No se encontró ningún curso con el nombre '{nombre_curso}' en la lista de cursos.")
def eliminar_curso():
    nombre_curso = input("Ingrese el nombre del curso que desea eliminar: ")
    negocio_cursos.eliminar_curso(nombre_curso)  # Llamamos a la función eliminar_curso

# Diccionario de opciones
opciones_cursos = {
    "1": registrar_cursos,
    "2": mostrar_cursos,
    "3": editar_curso,
    "4": eliminar_curso,
    "5": exit # Para salir 
}

while True:
    print("\n##########################")
    print("Menú (Gestión de Cursos):")
    print("1. Registrar Curso")
    print("2. Listar Cursos")
    print("3. Editar Curso")
    print("4. Eliminar Curso")
    print("5. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones_cursos:
        opciones_cursos[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
