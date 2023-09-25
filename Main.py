import os # Para trabajar con clear_acreen
import xlwt # Para trabajar con archivos xls

from Alumno import Alumno
from Curso import Curso
from Docente import Docente

lista_alumnos = [] # Lista para almacenar los alumnos
lista_docente = [] # Lista para registrar los docentes
lista_curso = [] # Para registrar los cursos 

# Para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Registrar los alumnos
def registrar_alumnos():

    alumno1 = Alumno('Claudio', 'Manya', 'Jacobo', '71306106',
                     '20220385', 'Informatica y Sistemas', 2022)
    alumno2 = Alumno('Jhon', 'Echevarría', 'Castro', '71306029',
                     '20220386', 'Informatica y Sistemas', 2022)
    alumno3 = Alumno('Jacob', 'Morales', 'Romero', 'dni3',
                     '20220387', 'Informatica y Sistemas', 2022)
    alumno4 = Alumno('Tobey', 'Zevallos', 'Macklaren', 'dni4',
                     '20220388', 'Informatica y Sistemas', 2022)
    alumno5 = Alumno('Nazthia', 'Rivera', 'Amanez', 'dni5',
                     '20220389', 'Informatica y Sistemas', 2022)
    lista_alumnos.append(alumno1)
    lista_alumnos.append(alumno2)
    lista_alumnos.append(alumno3)
    lista_alumnos.append(alumno4)
    lista_alumnos.append(alumno5)
    
    print("[ALUMNOS REGISTRADOS]")
    # Crea el archivo
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Alumnos")

    # Escribe los datos de cabecera
    headers = ["Nombre", "Apellido Paterno", "Apellido Materno", "DNI", "Código", "Facultad", "Año de Ingreso"]
    for col, header in enumerate(headers):
        sheet.write(0, col, header)

    # Escribe el dato de cada uno
    for row, alumno in enumerate(lista_alumnos):
        sheet.write(row + 1, 0, alumno.get_nombre())
        sheet.write(row + 1, 1, alumno.get_ap_paterno())
        sheet.write(row + 1, 2, alumno.get_ap_materno())
        sheet.write(row + 1, 3, alumno.get_dni())
        sheet.write(row + 1, 4, alumno.get_codigo())
        sheet.write(row + 1, 5, alumno.get_facultad())
        sheet.write(row + 1, 6, alumno.get_anio_ingreso())

    # Guarda en el archivo alumnos
    workbook.save("DatosAlumnos.xls")

    print("Datos de alumnos guardados en alumnos.xls")

# Registrar docentes
def registrar_docentes():
    # Instancia para llenar los datos
    docente1 = Docente('Luis', 'Suñiga', 'Mackey', '71202017', '202200', 'FIIS')
    docente2 = Docente('Cristian', 'Mendez', 'Morales', '71202018', '202201', 'FIIS')
    # Agregar los docentes a la lista
    lista_docente.append(docente1)
    lista_docente.append(docente2)
    print("[DOCENTES REGISTRADOS]")
    
    # Crea el Excel 
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Docentes")

    # Escribe la caberecera
    headers = ["Nombre", "Apellido Paterno", "Apellido Materno", "DNI", "Código", "Facultad"]
    for col, header in enumerate(headers):
        sheet.write(0, col, header)

    # Escribe los datos
    for row, docente in enumerate(lista_docente):
        sheet.write(row + 1, 0, docente.get_nombre())
        sheet.write(row + 1, 1, docente.get_ap_paterno())
        sheet.write(row + 1, 2, docente.get_ap_materno())
        sheet.write(row + 1, 3, docente.get_dni())
        sheet.write(row + 1, 4, docente.get_codigo())
        sheet.write(row + 1, 5, docente.get_facultad())
        
    # Guarda en el archivo Docentes
    workbook.save("DatosDocentes.xls")

    print("Datos de docentes guardados en docentes.xls")

