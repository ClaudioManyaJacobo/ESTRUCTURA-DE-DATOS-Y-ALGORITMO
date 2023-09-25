from openpyxl import Workbook, load_workbook
import pandas as pd
from openpyxl import Workbook
import os
from Docente_negocio import DocenteNegocio

listado_docente = []
registros_docentes = 'DatosDocentes.xls'

# Crear una instancia de DocenteNegocio
negocio_docente = DocenteNegocio()

def registrar_docentes():
    nombre = input('Ingrese nombre: ')
    ap_paterno = input("Ingrese ap_paterno: ")
    ap_materno = input("Ingrese ap_materno: ")
    dni = input("Ingrese DNI: ")
    codigo = input("Ingrese código: ")
    facultad = input("Ingrese facultad: ")

    negocio_docente.registrar_docente(nombre, ap_paterno, ap_materno, dni, codigo, facultad)
    print(f"Registro correctamente al docente")
    negocio_docente.guardar_docentes()

def obtener_docentes():
    listado_docente = negocio_docente.obtener_docentes()
    for indice, docente in enumerate(listado_docente):
        print(f"Índice: {indice}, {docente.imprimir()}")

def editar_docente():
    obtener_docentes()
    indice = int(input("Ingrese el índice del docente que desea editar: "))
    
    # Obtén la lista de docentes actualizada después de la edición
    listado_docente = negocio_docente.obtener_docentes()
    
    if 0 <= indice < len(listado_docente):
        docente = listado_docente[indice]
        print(f"Editando datos del docente: {docente.imprimir()}")
        
        nombre = input("Ingrese el nuevo nombre: ")
        ap_paterno = input("Ingrese el nuevo apellido paterno: ")
        ap_materno = input("Ingrese el nuevo apellido materno: ")
        dni = input("Ingrese el nuevo DNI: ")
        codigo = input("Ingrese el nuevo código: ")
        facultad = input("Ingrese la nueva facultad: ")
        
        # Llama al método editar_docente en la instancia de DocenteNegocio
        negocio_docente.editar_docente(indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad)
        print("Docente editado correctamente.")
    else:
        print("Índice de docente no válido.")

def eliminar_docente():
    obtener_docentes()
    indice = int(input("Ingrese el índice del docente que desea eliminar: "))
    
    # Llama al método eliminar_docente en la instancia de DocenteNegocio
    mensaje = negocio_docente.eliminar_docente(indice)
    print(mensaje)

# Diccionario de opciones
opciones_docente = {
    "1": registrar_docentes,
    "2": obtener_docentes,
    "3": editar_docente,
    "4": eliminar_docente,
    "5": exit
}

while True:
    print("##########################")
    print("Menú (Gestión de Docentes):")
    print("1. Registrar Docentes")
    print("2. Listar Docentes")
    print("3. Editar Docente")
    print("4. Eliminar Docente")
    print("5. Salir")
    print("##########################")

    seleccion = input("Seleccione una opción: ")

    if seleccion in opciones_docente:
        opciones_docente[seleccion]()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")