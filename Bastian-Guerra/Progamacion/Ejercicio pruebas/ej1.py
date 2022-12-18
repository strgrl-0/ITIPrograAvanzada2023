"""
Bastian Guerra ITI, ejercicio prueba I 
"""
#Nombres sucursal
nombre_1 = ""
nombre_2 = ""
#Cantidad sucursal
cant_suc = 0
#mayor
mayor_1 = -1
mayor_2 = -1
mayor_venta_sucursal_1 = ""
mayor_venta_sucursal_2 = ""
#Ventas unitarias
pro_1 = 0
pro_2 = 0
ventas1_suc1 = 0
ventas1_suc2 = 0
por_1 = 0
por_2 = 0
#total ventas
total_1 = 0
total_2 = 0
total = 0
#mayor ventas
mayor_1 = 0
mayor_2 = 0
n_mayor = ""
#producto caro
mayor_caro_1 = -1
mayor_caro_2 = -1
caro = ""
caro_1 = ""
caro_2 = ""
precio_caro = 0
precio_caro_1 = 0
precio_caro_2 = 0
nombre_caro = ""



#leer archivo
archivo = open("problema1.txt","r",encoding = "utf-8")
linea = archivo.readline().strip()


while linea != "":
    linea = archivo.readline().strip()
    partes = linea.split(",")
    uno = partes[0]
    if uno == "sucursal1":
        nombre_1 = uno
        cant_suc += 1
        partes = linea.split(",")
        uno = partes[0]
        dos = partes[1]
        n = int(dos)
        for i in range(n):
            linea = archivo.readline().strip()
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            tres = partes[2]
            pro_1 += 1
            total_1 = total_1 + (int(dos) * int(tres))
            venta_mayor_1 = int(dos) * int(tres)
            mayor_1 = mayor_1 + int(dos)
            precio_caro_1 = int(tres)
            if precio_caro_1 > mayor_caro_1:
                mayor_caro_1 = precio_caro_1
                caro_1 = uno
            if venta_mayor_1 > mayor_1:
                mayor_venta_sucursal_1 = uno
                mayor_1 = venta_mayor_1
            dos = int(dos)
            if dos == 1:
                ventas1_suc1 += 1       
    elif uno == "sucursal2":
        nombre_2 = uno
        cant_suc += 1
        partes = linea.split(",")
        uno = partes[0]
        dos = partes[1]
        n = int(dos)
        for i in range(n):
            linea = archivo.readline().strip()
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            tres = partes[2]
            pro_2 += 1
            total_2 = total_2 + (int(dos) * int(tres))
            venta_mayor_2 = int(dos) * int(tres)
            mayor_2 = mayor_2 + int(dos)
            precio_caro_2 = int(tres)
            if precio_caro_2 > mayor_caro_2:
                mayor_caro_2 = precio_caro_2
                caro_2 = uno
            if venta_mayor_2 > mayor_2:
                mayor_venta_sucursal_2 = uno
                mayor_2 = venta_mayor_2
            dos = int(dos)
            if dos == 1:
                ventas1_suc2 += 1

#Porcentaje ventas unitarias
por_1 = ventas1_suc1 / pro_1
por_2 = ventas1_suc2 / pro_2
#Total ventas
total = total_1 + total_2
#Mayor ventas
if mayor_1 > mayor_2:
    n_mayor = nombre_1
else:
    n_mayor = nombre_2
#Precio caro
if mayor_caro_1 > mayor_caro_2:
    caro = caro_1
    nombre_caro = nombre_1
    precio_caro = precio_caro_1
else:
    caro = caro_2
    nombre_caro = nombre_2
    precio_caro = precio_caro_2 


print("Producto con mayor venta en sucursal:",nombre_1)
print("es",mayor_1,"con total",mayor_venta_sucursal_1)
print("porcentajes de ventas unitarias es:",por_1 * 100,"%")
print("")
print("Producto con mayor venta en sucursal:",nombre_2)
print("es",mayor_2,"con total",mayor_venta_sucursal_2)
print("porcentajes de ventas unitarias es:",por_2 * 100,"%")
print("")
print("Total de ventas",total)
print("La sucursal con mas ventas",n_mayor)
print("Con total de ventas",total_2)
print("El producto mas caro fue",caro)
print("Vendido en la sucursal",nombre_caro)
print("Con un precio de",precio_caro)



         
        
 
            
        

