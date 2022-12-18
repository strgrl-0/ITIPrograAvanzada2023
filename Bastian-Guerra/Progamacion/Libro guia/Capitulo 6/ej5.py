"""
Libro guia, cap 6, ej 5
"""
total = 0

archivo = open("numeros.txt","r",encoding = "utf-8")
linea = archivo.readline().strip()
partes = linea.split(",")
filas = int(partes[0])

for i in range(filas):
    linea = archivo.readline().strip()
    partes = linea.split(",")
    columnas = int(partes[0])
    
    for a in range(columnas):
        primer = int(partes[0])
        num = int(partes[a - primer])
        print(a,i,num)
        for b in range(a):
            total = total + num
            
if total == 0:
    print("El total de la matriz es 0")
else:
    print("La suma total de la matriz no da 0, tiene el valor de",total )
        