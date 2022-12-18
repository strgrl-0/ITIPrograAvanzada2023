"""
Bastian Guerra Valdes,ITI
"""
#Mayor y menor
mayor = -1
menor = 10**10
mayor_su = ""
#mayor edad
mayor_ed = -1
menor_ed = 10**10
mayor_ed = ""
#Cantidad empleados
em_sant = 0
em_val = 0
em_ser = 0
#promedio edad
edad_sant = 0
edad_val = 0
edad_ser = 0

#leer archivo
archivo = open("sucursales.txt","r", encoding = "utf-8")
linea = archivo.readline().strip()

while linea != "":
    partes = linea.split(",")
    uno = partes[0]
    dos = partes[1]
    
    if uno == "Santiago":
        n = int(dos)
        for i in range(n):
            linea = archivo.readline().strip()
            em_sant += 1
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            edad_sant = edad_sant + int(dos)
            
    elif uno == "Valdivia":
        n = int(dos)
        for i in range(n):
            linea = archivo.readline().strip()
            em_val += 1
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            edad_val = edad_val + int(dos)
    elif uno  == "LaSerena":
        n = int(dos)
        for i in range(n):
            linea = archivo.readline().strip()
            em_ser += 1
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            edad_ser = edad_ser + int(dos)
    else:
        linea = archivo.readline().strip()

#Sucursal mayor 
if em_sant > em_val :
    mayor = em_sant
    if em_ser > mayor:
        mayor = em_ser
        mayor_su = "La Serena"
else:
    mayor = em_val

print("La sucursal mayor:",mayor_su)
print("Promedio edad sucursal Santiago:", (edad_sant / em_sant))
print("Promedio edad sucursal Valdivia:", (edad_val / em_val))
print("Promedio edad sucursal La Serena:", (edad_ser / em_ser))