# Registrar los cursos 
def registrar_cursos():
    # Instancia para los datos del curso
    curso1 = Curso('201', 'Ingles I')
    curso2 = Curso('301', 'Ingles II')
    curso3 = Curso('101', 'Matematica I')
    curso4 = Curso('201', 'Matematica II')
    # Agregar los cursos a la lista
    lista_curso.append(curso1)
    lista_curso.append(curso2)
    lista_curso.append(curso3)
    lista_curso.append(curso4)
    
    print("[CURSOS REGISTRADOS]")

# Asignar cursos a los alumnos
def asignar_cursos_a_Alumnos():
    print("Asignando cursos a alumnos\n")
    
    for alumno in lista_alumnos:
        print(f"{alumno.get_nombre()}, elige tus cursos:")
        for idx, curso in enumerate(lista_curso):
            print(f"{idx + 1}: {curso.get_nombre()}")
        selected_courses = input("Ingresa los números de los cursos que deseas llevar (separados por espacios): ")
        selected_courses = selected_courses.split()

        for course_idx in selected_courses:
            course_idx = int(course_idx) - 1
            if 0 <= course_idx < len(lista_curso):
                selected_course = lista_curso[course_idx]
                alumno.agregar_curso(selected_course)
            else:
                print("Opción inválida")

    print("Cursos asignados a alumnos")
    
# Asignar docente a los cursos
def asignar_docente_curso():
    print("Asignación de cursos a docentes")

    # Mostrar lista de docentes disponibles
    print("Lista de docentes disponibles:")
    for idx, docente in enumerate(lista_docente):
        print(f"{idx + 1}: {docente.get_nombre()}")

    # Seleccionar docente por su índice
    docente_idx = int(input("Seleccione el número de docente: ")) - 1
    if docente_idx < 0 or docente_idx >= len(lista_docente):
        print("Opción inválida")
        return
    selected_docente = lista_docente[docente_idx]
    # Mostrar lista de cursos disponibles
    print("Lista de cursos disponibles:")
    for idx, curso in enumerate(lista_curso):
        print(f"{idx + 1}: {curso.get_nombre()}")
    # Seleccionar curso por su índice
    curso_idx = int(input("Seleccione el número de curso: ")) - 1
    if curso_idx < 0 or curso_idx >= len(lista_curso):
        print("Opción inválida")
        return
    selected_curso = lista_curso[curso_idx]
    # Asignar el curso al docente
    selected_curso.asignar_docente(selected_docente)
    print(f"Curso '{selected_curso.get_nombre()}' asignado al docente '{selected_docente.get_nombre()}'")


# Actualizar el docentes de cada curso
def actualizar_docente_curso():
    print("Actualización de docente en curso")

    # Mostrar lista de cursos con sus docentes asignados
    print("Lista de cursos con docentes asignados:")
    for idx, curso in enumerate(lista_curso):
        docente_asignado = curso.obtener_docente_asignado()
        docente_nombre = docente_asignado.get_nombre() if docente_asignado else "Ninguno"
        print(f"{idx + 1}: {curso.get_nombre()} - Docente asignado: {docente_nombre}")

    # Seleccionar curso por su índice
    curso_idx = int(input("Seleccione el número de curso a actualizar: ")) - 1
    if curso_idx < 0 or curso_idx >= len(lista_curso):
        print("Opción inválida")
        return

    selected_curso = lista_curso[curso_idx]

    # Mostrar lista de docentes disponibles
    print("Lista de docentes disponibles:")
    for idx, docente in enumerate(lista_docente):
        print(f"{idx + 1}: {docente.get_nombre()}")

    # Seleccionar docente por su índice
    docente_idx = int(input("Seleccione el número de nuevo docente: ")) - 1
    if docente_idx < 0 or docente_idx >= len(lista_docente):
        print("Opción inválida")
        return

    selected_docente = lista_docente[docente_idx]

    # Actualizar el docente asignado al curso
    selected_curso.asignar_docente(selected_docente)

    print(f"Docente del curso '{selected_curso.get_nombre()}' actualizado a '{selected_docente.get_nombre()}'")

