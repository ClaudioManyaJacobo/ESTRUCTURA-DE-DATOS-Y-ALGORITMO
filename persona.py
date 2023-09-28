"""
@Frknk

Clases:
    - Persona

Atributos:
    None

Funciones:
    - Persona() : Constructor de la clase Persona.
"""


class Persona:
    """
    Clase para manejar los datos de una persona

    ...

    Atributos
    ---------
    nombre : str
        Nombre de la persona
    apellido : str
        Apellido de la persona
    dni : str
        Dni de la persona
    direccion : str
        Direccion de la persona
    telefono : str
        Telefono de la persona
    email : str
        Email de la persona

    Metodos
    -------
    getnombre()
        Obtener el nombre de la persona
    getapellido()
        Obtener el apellido de la persona
    getdni()
        Obtener el dni de la persona
    getdireccion()
        Obtener la direccion de la persona
    gettelefono()
        Obtener el telefono de la persona
    getemail()
        Obtener el email de la persona
    setnombre(nombre: str)
        Asignar un nombre a la persona
    setapellido(apellido: str)
        Asignar un apellido a la persona
    setdni(dni: str)
        Asignar un dni a la persona
    setdireccion(direccion: str)
        Asignar una direccion a la persona
    settelefono(telefono: str)
        Asignar un telefono a la persona
    setemail(email: str)
        Asignar un email a la persona
    getdata()
        Obtener los datos de la persona en un diccionario
    getdata_str()
        Obtener los datos de la persona en un string
    """

    def __init__(
        self,
        nombre: str,
        apellido: str,
        dni: str,
        direccion: str,
        telefono: str,
        email: str,
    ):
        """
        Constructor de la clase Persona

        Parametros
        ----------
        nombre : str
            nombre de la persona
        apellido : str
            apellido de la persona
        dni : str
            dni de la persona
        direccion : str
            direccion de la persona
        telefono : str
            telefono de la persona
        email : str
            email de la persona
        """
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    def getnombre(self) -> str:
        """
        Obtener el nombre de la persona

        Return
        ------
        str
            Nombre de la persona
        """
        return self.nombre

    def getapellido(self) -> str:
        """
        Obtener el apellido de la persona

        Return
        ------
        str
            Apellido de la persona
        """
        return self.apellido

    def getdni(self) -> str:
        """
        Obtener el dni de la persona

        Return
        ------
        str
            Dni de la persona
        """
        return self.dni

    def getdireccion(self) -> str:
        """
        Obtener la direccion de la persona

        Return
        ------
        str
            Direccion de la persona
        """
        return self.direccion

    def gettelefono(self) -> str:
        """
        Obtener el telefono de la persona

        Return
        ------
        str
            Telefono de la persona
        """
        return self.telefono

    def getemail(self) -> str:
        """
        Obtener el email de la persona

        Return
        ------
        str
            Email de la persona
        """
        return self.email

    def setnombre(self, nombre: str):
        """
        Asignar un nombre a la persona

        Parametros
        ----------
        nombre : str
            Nombre de la persona
        """
        self.nombre = nombre

    def setapellido(self, apellido: str):
        """
        Asignar un apellido a la persona

        Parametros
        ----------
        apellido : str
            Apellido de la persona
        """
        self.apellido = apellido

    def setdni(self, dni: str):
        """
        Asignar un dni a la persona

        Parametros
        ----------
        dni : str
            Dni de la persona
        """
        self.dni = dni

    def setdireccion(self, direccion: str):
        """
        Asignar una direccion a la persona

        Parametros
        ----------
        direccion : str
            Direccion de la persona
        """
        self.direccion = direccion

    def settelefono(self, telefono: str):
        """
        Asignar un telefono a la persona

        Parametros
        ----------
        telefono : str
            Telefono de la persona
        """
        self.telefono = telefono

    def setemail(self, email: str):
        """
        Asignar un email a la persona

        Parametros
        ----------
        email : str
            Email de la persona
        """
        self.email = email

    def getdata(self) -> dict:
        """
        Obtener los datos de la persona en un diccionario

        Return
        ------
        dict
            Datos de la persona
        """
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
        }

    def getdata_str(self) -> str:
        """
        Obtener los datos de la persona en un string

        Return
        ------
        str
            Datos de la persona
        """
        return f"""
        Nombre:{self.nombre} 
        Apellido:{self.apellido} 
        Dni:{self.dni} 
        Direccion:{self.direccion} 
        Telefono:{self.telefono} 
        Email:{self.email}
        """

    def __str__(self) -> str:
        """
        Obtener los datos de la persona en un string

        Return
        ------
        str
            Datos de la persona
        """
        return self.getdata_str()
