# Matriz bidimensional 3 x 3
matriz = [
    [25, 100, 96],
    [17, 72, 33],
    [13, 4,68]
]
print("Matriz original")
print(matriz)

# Método de ordenamiento buble_sort
def bubble_sort(fila):
    # algoritmo buble_sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i, -1):
            if fila[j] < fila[j-1]: # Se ubica el signo menor que (<) con el fin de ordenar ascendete como lo requiere la tarea
                fila[j], fila[j-1] = fila[j-1], fila[j]

# Ordenar la primera las filas de la matriz
bubble_sort(matriz[0])

print("Matriz con la primera fila ordenada")
print(matriz)

