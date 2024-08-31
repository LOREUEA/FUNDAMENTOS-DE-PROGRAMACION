# Matriz de 3 x 3
matriz = [
    [12, 16, 20],
    [22, 40, 45],
    [10, 11, 30]
]

print(matriz)
# funcion buscar_valor especifico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 16
print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print("valor encontrado en la posición",buscar_valor(matriz,valor_buscado))
else:
    print("valor incorrecto")


