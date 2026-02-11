numeros = [1,2,4,4,5,7,9,11,11,13,14,15,16,16]
numeros_sin_repetidos = []
for i in numeros:
    if i not in numeros_sin_repetidos:
        numeros_sin_repetidos.append(i)
print(numeros_sin_repetidos)