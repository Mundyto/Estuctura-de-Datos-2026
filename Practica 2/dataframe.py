import pandas as pd
df = pd.read_csv('./Housing.csv')
columnas_a_procesar = ['price','bedrooms','bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'sqft_above','sqft_basement','yr_built']

def sacar_media(lista):
    tamaño = len(lista)
    total = 0
    for i in lista:
        total = total + i
    media = total / tamaño
    return media

def sacar_moda(lista):
    frecuencia = {}
    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] = frecuencia[numero] + 1
        else:
            frecuencia[numero] = 1

    mayor_conteo = 0
    moda = None
    for numero, conteo in frecuencia.items():
        if conteo > mayor_conteo:
            mayor_conteo = conteo
            moda = numero
    return moda

def sacar_varianza(lista, media):
    tamaño = len(lista)
    sumavarianza = 0
    for x in lista:
        sumcuadrado = (x - media)**2
        sumavarianza = sumavarianza + sumcuadrado
    
    varianza = sumavarianza / (tamaño - 1)
    return varianza

for nombre_col in columnas_a_procesar:
    lista = df[nombre_col]
    
    print(f"\n--- ESTADÍSTICAS DE: {nombre_col} ---")

    media_res = sacar_media(lista)
    moda_res = sacar_moda(lista)
    varianza_res = sacar_varianza(lista, media_res)
    desviacion_res = varianza_res**0.5
    print("La media es de:", media_res)
    print("La moda es de:", moda_res)
    print("La variansa es:", varianza_res)
    print("La desviacion estandar es:", desviacion_res)