# Registrar las notas de los alumnos
def registrar_notas_alumno():
    for alumno in lista_alumnos:
        for curso in alumno.Curso:  
            # Pedir las notas para cada curso
            print(f"Ingresando notas para el curso '{curso.get_nombre()}' del alumno '{alumno.get_nombre()}':")
            for _ in range(4): 
                nota = float(input("Ingrese la nota: "))
                curso.ingresar_notas(nota)  

# Reporte de alumnos
def reporte_alumno():
    print("Reporte de promedio de alumnos")

    for alumno in lista_alumnos:
        print("======================================")
        print(f"Nombre del alumno: {alumno.get_nombre()}")
        print(f"Código del alumno: {alumno.get_codigo()}")
        print(f"Facultad: {alumno.get_facultad()}")
        print("Cursos matriculados:")
        for curso in alumno.Curso:
            print(f"  - Curso: {curso.get_nombre()}")
            print(f"    Promedio: {curso.obtener_promedio()}")
        print("======================================")
        print()

    input("Presione Enter para continuar...")
    
    # Manejar con los archivos txt
    with open("ReporteAlumnos.txt", "w") as file:
        for alumno in lista_alumnos:
            file.write("==============================\n")
            file.write(f"Nombre del alumno: {alumno.get_nombre()}\n")
            file.write(f"Código del alumno: {alumno.get_codigo()}\n")
            file.write(f"Facultad: {alumno.get_facultad()}\n")
            file.write("Cursos matriculados:\n")
            for curso in alumno.Curso:
                file.write(f"  - Curso: {curso.get_nombre()}\n")
                file.write(f"    Promedio: {curso.obtener_promedio()}\n")
            file.write("==============================\n\n")

    print("Reporte de promedio de alumnos guardado en ReporteAlumnos.txt")

# Reporte de docentes
def reporte_docente():
    print("Reporte de docentes")

    for docente in lista_docente:
        print("==============================")
        print(f"Nombre del docente: {docente.get_nombre()}")
        print(f"Código del docente: {docente.get_codigo()}")
        print(f"Facultad: {docente.get_facultad()}")
        print("Cursos asignados:")
        for curso in lista_curso:
            if curso.obtener_docente_asignado() == docente:
                print(f"  - Curso: {curso.get_nombre()}")
        print("==============================")
        print()

    input("Presione Enter para continuar...")

    # Guardar el reporte en un archivo txt
    with open("ReporteDocentes.txt", "w") as file:
        for docente in lista_docente:
            file.write("==============================\n")
            file.write(f"Nombre del docente: {docente.get_nombre()}\n")
            file.write(f"Código del docente: {docente.get_codigo()}\n")
            file.write(f"Facultad: {docente.get_facultad()}\n")
            file.write("Cursos asignados:\n")
            for curso in lista_curso:
                if curso.obtener_docente_asignado() == docente:
                    file.write(f"  - Curso: {curso.get_nombre()}\n")
            file.write("==============================\n\n")

    print("Reporte de docentes guardado en ReporteDocentes.txt")
 
# Diccionario para el menu de opciones}
menu_options = {
    1: registrar_alumnos,
    2: registrar_docentes,
    3: registrar_cursos,
    4: asignar_cursos_a_Alumnos,
    5: asignar_docente_curso,
    6: actualizar_docente_curso,
    7: registrar_notas_alumno,
    8: reporte_alumno,
    9: reporte_docente
}
   
# Menu de opciones
while True:
    clear_screen()
    print("""
    ----MENU DE OPCIONES----
    [1] Matricular Alumnos
    [2] Registrar Docentes
    [3] Registrar cursos
    [4] Asignar cursos a Alumnos
    [5] Asignar Cursos_Docente
    [6] Actualizar Docente_Curso
    [7] Registrar notas de los Alumnos
    [8] Reporte Alumnos
    [9] Reporte Docentes
    [10] Salir
    """)
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Opción inválida. Ingresa un número válido.")
        input("Presione Enter para continuar...")
        continue
    
    if opcion == 10:
        clear_screen()
        print("¡Hasta luego!")
        break

    selected_option = menu_options.get(opcion)
    if selected_option:
        selected_option()
    else:
        print("Opción inválida")

    input("Presione Enter para continuar...")