#array bidimensionales ejercicio 1

# array bidimensionales ejercicio 1

estefany_ejercicio_bi = [
    #   0    1    2
    [16,     6,   5],  # 0

    [8,     7,    2],  # 1

    [3,    4,    9]]  # 2


def buscar_valor(estefany_ejercicio_bi, valor):
    for i in range(len(estefany_ejercicio_bi)):
        for j in range(len(estefany_ejercicio_bi[i])):
            if estefany_ejercicio_bi[i][j] == valor:
                return f"El valor {valor} , se encontro en la posión ({i}, {j})."
    return f"El valor {valor}, no se encontro en la matriz"


# Valor a buscar

valor_a_buscar = 8


# Llamada a la función para buscar el valor
resul = buscar_valor(estefany_ejercicio_bi, valor_a_buscar)

print(resul)


