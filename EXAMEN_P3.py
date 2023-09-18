import os
class Persona:
    def __init__(self, cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento

class Autor(Persona):
    contador_personas = 0

    def __init__(self, cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial):
        Autor.contador_personas += 1
        cod_persona = Autor.contador_personas
        super().__init__(cod_persona, nombre, apellido_paterno, apellido_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    @staticmethod
    def agregar_autor():
        try:
            print("======NUEVO AUTOR======")
            cod_autor = input("CÓDIGO: ")
            nombre = input("NOMBRE: ")
            apellido_paterno = input("APELLIDO PATERNO: ")
            apellido_materno = input("APELLIDO MATERNO: ")
            fecha_nacimiento = input("FECHA DE NACIMIENTO: ")
            pais = input("PAIS: ")
            editorial = input("EDITORIAL: ")

            autor = Autor(cod_autor, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, pais, editorial)

            with open("autores.txt", "a") as file:
                file.write(f"AUTOR: {autor.cod_persona}\n")
                file.write(f"CÓDIGO: {autor.cod_autor}\n")
                file.write(f"NOMBRE: {autor.nombre}\n")
                file.write(f"APELLIDOS: {autor.apellido_paterno} {autor.apellido_materno}\n")
                file.write(f"FECHA DE NACIMIENTO: {autor.fecha_nacimiento}\n")
                file.write(f"PAIS: {autor.pais}\n")
                file.write(f"EDITORIAL: {autor.editorial}\n")
                file.write(f"================================\n")
            print("Autor agregado exitosamente.")
        except Exception as e:
            mensaje = f"Error al agregar autor: {str(e)}"
            print(mensaje)
            mantenimiento.agregar_error(mensaje)

    @staticmethod
    def editar_autor():
        try:
            cod_autor = input("Ingrese el código del autor que desea editar: ")

            with open("autores.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("autores.txt", "w") as file:
                for line in lines:
                    if line.startswith("CÓDIGO:"):
                        autor_data = line.strip().split(": ")[1]
                        if autor_data == cod_autor:
                            found = True
                            print("Autor encontrado. Ingrese los nuevos datos:")
                            print("========NUEVOS DATOS DEL AUTOR=========")
                            nombre = input("NUEVO-> NOMBRE: ")
                            apellido_paterno = input("NUEVO-> APELLIDO PATERNO: ")
                            apellido_materno = input("NUEVO-> APELLIDO MATERNO: ")
                            fecha_nacimiento = input("NUEVA-> FECHA DE NACIMIENTO: ")
                            pais = input("NUEVO-> PAIS: ")
                            editorial = input("NUEVA-> EDITORIAL: ")

                            file.write(f"AUTOR: {autor_data}\n")
                            file.write(f"CÓDIGO: {cod_autor}\n")
                            file.write(f"NOMBRE: {nombre}\n")
                            file.write(f"APELLIDOS: {apellido_paterno} {apellido_materno}\n")
                            file.write(f"FECHA DE NACIMIENTO: {fecha_nacimiento}\n")
                            file.write(f"PAIS: {pais}\n")
                            file.write(f"EDITORIAL: {editorial}\n")
                            file.write(f"================================\n")
                        else:
                            file.write(line)
                    else:
                        file.write(line)

            if not found:
                print("No se encontró ningún autor con ese código.")
            else:
                print("Autor editado exitosamente.")
        except Exception as e:
            print(f"Error al editar autor: {e}")

    @staticmethod
    def eliminar_autor():
        try:
            cod_autor = input("Ingrese el código del autor que desea eliminar: ")

            with open("autores.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("autores.txt", "w") as file:
                for line in lines:
                    if line.startswith("CÓDIGO:"):
                        autor_data = line.strip().split(": ")[1]
                        if autor_data == cod_autor:
                            found = True
                            print("Autor encontrado y eliminado.")
                        else:
                            file.write(line)
                    else:
                        file.write(line)

            if not found:
                print("No se encontró ningún autor con ese código.")
        except Exception as e:
            print(f"Error al eliminar autor: {e}")

class Libro:  # Clase asociada de Autor
    def __init__(self, codigo_libro, titulo, año, tomo, autor):
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.año = año
        self.tomo = tomo
        self.autor = autor

    @staticmethod
    def agregar_libro():
        try:
            print("======NUEVO LIBRO======")
            codigo_libro = input("CÓDIGO: ")
            titulo = input("TÍTULO: ")
            año = input("AÑO: ")
            tomo = input("TOMO: ")

            # Mostrar categorías disponibles
            categorias = Categoria.obtener_categorias()
            print("CATEGORÍAS DISPONIBLES:")
            for i, categoria in enumerate(categorias):
                print(f"{i + 1}. {categoria.cod_categoria} - {categoria.categoria}")

            categoria_index = int(input("Seleccione el número de la categoría: ")) - 1
            categoria_elegida = categorias[categoria_index]

            agregar_autor = input("¿Desea agregar un autor? (S/N): ")
            if agregar_autor.upper() == "S":
                # Mostrar autores disponibles
                with open("autores.txt", "r") as file:
                    autores_disponibles = [line.strip() for line in file.readlines() if line.startswith("NOMBRE:")]

                if autores_disponibles:
                    print("AUTORES DISPONIBLES:")
                    for i, autor in enumerate(autores_disponibles):
                        print(f"{i + 1}. {autor.split(': ')[1]}")
                    autor_index = int(input("Seleccione el número del autor: ")) - 1
                    autor_elegido = autores_disponibles[autor_index].split(': ')[1]
                else:
                    print("No hay autores disponibles.")
                    autor_elegido = input("Ingrese el nombre del autor: ")
            else:
                autor_elegido = "Anónimo"

            with open("REPORTE_LIBROS.txt", "a") as file:
                file.write(f"CÓDIGO: {codigo_libro}\n")
                file.write(f"TÍTULO: {titulo}\n")
                file.write(f"AÑO: {año}\n")
                file.write(f"TOMO: {tomo}\n")
                file.write(f"AUTOR: {autor_elegido}\n")
                file.write(f"CATEGORÍA: {categoria_elegida.categoria}\n")
                file.write(f"COD_CATEGORIA: {categoria_elegida.cod_categoria}\n")
                file.write("================================\n")
            print("Libro agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar libro: {e}")

    @staticmethod
    def editar_libro():
        try:
            codigo_libro = input("Ingrese el código del libro que desea editar: ")

            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []  # Usaremos una lista para almacenar las líneas actualizadas

            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("CÓDIGO:") and line.strip().split(": ")[1] == codigo_libro:
                    found = True
                    print("Libro encontrado. Ingrese los nuevos datos:")
                    print("========NUEVOS DATOS DEL LIBRO=========")
                    nuevo_codigo_libro = input("NUEVO-> CÓDIGO: ")
                    nuevo_titulo = input("NUEVO-> TÍTULO: ")
                    nuevo_año = input("NUEVO-> AÑO: ")
                    nuevo_tomo = input("NUEVO-> TOMO: ")

                    # Mostrar categorías disponibles
                    categorias = Categoria.obtener_categorias()
                    print("CATEGORÍAS DISPONIBLES:")
                    for j, categoria in enumerate(categorias):
                        print(f"{j + 1}. {categoria.cod_categoria} - {categoria.categoria}")

                    categoria_index = int(input("Seleccione el número de la nueva categoría: ")) - 1
                    nueva_categoria_elegida = categorias[categoria_index]

                    agregar_autor = input("¿Desea agregar un autor? (S/N): ")
                    if agregar_autor.upper() == "S":
                        # Mostrar autores disponibles
                        with open("autores.txt", "r") as autor_file:
                            autores_disponibles = [line.strip() for line in autor_file.readlines() if line.startswith("NOMBRE:")]

                        if autores_disponibles:
                            print("AUTORES DISPONIBLES:")
                            for k, autor in enumerate(autores_disponibles):
                                print(f"{k + 1}. {autor.split(': ')[1]}")
                            autor_index = int(input("Seleccione el número del nuevo autor: ")) - 1
                            nuevo_autor_elegido = autores_disponibles[autor_index].split(': ')[1]
                        else:
                            print("No hay autores disponibles.")
                            nuevo_autor_elegido = input("Ingrese el nombre del nuevo autor: ")
                    else:
                        nuevo_autor_elegido = "Anónimo"

                    # Actualizar los datos del libro en las líneas
                    updated_lines.append(f"CÓDIGO: {nuevo_codigo_libro}\n")
                    updated_lines.append(f"TÍTULO: {nuevo_titulo}\n")
                    updated_lines.append(f"AÑO: {nuevo_año}\n")
                    updated_lines.append(f"TOMO: {nuevo_tomo}\n")
                    updated_lines.append(f"AUTOR: {nuevo_autor_elegido}\n")
                    updated_lines.append(f"CATEGORÍA: {nueva_categoria_elegida.categoria}\n")
                    updated_lines.append(f"COD_CATEGORIA: {nueva_categoria_elegida.cod_categoria}\n")
                    updated_lines.append("================================\n")
                    i += 8  # Saltar las líneas del libro que hemos actualizado
                else:
                    updated_lines.append(line)
                    i += 1

            if not found:
                print("No se encontró ningún libro con ese código.")

            # Escribir las líneas actualizadas en el archivo
            with open("REPORTE_LIBROS.txt", "w") as file:
                file.writelines(updated_lines)
            print("Libro editado exitosamente.")
        except Exception as e:
            print(f"Error al editar libro: {e}")

    @staticmethod
    def eliminar_libro():
        try:
            codigo_libro = input("Ingrese el código del libro que desea eliminar: ")

            with open("REPORTE_LIBROS.txt", "r") as file:
                lines = file.readlines()

            found = False
            updated_lines = []

            i = 0
            while i < len(lines):
                line = lines[i]
                if line.startswith("CÓDIGO:") and line.strip().split(": ")[1] == codigo_libro:
                    found = True
                    print("Libro encontrado y eliminado.")
                    i += 8  # Saltar las líneas del libro que estamos eliminando
                else:
                    updated_lines.append(line)
                    i += 1

            if not found:
                print("No se encontró ningún libro con ese código.")

            # Escribir las líneas actualizadas en el archivo, lo que efectivamente elimina el libro
            with open("REPORTE_LIBROS.txt", "w") as file:
                file.writelines(updated_lines)
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
           
class Categoria:
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    @staticmethod
    def mostrar_libros_por_categoria(cod_categoria):
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

            
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def Menu_B_categoria():
    while True:
        clear_screen()
        print("==== MENU CATEGORIA ====")
        print("1. MOSTRAR LIBROS")
        print("2. BUSCAR POR CATEGORIA")
        print("3. <= VOLVER")
        op_categoria = input("Ingrese una opcion: ")
        if op_categoria == "1":
            clear_screen()
            Categoria.mostrar_libros_por_categoria_ordenados_ascendente()
            input("Enter para continuar...")
        elif op_categoria == "2":
            clear_screen()
            # Obtener el código de categoría deseado
            cod_categoria_deseado = input("Ingrese el código de la categoría: ")
            # Llamar al método para mostrar los libros en esa categoría
            Categoria.mostrar_libros_por_categoria(cod_categoria_deseado)
            input("Enter para continuar...")
        elif op_categoria == "3":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")

def Menu_autor():
    while True:
        clear_screen()
        print("==== MENU AUTOR ====")
        print("1. AGREGAR")
        print("2. EDITAR")
        print("3. ELIMINAR")
        print("4. <= VOLVER")
        
        op_autor = input("Ingrese una opción: ")
        
        if op_autor == "1":
            clear_screen()
            Autor.agregar_autor()
            input("Enter para continuar...")
        elif op_autor == "2":
            clear_screen()
            Autor.editar_autor()
            input("Enter para continuar...")
        elif op_autor == "3":
            clear_screen()
            Autor.eliminar_autor()
            input("Enter para continuar...")
        elif op_autor == "4":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")
            
def Menu_libro():
    while True:
        clear_screen()
        print("==== MENU LIBROS ====")
        print("1. AGREGAR")
        print("2. EDITAR")
        print("3. ELIMINAR")
        print("4. <= VOLVER")
        op_libro = input("Ingrese una opcion: ")
        if op_libro == "1":
            clear_screen()
            Libro.agregar_libro()
            input("Enter para continuar...")
        elif op_libro == "2":
            clear_screen()
            Libro.editar_libro()
            input("Enter para continuar...")
        elif op_libro == "3":
            clear_screen()
            Libro.eliminar_libro()
            input("Enter para continuar...")
        elif op_libro == "4":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")
def main_menu():
    while True:
        clear_screen()
        print("=== MENÚ PRINCIPAL ===")
        print("1. AUTOR")
        print("2. LIBROS")
        print("3. BUSQUEDA")
        print("4. SALIR")
        
        option = input("Ingrese una opción: ")
        
        if option == "1":
            Menu_autor()
        elif option == "2":
            Menu_libro()
        elif option == "3":
            Menu_B_categoria()
        elif option == "4":
            break
        else:
            input("Opción incorrecta. Enter para volver a intentar...")

if __name__ == "__main__":
    main_menu()