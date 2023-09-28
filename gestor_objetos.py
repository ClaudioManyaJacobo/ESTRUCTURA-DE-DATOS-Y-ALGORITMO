from cliente import Cliente
from gestor import Gestor
from pelicula import Pelicula
from datetime import datetime

class GestorObjetos:
    """
    Clase que se encarga de gestionar la recuperación de objetos Pelicula y Cliente
    a partir de un archivo de datos.

    Métodos
    -------
    recuperar_pelicula(pelicula_id: str, data_file: str) -> Pelicula:
        Recupera una película a partir de su id y el archivo de datos.

    recuperar_cliente(cliente_id: str, data_file: str) -> Cliente:
        Recupera un cliente a partir de su id y el archivo de datos.

    registro(tipo: str, cliente_id: str, pelicula_id: str, data_file: str) -> None:
        Registra un diccionario de tipo registro en un archivo de datos.
    """

    @classmethod
    def registro(cls, tipo: str, cliente_id: str, pelicula_id: str, data_file: str):
        """
        Registra un diccionario de tipo registro en un archivo de datos.

        Parametros
        ----------
        tipo : str
            tipo de registro
        cliente_id : str
            id del cliente
        pelicula_id : str
            id de la pelicula
        data_file : str
            ruta del archivo de datos
        
        Return
        ------
        None
        """

        dict = {
            "tipo": tipo,
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "hora": datetime.now().strftime("%H:%M:%S"),
            "cliente_id": cliente_id,
            "pelicula_id": pelicula_id,
        }

        Gestor.agregar_data(data_file, dict)

    @classmethod
    def recuperar_pelicula(cls, pelicula_id: str, data_file : str):
        """
        Recuperar un cliente en una clase Cliente

        Parametros
        ----------
        cliente_id : str
            id del cliente a recuperar

        Return
        ------
        cliente : Cliente
            cliente recuperado
        """

        # Recuperar data en diccionario
        data = Gestor.recuperar_data(data_file)

        # Verificar si cliente_id existe en data
        if pelicula_id not in data:
            return None

        # Recuperar datos del cliente
        pelicula_data = data[pelicula_id]

        # Crear pelicula
        """"nombre": self.nombre,
            "genero": self.genero,
            "duracion": self.duracion,
            "clasificacion": self.clasificacion,
            "idioma": self.idioma,
            "subtitulos": self.subtitulos,
            "sinopsis": self.sinopsis,
            "director": self.director,
            "actores": self.actores,
            "productora": self.productora,
            "pais": self.pais,
            "fecha": self.fecha,
            "precio": self.precio,
            "disponible": self.disponible"""
        pelicula = Pelicula(
            pelicula_data["nombre"],
            pelicula_data["genero"],
            pelicula_data["duracion"],
            pelicula_data["clasificacion"],
            pelicula_data["idioma"],
            pelicula_data["subtitulos"],
            pelicula_data["sinopsis"],
            pelicula_data["director"],
            pelicula_data["actores"],
            pelicula_data["productora"],
            pelicula_data["pais"],
            pelicula_data["fecha"],
            pelicula_data["precio"],
            pelicula_data["disponible"],
        )

        pelicula.setid(pelicula_id)

        return pelicula

    @classmethod
    def recuperar_cliente(cls, cliente_id: str, data_file : str):
        """
        Recuperar un cliente en una clase Cliente

        Parametros
        ----------
        cliente_id : str
            id del cliente a recuperar

        Return
        ------
        cliente : Cliente
            cliente recuperado
        """

        # Recuperar data en diccionario
        data = Gestor.recuperar_data(data_file)

        # Verificar si cliente_id existe en data
        if cliente_id not in data:
            return None

        # Recuperar datos del cliente
        cliente_data = data[cliente_id]

        # Crear cliente
        cliente = Cliente(
            cliente_data["nombre"],
            cliente_data["apellido"],
            cliente_data["dni"],
            cliente_data["direccion"],
            cliente_data["telefono"],
            cliente_data["email"],
            cliente_data["password"],
        )

        for pelicula in cliente_data["peliculas_alquiladas"]:
            cliente.agregar_pelicula_alquilada(pelicula)

        cliente.setid(cliente_id)

        return cliente
