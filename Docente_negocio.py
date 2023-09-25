from openpyxl import Workbook
from Docente import Docente
from datetime import datetime
import os
import pandas as pd

class DocenteNegocio:
    def __init__(self):
        self.listado_docente = []  # Lista para almacenar objetos Docente
        self.registros_docentes = "DatosDocentes.xlsx"  # Archivo Excel para almacenar datos de docentes
        
    def obtener_docentes(self):
        full_path = os.path.join(os.getcwd(), self.registros_docentes)
        
        if not os.path.isfile(full_path):
            return []  # Devolver una lista vacía si el archivo no existe
        
        df = pd.read_excel(full_path)
        listado_docente = []
        
        for index, row in df.iterrows():
            docente = Docente(row["Nombre"], row["Apellido_Paterno"], row["Apellido_Materno"], row["DNI"], row["Codigo"], row["Facultad"])
            listado_docente.append(docente)
        
        return listado_docente  # Devuelve una lista de objetos Docente

    def registrar_docente(self, _nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad):
        self.listado_docente = self.obtener_docentes()  # Carga los docentes existentes desde el archivo
        docente = Docente(_nombre, _apellido_paterno, _apellido_materno, _dni, _codigo, _facultad)
        self.listado_docente.append(docente)  # Agrega el nuevo docente a la lista

    def guardar_docentes(self):
        if len(self.listado_docente) > 0:
            data = []
            for docente in self.listado_docente:
                data.append([docente.nombre, docente.ap_paterno, docente.ap_materno, docente.dni, docente.codigo_docente, docente.facultad])
            columnas = ["Nombre", "Apellido_Paterno", "Apellido_Materno", "DNI", "Codigo", "Facultad"]
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(self.registros_docentes, index=False, engine="openpyxl")  # Guarda los datos de los docentes en el archivo Excel
            return "Se registraron los datos del docente correctamente."
        else:
            return "No se registraron datos de docentes."

    def editar_docente(self, indice, nombre, ap_paterno, ap_materno, dni, codigo, facultad):
        self.listado_docente = self.obtener_docentes()  # Carga los docentes existentes desde el archivo
        
        if indice < len(self.listado_docente):
            docente = self.listado_docente[indice]
            
            # Actualiza los atributos del docente
            docente.set_nombre(nombre)
            docente.set_ap_paterno(ap_paterno)
            docente.set_ap_materno(ap_materno)
            docente.set_dni(dni)
            docente.set_codigo(codigo)
            docente.set_facultad(facultad)
            
            # Guarda los cambios en el archivo Excel
            self.guardar_docentes()
            
            return "Docente editado correctamente."
        else:
            return "Índice de docente no válido."
        
    def eliminar_docente(self, indice):
        self.listado_docente = self.obtener_docentes()  # Carga los docentes existentes desde el archivo
        
        if 0 <= indice < len(self.listado_docente):
            del self.listado_docente[indice]
            self.guardar_docentes()
            return "Docente eliminado correctamente."
        else:
            return "Índice de docente no válido."
