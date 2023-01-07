# Diego Marti­nez
# Ejercicio 1, Ayudantia 9

#-----------------------------------------FUNCIONES--------------------------------------------

def valor_consulta_medico(a):
    monto = 0
    if a == 'sofi­a' or a == 'alejandra' or a == 'daniel':
        monto = 40000
    else:
        monto = 35000
    return monto

def prevision_porcentaje(a):
    porcentaje = 0
    if a == 'fonasa':
        porcentaje = 15
    else:
        porcentaje = 80
    return porcentaje

def valor_consulta(a,b):
    valor = (a*b)/100
    return valor

def imprimir(a,lista,cont):
    print('\nEl doctor o doctora: ',a,'estaria disponible en los siguientes bloques:')
    print(' ')
    if cont == 0:
        print('-> No tiene bloques disponibles')
    else:
        for i in range(len(lista)):
            print('->',lista[i])
    print('\n--------------------------------------------------------------------------')
    
def imprimir_2 (lista1,lista2):
    print('\n----------------2da Pregunga.-------------------')
    print('\n--------------------------------------------------------------------------')
    indice = lista1.index(max(lista1))
    total = lista2[indice]
    print('\n->El medico que genera mas ingreso es',total,'con ->',lista1[indice],'$')
    print('\n--------------------------------------------------------------------------')
    
def imprimir_3 (lista1,lista2):
    print('\n----------------3ra Pregunga.-------------------')
    print('\n--------------------------------------------------------------------------')
    indice = lista1.index(min(lista1))
    total = lista2[indice]
    print('\n->El bloque que genera menos ingreso para el centro de salud es el',total,'con ->',lista1[indice],'$')
    print('\n--------------------------------------------------------------------------')

#-----------------------------------------MATRIZ--------------------------------------------

import numpy as np
programa = np.zeros([100,100])

#---------------------------------LISTAS/VARIABLE--------------------------------------------

bloques = []
doctores = []
disponible = []
pago = []
ingresosxbloque = []
nombre = ''
bloque = ''
cont = 0
suma = 0
total = 0

#-----------------------------------------PROGRAMA--------------------------------------------

arch = open('solicitudes.txt')
linea = arch.readline().strip()

while linea != '':
    partes = linea.split(',')
    paciente = partes[0].lower()
    doctor = partes[1].lower()
    bloque = partes[2]
    prevision = partes[3].lower()
    fono = int(partes[4])
   
    valor_medico =  valor_consulta_medico(doctor)   
    porcentaje = prevision_porcentaje(prevision)
    valor_total = valor_consulta(valor_medico,porcentaje)
    
    if bloque not in bloques:
        bloques.append(bloque)
    if doctor not in doctores:
        doctores.append(doctor)
   
    fila = doctores.index(doctor)
    columna = bloques.index(bloque)
    
    if programa[fila][columna].any():
        programa[fila][columna] += valor_total
    else:
        programa[fila][columna] = valor_total
        
    linea = arch.readline().strip()

arch.close()
#-------------------1ra PREGUNTA------------------------------

indice = len(bloques)
fila = len(programa)
columna = len(programa[0])

print('\n----------------1ra Pregunga.-------------------')
print('\n--------------------------------------------------------------------------')

for i in range(fila+1):   
    if indice == i:
        imprimir(nombre,disponible,cont)
        break
    if nombre != '':
        imprimir(nombre,disponible,cont)    
    cont = 0
    disponible = []
    nombre = doctores[i]   
    for x in range(columna):       
        if indice == x:
            break
        if programa[i][x].any():            
            continue
        else:
            cont += 1
            bloque = bloques[x]
            disponible.append(bloque)
            
#-------------------2da PREGUNTA------------------------------

indice = len(bloques)
fila = len(programa)
columna = len(programa[0])

for i in range(fila+1):
    if indice == i:
        break
    if suma != 0:
        pago.append(suma)
    suma = 0
    for x in range(columna):
        if indice == x:
            break
        if programa[i][x].any():
            suma += programa[i][x] 
        else:
            continue
            
imprimir_2(pago,doctores)

#-------------------3ra PREGUNTA------------------------------

indice = len(bloques)
fila = len(programa)
columna = len(programa[0])

for i in range(columna):
    if indice == i:
        break
    total = sum([fila[i] for fila in programa])
    ingresosxbloque.append(total)

imprimir_3(ingresosxbloque,bloques)

