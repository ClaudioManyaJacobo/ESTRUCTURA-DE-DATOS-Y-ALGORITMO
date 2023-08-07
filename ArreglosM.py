# FECHA: 03/08/2023
# -> Clases de Python para los arreglos y las matricez

# agrega un elemento a lista
list.append()  
# extiende la lista con nuevos elementos
list.extend()
# inserta un elemento de una lista, teniendo en cuenta la posicion
list.insert()
#quita el primer elemento de una lista
list.remove()
#quita un elemento, teniendo la posicion y retorna el ultimo elemento
#pilas y colas
list.pop()
#retorna la posicion del elemento
list.index()
#cuenta el numero de veces que aparece un elemento
list.count()
#ordena los elementos
list.sort()
#invierte los elementos de una lista
list.reverse()
#retorna una copia de la lista
list.copy()

# crear una lista de frutas de la selva
fruta = ['piña', 'mango', 'mango', 'mango', 'caimito', 'guaba', 'puma rosa', 'pacay', 'guanabano']
#contar cuantas veces aparece la palabra mango
fruta.count('mango')
size = len(fruta)
size

fruta.index('mango')

fruta.append('papaya')
fruta

fruta.index('mango')
#fruta

fruta.insert(9, 'algo')
fruta

fruta.index('papaya')


fruta.sort()
fruta

fruta.reverse()
fruta

fruta.pop()
#fruta


# pilas -- LIFO
list_num = [15, 8, 6]
lista2 = [4,3]
#agregar elementos
list_num.append(lista2)
list_num.append(2)
list_num.append(5)
# mostrar los elemento
print(list_num)
list_num

#quitar elementos LIFO
list_num.pop()
list_num
list_num.pop()
list_num

# colas -- FIFO
# importar la libreria para el uso de colas
from collections import deque # C++ queque
#iniciando la lista con elementos
queque = deque(['A', 'B', 'C', 'D'])
#agregando elementos a la cola
queque.append('E')
queque.append('F')
queque.append('G')
#imprimiento los elementos de la cola
queque


queque.popleft()
queque

# crear una lista
arreglo = []
#agrega elementos a la lista 
for i in range(len(fruta)):
    #arreglo.append(i**2)
    arreglo.append(fruta[i])
    #print(fruta[i])
arreglo

#arreglo += list(map(lambda x:x**2, range(10)))
arreglo =  arreglo + list(map(lambda x:x**2, range(10)))
arreglo

# matrices tarea
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a elementos de la matriz
print(matriz[0][0])  # Imprime el primer elemento (fila 0, columna 0)
print(matriz[1][2])  # Imprime el elemento en la segunda fila y tercera columna (5)

# Modificar elementos de la matriz
matriz[1][1] = 10   # Cambia el valor de la segunda fila y segunda columna a 10

# Imprimir la matriz completa
for fila in matriz:
    print(fila)
# COMPLETADO