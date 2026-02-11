cereales = [12,24,16,15,20,18,6,10,12,11,15,12]
cereales.sort()
contador = 0

for cantidad in cereales:
    contador += cantidad
print("La cantidad total de cereales es:", contador, "toneladas")

total = len(cereales)
promedio = contador / total
print("El promedio de cereales por mes es:", promedio, "toneladas")

cereales_copias = cereales.copy()
for cantidad in cereales:
    if cantidad < promedio:
        cereales_copias.remove(cantidad)    
total_altas = len(cereales_copias)
print("El número de meses con cantidades de cereales por encima del promedio es:", total_altas)

cereales_bajas = cereales.copy()
for cantidad in cereales:
    if cantidad >= promedio:
        cereales_bajas.remove(cantidad)
total_bajas = len(cereales_bajas)
print("El número de meses con cantidades de cereales por debajo del promedio es:", total_bajas)

