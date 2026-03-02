matriz = [
    [4, 7, 2, 9, 5, 7],
    [1, 3, 7, 6, 8, 0],
    [9, 2, 5, 7, 4, 6],
    [8, 7, 1, 3, 7, 2],
    [5, 0, 6, 4, 2, 9],
    [7, 8, 9, 2, 1, 7]
]

x = int(input("Dame etun numero: "))\


encontrados = []

for i in range (6):
    for j in range (6):
        if matriz[i][j] == x:
            encontrados.append([i,j])

if encontrados:
    print ("cordenadas encontradas:",encontrados)
else:
    print("no se encontro ningun numero")


