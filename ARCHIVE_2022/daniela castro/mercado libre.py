productos = []
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
ventas = []


import numpy as np
matriz1 = np.zeros([20,12])
suma = np.zeros([20,1])

def buscar_agregar(elemento,lista):
    if elemento not in lista:
        lista.append(elemento)
    return lista.index(elemento)

def suma_fila(matriz):
    for i in range(20):
        for j in range (12):
            suma[i,0] = suma[i][0] + matriz1[i][j]
    return suma

def buscar_mayor(matriz):
    mayor = suma[0][0]
    for a in range(20):
        if suma[a][0] > mayor:
            mayor = suma[a][0]
            vmayor = productos[a]
        if suma[a][0] == mayor:
            mayor1 = suma[a][0]
            vmayor1 = productos[a]
    return print('El(los) producto(s) con más ventas es(son):','\n*',vmayor,'\n*',vmayor1,'\ncon',int(mayor1),'unidades vendidas.')

# def buscar_menor(matriz):
#     menor = suma[0][0]
#     for b in range(20):
#         if suma[b][0] < menor:
#             menor = suma[b][0]
#             vmenor = productos[b]
#         if suma[b][0] == menor:
#             menor1 = suma[b][0]
#             vmenor1 = productos[b]
#             # for c in range(12):
                
#     return print('El(los) producto(s) con menos ventas es(son):','\n*',vmenor,'con',int(menor),'unidades vendidas.','\n*',vmenor1,'con',int(menor1),'unidades vendidas.')
def buscar_menor(matriz):
    menor = matriz[0][0]
    nombre = productos[0]
    texto="El(los) producto(s) con menos ventas es(son):\n"
 
    for b in range(20):
       a=matriz[b][0]
       if a <= menor:
           menor=a
           nombre=productos[b]
           texto=texto +"*" +nombre +" con "+str(menor)+" unidades vendidas.\n "
    return print(texto)

def cant_ventas(matriz):
    for d in range(20):
        ventas.append(int(suma[d][0]))
        print(productos[d],':',ventas[d])
    return 

arch = open('ventas.txt',encoding = 'utf-8')
linea = arch.readline().strip()



while linea != '':
    partes = linea.split('-')
    producto = partes[0]
    mes = partes[1]
    cantidad = int(partes[2])
    
    product = buscar_agregar(producto, productos)
    month = buscar_agregar(mes, meses)
    
    
    matriz1[product][month] += cantidad
    
    linea = arch.readline().strip()
    
suma_fila(matriz1)
buscar_mayor(suma)
buscar_menor(suma)
cant_ventas(suma)