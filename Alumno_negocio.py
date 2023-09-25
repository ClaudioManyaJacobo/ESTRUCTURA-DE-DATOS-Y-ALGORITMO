from openpyxl import Workbook
from Alumno import Alumno  
from datetime import datetime
import os
import pandas as pd

class AlumnoNegocio:
    def __init__(self):
        self.listado_alumno = []  # Lista para almacenar objetos Alumno
        self.registros_alumnos = "DatosAlumnos.xlsx"  # Archivo Excel para almacenar datos de estudiantes

    def obtener_alumnos(self):
        # Construye la ruta completa al archivo Excel
        full_path = os.path.join(os.getcwd(), self.registros_alumnos)
        
        # Verifica si el archivo existe
        if not os.path.isfile(full_path):
            return []  # Devuelve una lista vacía si el archivo no existe
        
        # Lee el archivo Excel utilizando pandas
        df = pd.read_excel(full_path)
        listado_alumno = []
        
        # Itera a través de las filas y crea objetos Alumno
        for index, row in df.iterrows():
            alumno = Alumno(row["Nombre"], row["Apellido_Paterno"], row["Apellido_Materno"], row["DNI"], row["Codigo"], row["Facultad"], row["Año"])
            listado_alumno.append(alumno)
        
        return listado_alumno  # Devuelve una lista de objetos Alumno

    def registrar_alumno(self, _nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad, _anio):
        self.listado_alumno = self.obtener_alumnos()  # Carga los estudiantes existentes desde el archivo
        alumno = Alumno(_nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad, _anio)
        self.listado_alumno.append(alumno)  # Agrega el nuevo estudiante a la lista

    def guardar_alumnos(self):
        if len(self.listado_alumno) > 0:
            data = []
            for alumno in self.listado_alumno:
                data.append([alumno.nombre, alumno.ap_paterno, alumno.ap_materno, alumno.dni, alumno.codigo, alumno.facultad, alumno.anio_ingreso])
            columnas = ["Nombre", "Apellido_Paterno", "Apellido_Materno", "DNI", "Codigo", "Facultad", "Año"]
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_alumnos, index=False, engine="openpyxl")  # Guarda los datos de los estudiantes en el archivo Excel
            return "Se registraron los datos del alumno correctamente."
        else:
            return "No se registraron datos de alumnos."

    def editar_alumno(self, indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad, anio):
        self.listado_alumno = self.obtener_alumnos()  # Carga los estudiantes existentes desde el archivo
        
        if indice < len(self.listado_alumno):
            alumno = self.listado_alumno[indice]
            
            # Actualiza los atributos del estudiante
            alumno.set_nombre(nombre)
            alumno.set_ap_paterno(ap_paterno)
            alumno.set_ap_materno(ap_materno)
            alumno.set_dni(dni)
            alumno.set_codigo(codigo)
            alumno.set_facultad(facultad)
            alumno.set_anio_ingreso(anio)
            
            # Guarda los cambios en el archivo Excel
            self.guardar_alumnos()
            
            return "Alumno editado correctamente."
        else:
            return "Índice de alumno no válido."

    def eliminar_alumno(self, indice):
        self.listado_alumno = self.obtener_alumnos()  # Carga los estudiantes existentes desde el archivo
        
        if 0 <= indice < len(self.listado_alumno):
            self.listado_alumno.pop(indice)  # Elimina al estudiante en el índice especificado
            self.guardar_alumnos()  # Guarda los cambios en el archivo Excel
            return "Alumno eliminado correctamente."
        else:
            return "Índice de alumno no válido."
