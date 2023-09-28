"""
@Frknk

Clases:
    - Cliente

Atributos:
    None

Funciones:
    - Cliente() : Constructor de la clase Cliente.
"""

from persona import Persona
from gestor import Gestor


class Cliente(Persona):
    """
    Clase para manejar los clientes

    ...

    Atributos
    ---------
    id : str
        id del cliente
    password : str
        password del cliente
    peliculas_alquiladas : list
        lista de peliculas alquiladas por el cliente


    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: str,
        direccion: str,
        telefono: str,
        email: str,
        password: str,
    ):
        """
        Constructor de la clase Cliente

        Parametros
        ----------
        nombre : str
            nombre del cliente
        apellido : str
            apellido del cliente
        dni : str
            dni del cliente
        direccion : str
            direccion del cliente
        telefono : str
            telefono del cliente
        email : str
            email del cliente
        password : str
            password del cliente
        """
        super().__init__(nombre, apellido, dni, direccion, telefono, email)
        self.id = Gestor.crear_id_unica("data/clientes_data.yml")
        self.password = password
        self.peliculas_alquiladas = []

    def agregar_pelicula_alquilada(self, pelicula_id: str) -> None:
        """
        Agregar una pelicula a la lista de peliculas alquiladas

        Parametros
        ----------
        pelicula_id : str
            id de la pelicula a agregar
        """
        self.peliculas_alquiladas.append(pelicula_id)

    def getid(self) -> str:
        """
        Obtener el id del cliente

        Return
        ------
        str
            id del cliente
        """
        return self.id

    def setid(self, id: str) -> None:
        """
        Asignar un id al cliente
        """
        self.id = id

    def getpassword(self) -> str:
        """
        Obtener el password del cliente

        Return
        ------
        str
            password del cliente
        """
        return self.password

    def getpelisalquiladas(self) -> list:
        """
        Obtener la lista de peliculas alquiladas por el cliente

        Return
        ------
        list
            lista de peliculas alquiladas por el cliente
        """
        return self.peliculas_alquiladas

    def setpassword(self, password: str) -> None:
        """
        Asignar un password al cliente

        Parametros
        ----------
        password : str
            password del cliente
        """
        self.password = password

    def getclientedatasimple(self) -> dict:
        """
        Obtener los datos del cliente en un diccionario

        Return
        ------
        dict
            datos del cliente en un diccionario
        """
        cliente_info = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "password": self.password,
        }
        return cliente_info

    def getclientedata(self) -> dict:
        """
        Obtener los datos del cliente en un diccionario

        Return
        ------
        dict
            datos del cliente en un diccionario
        """
    
        cliente_info = {
                "nombre": self.nombre,
                "apellido": self.apellido,
                "dni": self.dni,
                "direccion": self.direccion,
                "telefono": self.telefono,
                "email": self.email,
                "password": self.password,
                "peliculas_alquiladas": self.peliculas_alquiladas,
            }
        return {self.id: cliente_info}
