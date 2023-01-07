# Diego Martínez C7
# Ejercicio 2

import numpy as np

SKU = []
categorias = []
comprobar = []
minimos_categorias = []
menor_articulo = []

arch = open('Productos.txt','r',encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    lista = []
    mini = 9999999999999999999999
    partes = linea.split(';')
    articulo = partes[1]
    categoria = partes[2]
    
    precio = int(partes[3])
    precio_falabella = int(partes[4])
    precio_ripley = int(partes[5])
    precio_paris = int(partes[6])
    
    lista.append(precio_falabella)
    lista.append(precio_ripley)
    lista.append(precio_paris)
    
    for x in lista:
        if mini > x:
            mini = x       
    
    if categoria not in categorias:
        categorias.append(categoria)
        comprobar.append(0)
        minimos_categorias.append(0)
        menor_articulo.append('')
        
    indice = categorias.index(categoria)
    menor_articulo[indice] = mini
    if mini > comprobar[indice]:
        minimos_categorias[indice] = precio
    
    linea = arch.readline().strip()