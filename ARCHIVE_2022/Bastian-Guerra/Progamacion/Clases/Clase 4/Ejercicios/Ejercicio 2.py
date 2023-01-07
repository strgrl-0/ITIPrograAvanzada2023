"""
Bastian Guerra Valdes,ITI
"""
cant = 0
sant = 0
menor_100 = 0
anto_sant = 0
pas_anto_sant = 0
mayor = -1
menor = 10**10

archivo = open("vuelos.txt","r",encoding = "utf-8")
linea = archivo.readline().strip()
partes = linea.split(",")
origen = partes[0] #Desde que ciudad partio el vuelo
destino = partes[1] #Hacia que ciudad se dirigio el vuelo
cant_pas = partes[2] # La cantidad de pasajeros


while linea != "":
   
    partes = linea.split(",")
    origen = partes[0] #Desde que ciudad partio el vuelo
    destino = partes[1] #Hacia que ciudad se dirigio el vuelo
    cant_pas = partes[2] # La cantidad de pasajeros
    linea = archivo.readline().strip()
    cant += 1
    cant_pas = int(cant_pas)
    if destino == "Santiago": #Cantidad de vuelos a Santiago
        sant = sant +  1
    if origen == "Antofagasta" or origen == "Santiago":
        cant_pas = int(cant_pas)
        pas_anto_sant = pas_anto_sant + cant_pas
        anto_sant += 1
    if cant_pas > mayor:
        cant_pas
        mayor = cant_pas
        mayor_dest = partes[1] 
    if cant_pas < menor:
        cant_pas
        menor = cant_pas
        menor_dest = partes[1]
    if cant_pas < 100:
        menor_100 += 1
    
por = ((cant * menor_100) / 100)

print("Cantidad total de vuelos realizados: ",cant)
print("Cantidad total de vuelos hacia Santiago: ",sant)
print("Promedio pasajeros origen Antofagasta o Santiago: ",pas_anto_sant/anto_sant)
print("El destino con más pasajeros fue:",mayor_dest)
print("El destino con menos pasajeros fue:",menor_dest)
print("Porcentaje de vuelos de menos de 100 personas:",(por * 100),"%")

