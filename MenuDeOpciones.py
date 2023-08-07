# 24/07/2023
# Programa con un menu de opciones para ingresar notas y sacar promedio
notas = []

while True:
    print("Menú:")
    print("1. Ingresar notas")
    print("2. Calcular promedio")
    print("3. Salir")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        try:
            for i in range(10):
                # Pedir al usuario que ingrese la nota
                nota = float(input("Ingrese la nota {}: ".format(i + 1)))
                
                # Verificar si la nota está dentro del rango válido (0-20)
                if nota < 0 or nota > 20:
                    raise ValueError("Error: La nota debe estar en el rango de 0 a 20.")
                
                # Agregar la nota válida a la lista
                notas.append(nota)
        
        except ValueError as e:
            # Capturar la excepción si el usuario ingresa un valor no numérico o una nota fuera del rango válido
            print(e)
    
    elif opcion == "2":
        if len(notas) == 0:
            # Verificar si se han ingresado notas antes de calcular el promedio
            print("Error: No se han ingresado notas.")
        else:
            # Calcular el promedio de las notas ingresadas
            promedio = sum(notas) / len(notas)
            print("El promedio de las notas es: {:.2f}".format(promedio))
    
    elif opcion == "3":
        break  # Salir del ciclo y finalizar el programa
    
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
# COMPLETADO