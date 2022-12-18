"""
Bastian Guerra Valdes,ITI
"""
#Cantidad vuelos
cant = 0
cant_sant = 0
cant_ant = 0
#Cantidad pasajeros
pas_sant = 0
pas_ant = 0
#Mayor y menor
mayor = -1
mayor_nom = ""
menor = 10**10
menor_nom = ""
#Menor a 100 pasajeros
menor_100 = 0

#Leer achivo
archivo = open("vuelos.txt","r", encoding = "utf-8")
linea = archivo.readline().strip()
print(linea)

while linea != "":
    partes = linea.split(",")
    uno = partes[0]
    dos = partes[1]
    tres = partes[2]
    cant += 1   
    linea = archivo.readline().strip()
    tres = int(tres)
    if tres > mayor :
        mayor = tres
        mayor_nom = dos
    if tres < menor :
        menor = tres
        menor_nom = dos
    if tres < 100:
        menor_100 += 1
    if dos == "Santiago":
        cant_sant =+ 1
    if uno == "Santiago":
        tres = int(tres)
        pas_sant = pas_sant + tres
    if uno == "Antofagasta":
        cant_ant=+ 1
        tres = int(tres)
        pas_ant = pas_ant + tres
    print(linea)
    
por = (menor_100 / cant)   

print("Cantidad total de vuelos:",cant)
print("Cantidad de vuelos a Santiago:",cant_sant + 1)
print("Promedio vuelos origen Antofagasta o Santiago",(pas_sant + pas_ant) / (cant_sant + cant_ant))
print("La ciudad de destino con mas pasajeros fue:",mayor_nom)
print("La ciudad de destino con menos pasajeros fue:",menor_nom)
print("Porcentaje de vuelos que transportaron menos de 100 personas:",por * 100)

    