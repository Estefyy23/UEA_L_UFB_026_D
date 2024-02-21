
#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3)
#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).
#Muestra la matriz original y la matriz con la fila ordenada.

# array bidimensionales ejercicio 2

estefany_ejercicio_bi_2 = [

#   0,   1,   2 Columna

    [8,  9,   6], # 0 fila
    [2,  13,   4], # 1
    [30, 35, 32]  # 2
    ]

def bubble_sort(row):
    n = len(row)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if row[j] > row[j + 1]:
                row[j], row[j + 1] = row[j + 1], row[j]


def print_matrix(estefany_ejercicio_bi_2):
    for row in estefany_ejercicio_bi_2:


        print(row)


def sort_specific_row(estefany_ejercicio_bi_2, row_index):
    if row_index < 0 or row_index >= len(estefany_ejercicio_bi_2):
        print("Índice de fila fuera de rango")
        return

    bubble_sort(estefany_ejercicio_bi_2[row_index])

print("Matriz original:")
print_matrix(estefany_ejercicio_bi_2)

row_index = int(input("Ingrese el índice de la fila que desea ordenar (0, 1 o 2): "))
sort_specific_row(estefany_ejercicio_bi_2, row_index)

print("Matriz con la fila ordenada:")
print_matrix(estefany_ejercicio_bi_2)

