"""
Bastian Alonso Guerra Valdes,ITI
"""
nombre = ""
regio = ""
ciudad = ""
oc = ""
estado = ""
monto = 0
pro = 0
total = 0
total_monto = 0
coquim = 0
com_coquim = 0
por_entre = 0
por_camino = 0
por_retra = 0
por_devuel = 0
cant_entre = 0
cant_camino = 0
cant_retra = 0
cant_devuel = 0
mayor_devuel = -1
nombre_devuel = ""
barato = 10**10
nombre_barato = 0
compra_barato = ""
ingre_total = 0
monto_entre = 0
monto_devuel = 0 
monto_retra = 0
desc = 0
antofa = ""
#Leer
archivo = open("ali.txt","r",encoding = "utf-8")
linea = archivo.readline().strip()

while linea != "":
    partes = linea.split(",")
    nombre = str(partes[0]).lower()
    region = str(partes[1]).lower()
    ciudad = str(partes[2]).lower()
    oc = str(partes[3]).lower()
    estado = str(partes[4]).lower()
    monto = float(partes[5])
    total += 1
    total_monto = total_monto + monto
    if estado == "entregado":
        cant_entre += 1
        monto_entre = monto_entre + monto
    if estado == "en camino":
        cant_camino += 1
        compra_barata = monto
        if compra_barata < barato:
            nombre_barato = oc
    if estado == "retrasado":
        cant_retra += 1
        monto = float(monto)
        desc = desc + (monto * 0.10)
        monto_retra = monto_retra + monto
    if estado == "devuelto":
        cant_devuel += 1
        devuelto = monto
        monto_devul = monto_devuel + monto
        if devuelto > mayor_devuel:
            nombre_devuel = nombre
            mayor_devuel = devuelto
    if region == "coquimbo":
        coquim += 1
        com_coquim = com_coquim + monto
    if region == "antofagasta":
       antofa = ciudad
    linea = archivo.readline().strip()
    
    
resta = monto_retra + monto_devuel
por_entre = ((cant_entre / total) *100)
por_retra = (cant_retra / total) *100
por_devuel = (cant_devuel / total) *100
por_camino = (cant_camino / total) *100
pro_coquim = (com_coquim / coquim)
ingre_total = monto_entre - resta
ingre_total = ingre_total - desc

print("1) Promedio compras Region de Coquimbo: $",pro_coquim)
print("2) Cantidades por estado de compra:")
print("- Entregadas:",cant_entre,"(",por_entre,"%",")") 
print("- En camino:",cant_camino,"(",por_camino,"%",")") 
print("- Retrasadas:",cant_retra,"(",por_retra,"%",")") 
print("- Devueltas:",cant_devuel,"(",por_devuel,"%",")") 
print("3) Compra devuelta mas cara: $",devuelto,"Hecha por",nombre_devuel)
print("4) Compra en camino más barata:",nombre_barato.upper())
print("5) Ingresos totales: $",ingre_total)
print("6) La utlima entrega en la region de antofagasta fue a:",antofa.upper())
    


    