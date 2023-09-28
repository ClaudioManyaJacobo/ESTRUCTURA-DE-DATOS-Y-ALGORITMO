"""
@Frknk

Clases:
    - Gestor

Atributos:
    - None

Funciones:
    - Gestor() : Constructor de la clase Gestor.
"""
import os
import uuid

import yaml


class Gestor:
    """
    Clase para manejar los identificadores unicos,
    a si mismo como los archivos de datos

    ...

    Atributos
    ---------
    None

    Metodos
    -------
    agregar_data(data_file: str, data: dict)
        Agregar datos a un archivo de datos (Append)
    guardar_data(data_file: str, data: dict)
        Guardar datos en un archivo de datos
    recuperar_data(data_file: str)
        Recuperar datos de un archivo de datos en un diccionario
    generar_id()
        Genera un identificador unico de 6 caracteres alfanumericos usando uuid4.
    crear_id_unica()
        Comprueba la existencia de un id en un archivo de datos. Si ya existe, genera otro id.
        Si no retorna el id generado.
    """

    @classmethod
    def agregar_data(cls, data_file, data) -> bool:
        """
        Agregar datos a un archivo de datos (Append)

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            ejemplo: "data/peliculas_data.yml"
        data : dict
            datos a agregar en el archivo de datos

        Return
        ------
        bool
            True si se agrego correctamente
            False si ocurrio un error
        """

        # Verificar si data_file existe
        if not os.path.exists(os.getcwd() + "/" + data_file):
            print(f"El archivo {data_file} no existe en {os.getcwd()}")
            print(f"Ruta {os.getcwd()}/{data_file}")
            return False

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            print(f"El parametro data no es un diccionario")
            return False

        # Leer archivo de datos
        with open(data_file, "r") as archivo:
            data_old = yaml.load(archivo, Loader=yaml.FullLoader)

        # Verificar si data_old es un diccionario
        if not isinstance(data_old, dict):
            data_old = {}

        # Agregar datos a data_old
        data_old.update(data)

        # Guardar datos en archivo de datos
        with open(data_file, "a") as archivo:
            yaml.dump(data_old, archivo)

        return True

    @classmethod
    def guardar_data(cls, data_file, data) -> bool:
        """
        Sobreescribir datos en un archivo de datos

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            ejemplo: "data/peliculas_data.yml"
        data : dict
            datos a guardar en el archivo de datos

        Return
        ------
        bool
            True si se guardo correctamente
            False si ocurrio un error
        """

        # Verificar si data_file existe
        if not os.path.exists(os.getcwd() + "/" + data_file):
            print(f"El archivo {data_file} no existe en {os.getcwd()}")
            print(f"Ruta {os.getcwd()}/{data_file}")
            return False

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            print(f"El parametro data no es un diccionario")
            return False

        # Guardar datos en archivo de datos
        with open(data_file, "w") as archivo:
            # Sobre escribir datos en archivo de datos
            yaml.dump(data, archivo)

        return True


    @classmethod
    def recuperar_data(cls, data_file) -> dict:
        """
        Recuperar datos de un archivo de datos
        en un diccionario

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            ejemplo: "data/peliculas_data.yml"

        Return
        ------
        data : dict
            datos recuperados del archivo de datos
        """

        # Verificar si data_file existe
        if not os.path.exists(os.getcwd() + "/" + data_file):
            print(f"El archivo {data_file} no existe en {os.getcwd()}")
            print(f"Ruta {os.getcwd()}/{data_file}")
            return {}

        # Leer archivo de datos
        with open(data_file, "r") as archivo:
            data = yaml.load(archivo, Loader=yaml.FullLoader)

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            data = {}

        return data

    @staticmethod
    def generar_id() -> str:
        """
        Genera un identificador unico de 6 caracteres alfanumericos usando uuid4.
        Preferible si no quieres guardar el id en un archivo de datos.

        Parametros
        ----------
        None

        Return
        ------
        str
            id generado
        """
        return str(uuid.uuid4().int)[:6]

    @classmethod
    def crear_id_unica(cls, data_file) -> str:
        """
        Checar si el id ya existe en un archivo de datos
        Si existe, crear otro
        Si no existe, retornar el id

        Parametros
        ----------
        data_file : str
            ruta del archivo de datos
            ejemplo: "data/peliculas_data.yml"

        Return
        ------
        id_gen : str
            id generado - En caso de fallo retorna "NULL ID"
        """

        # Verificar si data_file existe
        if not os.path.exists(os.getcwd() + "/" + data_file):  # Obtener directorio actual
            print(f"El archivo {data_file} no existe en {os.getcwd()}")
            print(f"Ruta {os.getcwd()}/{data_file}")
            return "NULL ID"
        else:
            with open(data_file, "r") as archivo:
                data = yaml.load(archivo, Loader=yaml.FullLoader)

        # Verificar si data es un diccionario
        if not isinstance(data, dict):
            data = {}

        # Loop para generar id unica
        try:
            while True:
                # Generar id
                id_gen = cls.generar_id()
                # Verificar si id_gen ya existe en data
                if id_gen not in data:
                    return id_gen
        except Exception as e:
            print(f"A ocurrido un error al generar la id: {e}")
