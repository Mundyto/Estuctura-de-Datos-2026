calificaciones = [8,8,7,5,10,9,9,5,6,10]
calificaciones.sort()
aprobado = 7

contador=0
for cantidad in calificaciones:
    contador += cantidad
total = len(calificaciones)
promedio = contador / total
print("El promedio de las calificaciones es:", promedio)

lista_aprobados = calificaciones.copy()
for apro in calificaciones:
    if apro < aprobado:
        lista_aprobados.remove(apro)

print("Las calificaciones aprobadas son:", lista_aprobados)

lista_reprobados = calificaciones.copy()
for i in calificaciones:
    if i >= aprobado:
        lista_reprobados.remove(i) 
print("Las calificaciones reprobadas son:", lista_reprobados)