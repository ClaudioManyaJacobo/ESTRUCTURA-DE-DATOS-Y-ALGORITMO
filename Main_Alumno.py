from openpyxl import Workbook, load_workbook
import pandas as pd
from openpyxl import Workbook
import os
from Alumno_negocio import AlumnoNegocio

# Crear una lista para almacenar objetos Alumno
listado_alumno = []

# Nombre del archivo Excel para almacenar los datos de los alumnos
registros_alumnos = 'DatosAlumnos.xls'

# Crear una instancia de AlumnoNegocio
negocio = AlumnoNegocio()

def registrar_alumnos():
    # Solicitar información del alumno al usuario
    nombre = input('Ingrese nombre: ')
    ap_paterno = input('Ingrese ap_paterno: ')
    ap_materno = input('Ingrese ap_materno: ')
    dni = input('Ingrese DNI: ')
    codigo = input('Ingrese código: ')
    facultad = input('Ingrese facultad: ')

    # Validar la entrada para el año de ingreso
    while True:
        anio_ingreso_str = input('Ingrese año de ingreso (como número): ')
        if anio_ingreso_str.isdigit():
            anio_ingreso = int(anio_ingreso_str)
            break
        else:
            print("Por favor, ingrese un año válido como número.")

    # Registrar al alumno
    negocio.registrar_alumno(nombre, ap_paterno, ap_materno, dni, codigo, facultad, anio_ingreso)
    print(f'Alumno registrado correctamente.')
    negocio.guardar_alumnos()

def obtener_alumnos():
    # Obtener la lista de alumnos
    listado_alumno = negocio.obtener_alumnos()

    # Mostrar la lista de alumnos
    for indice, alumno in enumerate(listado_alumno):
        print(f"Índice: {indice}, {alumno.imprimir()}")

def editar_alumno():
    obtener_alumnos()
    indice = int(input('Ingrese el índice del alumno que desea editar: '))
    
    # Obtener la lista de alumnos actualizada después de la edición
    listado_alumno = negocio.obtener_alumnos()
    
    if 0 <= indice < len(listado_alumno):
        alumno = listado_alumno[indice]
        print(f'Editando datos del alumno: {alumno.imprimir()}')
        
        # Solicitar y validar la información actualizada del alumno
        nombre = input('Ingrese el nuevo nombre: ')
        ap_paterno = input('Ingrese el nuevo apellido paterno: ')
        ap_materno = input('Ingrese el nuevo apellido materno: ')
        dni = input('Ingrese el nuevo DNI: ')
        codigo = input('Ingrese el nuevo código: ')
        facultad = input('Ingrese la nueva facultad: ')
        
        # Validar la entrada para el año de ingreso
        while True:
            anio_ingreso_str = input('Ingrese el nuevo año de ingreso (como número): ')
            if anio_ingreso_str.isdigit():
                anio_ingreso = int(anio_ingreso_str)
                break
            else:
                print("Por favor, ingrese un año válido como número.")
        
        # Editar al alumno
        negocio.editar_alumno(indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad, anio_ingreso)
        print('Alumno editado correctamente.')
    else:
        print('Índice de alumno no válido.')

def eliminar_alumno():
    obtener_alumnos()
    indice = int(input("Ingrese el índice del alumno que desea eliminar: "))
    
    # Eliminar al alumno
    resultado = negocio.eliminar_alumno(indice)
    print(resultado)

# Diccionario de opciones
opciones = {
    "1": registrar_alumnos,
    "2": obtener_alumnos,
    "3": editar_alumno,
    "4": eliminar_alumno,
    "5": exit
}

while True:
    print("##########################")
    print("Menú (Gestión de Alumnos):")
    print("1. Registrar Alumnos")
    print("2. Listar Alumnos")
    print("3. Editar Alumno")
    print("4. Eliminar Alumno")
    print("5. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones:
        opciones[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
