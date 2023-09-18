class Categoria:
    """
    Clase que representa una categoría de libros.
    """

    def __init__(self, cod_categoria, categoria):
        """
        Constructor de la clase Categoria.

        Args:
            cod_categoria (str): Código único de la categoría.
            categoria (str): Nombre de la categoría.
        """
        self.cod_categoria = cod_categoria
        self.categoria = categoria
        
    @classmethod
    def obtener_categorias(cls):
        datos_categorias = [
            ('B101', 'Ficción'),
            ('B102', 'No Ficción'),
            ('B103', 'Literatura infantil y juvenil'),
            ('B104', 'Referencia'),
            ('B105', 'Educación'),
            ('B106', 'Artes y Entretenimiento'),
            ('B107', 'Cocina y Gastronomía'),
            ('B108', 'Viajes'),
            ('B109', 'Ciencia y Tecnología'),
            ('B110', 'Autoayuda y Desarrollo personal')
        ]

        categorias = []
        for cod, cat in datos_categorias:
            categoria = Categoria(cod, cat)
            categorias.append(categoria)

        return categorias
    
    @staticmethod
    def mostrar_libros_por_categoria(cod_categoria):
        """
        Muestra los libros que pertenecen a una categoría específica identificada por su código.

        - Parámetros:
            - cod_categoria (str): El código de la categoría por la que se desea filtrar los libros.

        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.

        Esta función busca y muestra los libros en el archivo "REPORTE_LIBROS.txt" que tienen el código de
        categoría especificado. Imprime los detalles de cada libro, incluyendo su código, título, año, tomo,
        autor y el código de la categoría.
        """
        try:
            # Buscar y mostrar los libros con el código de categoría especificado
            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            found_books = False
            print("=====LIBROS DISPONIBLES=====")
            for i in range(0, len(lines), 8):
                if lines[i + 6].strip() == f"COD_CATEGORIA: {cod_categoria}":
                    found_books = True
                    print(f"{lines[i + 0].strip()}")
                    print(f"{lines[i + 1].strip()}")
                    print(f"{lines[i + 2].strip()}")
                    print(f"{lines[i + 3].strip()}")
                    print(f"{lines[i + 4].strip()}")
                    print(f"{lines[i + 5].strip()}")
                    print(f"{lines[i + 6].strip()}")
                    print("================================")

            if not found_books:
                print("No se encontraron libros en esta categoría.")
        except FileNotFoundError:
            print("El archivo 'REPORTE_LIBROS.txt' no se encuentra.")
        except Exception as e:
            print(f"Error al mostrar libros por categoría: {e}")

    @staticmethod
    def mostrar_libros_por_categoria_ordenados_ascendente():
        """
        Muestra los libros ordenados por categoría en orden ascendente.

        - Parámetros: Ninguno.
        - Retorno: Ninguno.
        - Excepciones: Puede generar excepciones si ocurre algún error durante la ejecución.

        Esta función lee los datos de los libros desde el archivo "REPORTE_LIBROS.txt", los almacena en una
        lista de diccionarios y luego los ordena por código de categoría en orden ascendente. Finalmente,
        muestra los detalles de los libros ordenados por categoría.
        """
        try:
            # Leer los datos de los libros desde el archivo
            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            # Crear una lista de diccionarios para almacenar los datos de los libros
            libros = []
            current_book = {}

            for line in lines:
                line = line.strip()
                if line.startswith("CÓDIGO:"):
                    current_book["CÓDIGO"] = line.split(": ")[1]
                elif line.startswith("TÍTULO:"):
                    current_book["TÍTULO"] = line.split(": ")[1]
                elif line.startswith("AÑO:"):
                    current_book["AÑO"] = line.split(": ")[1]
                elif line.startswith("TOMO:"):
                    current_book["TOMO"] = line.split(": ")[1]
                elif line.startswith("AUTOR:"):
                    current_book["AUTOR"] = line.split(": ")[1]
                elif line.startswith("COD_CATEGORIA:"):
                    current_book["COD_CATEGORIA"] = line.split(": ")[1]
                elif line == "================================":
                    libros.append(current_book)
                    current_book = {}

            # Ordenar los libros por cod_categoria
            libros_ordenados = sorted(libros, key=lambda libro: libro["COD_CATEGORIA"])

            # Mostrar los libros ordenados
            print("=====LIBROS ORDENADOS POR CATEGORÍA=====")
            for libro in libros_ordenados:
                print(f"CÓDIGO: {libro['CÓDIGO']}")
                print(f"TÍTULO: {libro['TÍTULO']}")
                print(f"AÑO: {libro['AÑO']}")
                print(f"TOMO: {libro['TOMO']}")
                print(f"AUTOR: {libro['AUTOR']}")
                print(f"COD_CATEGORIA: {libro['COD_CATEGORIA']}")
                print("================================")
        except FileNotFoundError:
            print("El archivo 'REPORTE_LIBROS.txt' no se encuentra.")
        except Exception as e:
            print(f"Error al mostrar libros por categoría ordenados ascendente: {e}")
