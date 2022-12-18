"""
Bastian Alonso Guerra Valdes,ITI
"""
#Leer
archivo = open("file.txt","r",encoding = "utf-8")
linea = archivo.readline().strip()
#Variables
amar = 0
mayor = -1
color_mayor = ""
croa = 0
total = 0
blue = 0
porcentaje_blue = 0
porcentaje_abc = 0
a = 0
b = 0
c = 0
suma_adc = 0
maroon = 0

while linea != "":
    partes = linea.split(",")
    color = str(partes[0]).lower()
    idioma = str(partes[1]).lower()
    cantidad = int(partes[2])
    año = int(partes[3])
    total += 1
    if color == "blue":
        blue += 1
    if color == "yellow":
        amar += 1
    if idioma == "croatian" and año > 2005:
        croa += 1
    if año > mayor:
        mayor = año
        color_mayor = color
    if año >= 2002 and color == "green":
        a += 1
    if color == "maroon" and cantidad > 12:
        b += 1
    if idioma == "sotho":
        c += 1
    linea = archivo.readline().strip()
    
suma = a + b + c
porcentaje_blue = (blue / total) * 100
porcentaje_abc = (suma / total) * 100
print(amar,"Yellow")
print(croa,"Croatian")
print("El color maximo es",color_mayor,"en el año",mayor)
print("Blue tiene un",porcentaje_blue,"%")
print("Las condiciones se cumplen en el",porcentaje_abc,"% de los casos")