A = [[5, 6, 13], [3, 10, 1], [2, 11, 3]]
B = [[1, 2, 17], [6, 5, 15], [3, 11, 12]]

resultado = [[sum(a * b for a, b in zip(fila_A, col_B)) 
              for col_B in zip(*B)] 
             for fila_A in A]

print(resultado)