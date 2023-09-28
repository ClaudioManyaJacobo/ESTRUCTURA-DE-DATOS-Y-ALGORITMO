import rich
from datetime import datetime
from rich import box
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table

from cliente import Cliente
from gestor import Gestor
from gestor_objetos import GestorObjetos
from pelicula import Pelicula

LOGO = r"""
:::::::::  :::::::::: :::        ::::::::::: ::::::::  :::    ::: :::            :::      ::::::::  
:+:    :+: :+:        :+:            :+:    :+:    :+: :+:    :+: :+:          :+: :+:   :+:    :+: 
+:+    +:+ +:+        +:+            +:+    +:+        +:+    +:+ +:+         +:+   +:+  +:+        
+#++:++#+  +#++:++#   +#+            +#+    +#+        +#+    +:+ +#+        +#++:++#++: +#++:++#++ 
+#+        +#+        +#+            +#+    +#+        +#+    +#+ +#+        +#+     +#+        +#+ 
#+#        #+#        #+#            #+#    #+#    #+# #+#    #+# #+#        #+#     #+# #+#    #+# 
###        ########## ########## ########### ########   ########  ########## ###     ###  ########  
"""


def generar_tabla_rich_dict(diccionario: dict, objeto_id: str):
    tabla = Table(show_edge=True, show_header=False, box=box.MINIMAL)
    for key, value in diccionario.items():
        tabla.add_row(f"[magenta bold] {key.capitalize()}", str(value))
    tabla = Columns([Panel(tabla, title=objeto_id)], equal=True)
    return tabla


# Recuperar data usando gestor
peliculas_dict = Gestor.recuperar_data("data/peliculas_data.yml")  # Diccionario
clientes_dict = Gestor.recuperar_data("data/clientes_data.yml")  # Diccionario

r_console = rich.get_console()  # Libreria de consola


def devolver_pelicula(cliente: Cliente):
    r_console.clear()
    r_console.print(
        LOGO, justify="center", style="bold red", markup=False, highlight=False
    )
    rich.print("[bold green]Devolver pelicula")
    rich.print("[bold yellow]Peliculas alquiladas")
    for pelicula_id in cliente.peliculas_alquiladas:
        peliculas_dict_act = Gestor.recuperar_data("data/peliculas_data.yml")
        pelicula_data = peliculas_dict_act[pelicula_id]
        rich.print(generar_tabla_rich_dict(pelicula_data, pelicula_id))
    pelicula_id = r_console.input("[yellow] Seleccione Pelicula (ID): ")
    if pelicula_id in cliente.peliculas_alquiladas:
        cliente.peliculas_alquiladas.remove(pelicula_id)
        peliculas_dict[pelicula_id]["disponible"] = True
        clientes_dict[cliente.id]["peliculas_alquiladas"] = cliente.peliculas_alquiladas
        Gestor.guardar_data("data/peliculas_data.yml", peliculas_dict)
        Gestor.guardar_data("data/clientes_data.yml", clientes_dict)
        GestorObjetos.registro("devolucion", cliente.id, pelicula_id, "data/alquiler_data.yml")
        rich.print("[bold green]Devolucion exitosa")
        # Press Enter to continue
        r_console.input("[red] Presione Enter para continuar...")
    else:
        rich.print("[bold red]No tiene alquilada la pelicula", pelicula_id)


def ver_peliculas_alquiladas(cliente: Cliente):
    r_console.clear()
    r_console.print(LOGO, justify="center", style="bold red", markup=False)
    rich.print("[bold yellow]Peliculas alquiladas")

    for pelicula_id in cliente.peliculas_alquiladas:
        peliculas_dict_act = Gestor.recuperar_data("data/peliculas_data.yml")
        pelicula_data = peliculas_dict_act[pelicula_id]
        rich.print(generar_tabla_rich_dict(pelicula_data, pelicula_id))

    # Press Enter to continue
    r_console.input("[red] Presione Enter para continuar...")


def alquilar_pelicula(cliente: Cliente):
    r_console.clear()
    r_console.print(
        LOGO, justify="center", style="bold red", markup=False, highlight=False
    )
    r_console.print("[bold green]Alquilar pelicula")
    for pelicula_id, pelicula_data in peliculas_dict.items():
        if pelicula_data["disponible"]:
            rich.print(generar_tabla_rich_dict(pelicula_data, pelicula_id))

    pelicula_id = r_console.input("[yellow] Seleccione Pelicula (ID): ")

    try:
        peliculaa = Gestor.recuperar_data("data/peliculas_data.yml")[pelicula_id]
    except KeyError:
        r_console.print("[red] Ingrese un ID Valido")
        r_console.input("[red] Presione Enter para continuar...")
        return

    if peliculaa["disponible"]:
        cliente.agregar_pelicula_alquilada(pelicula_id)

        # Pelicula no disponible
        peliculas_dict[pelicula_id]["disponible"] = False

        # Update data en clientes dict
        clientes_dict[cliente.id]["peliculas_alquiladas"] = cliente.peliculas_alquiladas

        Gestor.guardar_data("data/peliculas_data.yml", peliculas_dict)
        Gestor.guardar_data("data/clientes_data.yml", clientes_dict)
        
        GestorObjetos.registro("alquiler", cliente.id, pelicula_id, "data/alquiler_data.yml")

        rich.print("[bold green]Alquiler exitoso")
        # Press Enter to continue
        r_console.input("[red] Presione Enter para continuar...")
    else:
        rich.print("[bold red]La pelicula no esta disponible")
        r_console.input("[red] Presione Enter para continuar...")


def ver_datos(cliente: Cliente):

    r_console.clear()
    r_console.print(
        LOGO, justify="center", style="bold red", markup=False, highlight=False
    )
    rich.print("[bold green]Datos del cliente")
    rich.print(generar_tabla_rich_dict(cliente.getclientedatasimple(), cliente.id))
    # Press Enter to continue
    r_console.input("[red] Presione Enter para continuar...")


def iniciar_sesion():
    r_console.clear()
    r_console.print(
        LOGO, justify="center", style="bold red", markup=False, highlight=False
    )
    r_console.print("[bold green]INICIO DE SESION", justify="center")
    cid = r_console.input("[bold yellow]Ingrese su ID: ")
    
    if cid == "CREATE":
        pelicula = Pelicula(
            nombre="El señor de los anillos",
            genero="Fantasia",
            duracion="120",
            clasificacion="B",
            idioma="Ingles",
            subtitulos="Español",
            sinopsis="Un hobbit tiene que destruir un anillo",
            director="Peter Jackson",
            actores="Elijah Wood, Ian McKellen, Viggo Mortensen",  # [Elijah Wood, Ian McKellen, Viggo Mortensen] Lista
            productora="New Line Cinema",
            pais="Estados Unidos",
            fecha="2001",
            precio=100,
        )
        data = pelicula.getdata()
        Gestor.agregar_data("data/peliculas_data.yml", data)
        return
    
    password = r_console.input("[bold yellow]Ingrese su password: ")
    cliente = GestorObjetos.recuperar_cliente(cid, "data/clientes_data.yml")

    if cliente:
        if cliente.password == password:
            r_console.print("[bold green]INICIO DE SESION EXITOSO", justify="center")
            r_console.clear()
            r_console.print(
                LOGO, justify="center", style="bold red", markup=False, highlight=False
            )
            cliente_menu = (
                """
            [bold]Bienvenido [green]"""
                + cliente.nombre
                + """
            
            [yellow]Seleccione una opcion:

            [reset]1. Alquilar pelicula
            2. Devolver pelicula
            3. Ver peliculas alquiladas
            4. Ver datos
            5. Salir
            """
            )
            r_console.print(cliente_menu, justify="center")

            opcion = r_console.input("[bold yellow] Opcion: ")
            if opcion == "1":
                alquilar_pelicula(cliente)
            elif opcion == "2":
                devolver_pelicula(cliente)
            elif opcion == "3":
                ver_peliculas_alquiladas(cliente)
            elif opcion == "4":
                ver_datos(cliente)
            elif opcion == "5":
                rich.print("[bold]Gracias por usar el sistema de alquiler de peliculas")
            else:
                rich.print("[bold red]Opcion invalida")
        else:
            rich.print("[bold red]Password incorrecto")
            r_console.input("[red] Presione Enter para continuar...")
    else:
        rich.print("[bold red]No existe el cliente con el id", cid)
        r_console.input("[red] Presione Enter para continuar...")


def registrarse():
    r_console.clear()
    r_console.print(
        LOGO, justify="center", style="bold red", markup=False, highlight=False
    )
    rich.print("[bold]Registrarse")
    rich.print("[bold]Ingrese su nombre:")
    nombre = input("Nombre: ")
    rich.print("[bold]Ingrese su apellido:")
    apellido = input("Apellido: ")
    rich.print("[bold]Ingrese su dni:")
    dni = input("DNI: ")
    rich.print("[bold]Ingrese su direccion:")
    direccion = input("Direccion: ")
    rich.print("[bold]Ingrese su telefono:")
    telefono = input("Telefono: ")
    rich.print("[bold]Ingrese su email:")
    email = input("Email: ")
    rich.print("[bold]Ingrese su password:")
    password = input("Password: ")
    cliente = Cliente(nombre, apellido, dni, direccion, telefono, email, password)
    cliente_data = cliente.getclientedata()
    Gestor.agregar_data("data/clientes_data.yml", cliente_data)
    rich.print("[bold green]Registro exitoso")
    rich.print(generar_tabla_rich_dict(cliente.getclientedatasimple(), cliente.id))
    # Press Enter to continue
    r_console.input("[red] Presione Enter para continuar...")


def main_menu():
    while True:
        r_console.clear()
        r_console.print(
            LOGO, justify="center", style="bold red", markup=False, highlight=False
        )
        menu_text = """
        [bold][green]Bienvenido al sistema de alquiler de peliculas

        [yellow]Seleccione una opcion:

        [reset]1. Iniciar sesion
        2. Registrarse
        3. Salir
        """
        r_console.print(menu_text, justify="center")
        opcion = r_console.input("[bold yellow]Opcion: ")
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrarse()
        elif opcion == "3":
            rich.print(
                "[bold green]Gracias por usar el sistema de alquiler de peliculas"
            )
            break
        else:
            rich.print("[bold red]Opcion invalida")


if __name__ == "__main__":
    main_menu()
