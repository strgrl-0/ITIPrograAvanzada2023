"""
Bastian Guerra Valdes,ITI
"""
#Variables
n = 0
mayor = -1
menor = 10**10
#Cantidad empleados
cant_em_ant = 0
cant_em_cal = 0
cant_em_ser = 0
#total empelados
total = 0
#Ponderados
pon_ant = 0
pon_cal = 0
pon_ser = 0
pon_menor = ""
#edades
edad_ant = 0
edad_cal = 0
edad_ser = 0
edad_int = 0
edad_33 = 0
#Promedio edades
pro_ant = 0
pro_cal = 0
pro_ser = 0
#Edad mayor
mayor_edad_ant = -1
mayor_edad_cal = -1
mayor_edad_ser = -1
#Nombre mayor
nombre_mayor = ""
nombre_mayor_ant = ""
nombre_mayor_cal = ""
nombre_mayor_ser = ""


#Leer archivo
archivo = open("sucursales.txt","r")
linea = archivo.readline().strip()


#Mientas la linea no este vacia
while linea != "":
    partes = linea.split(",")
    uno = partes[0]
    dos = partes[1]
    
    if uno == "Antofagasta": #Cantidad de personas sede Antofa
        n = int(dos)
        for i in range(n): 
            linea = archivo.readline().strip()
            cant_em_ant += 1
            partes = linea.split(",")
            uno = partes[0]
            dos = partes[1]
            dos = int(dos)
            edad_ant = edad_ant + dos
            if dos > mayor_edad_ant:
                mayor_edad_ant = dos
                nombre_mayor_ant = uno
            if dos >= 25 and dos <= 30:
                edad_int = edad_int + dos
            if dos == 33:
                edad_33 = uno
        pro_ant = edad_ant / n
    else:
        if uno == "Calama": #Cantidad de personas sede Antofa
            n = int(dos)
            for i in range(n): 
                linea = archivo.readline().strip()
                cant_em_cal += 1
                partes = linea.split(",")
                uno = partes[0]
                dos = partes[1]
                dos = int(dos)
                edad_cal = edad_cal + dos
                if dos > mayor_edad_cal:
                    mayor_edad_cal = dos
                    nombre_mayor_cal = uno
                if dos >= 25 and dos <= 30:
                    edad_int = edad_int + dos
                if dos == 33:
                    edad_33 = uno
            pro_cal = edad_cal / n    
        else:
            if uno == "La Serena": #Cantidad de personas sede Antofa
                n = int(dos)
                for i in range(n): 
                    linea = archivo.readline().strip()
                    cant_em_ser += 1
                    partes = linea.split(",")
                    uno = partes[0]
                    dos = partes[1]
                    dos = int(dos)
                    edad_ser = edad_ser + dos
                    if dos > mayor_edad_ser:
                        mayor_edad_cal = dos
                        nombre_mayor_ser = uno
                    if dos >= 25 and dos <= 30:
                        edad_int = edad_int + dos
                    if dos == 33:
                        edad_33 = uno
                pro_ser = edad_ser / n
            else:
                linea = archivo.readline().strip()
                
#Total empleados
total = cant_em_ant + cant_em_cal + cant_em_ser 
#Porcentaje intervalo edad 25-30
por = ( total * edad_int) / 100 
#Ponderado 
pon_ant = (cant_em_ant * 10) + (pro_ant * 0.5)
pon_cal = (cant_em_cal * 10) + (pro_cal * 0.5)
pon_ant = (cant_em_ser * 10) + (pro_ser * 0.5)
#Ponderado menor
if pon_ant < pon_cal:
    pon_menor = "Antofagasta"
elif pon_ant < pon_ser:
        pon_menor = "Antofagasta"
else:
    pon_menor = "La Serena"
        
#Mayor cantidad de empleados sucursal
if cant_em_ant > cant_em_cal:
    sede = "Antofagasta"
    mayor = cant_em_ant
    if cant_em_ant > cant_em_ser:
        sede = "Antofagasta"
        mayor = cant_em_ant
    else:
        sede = "La Serena"
        mayor = cant_em_ser
        
#Mayor edad entre empleados
if mayor_edad_ant > mayor_edad_cal:
    nombre_mayor = nombre_mayor_ant
    if mayor_edad_ant > mayor_edad_ser:
        nombre_mayor = nombre_mayor_ant
    else:
        nombre_mayor = nombre_mayor_ser
        
print("La sede con la mayor cantidad de empleados es",sede,"con la cantidad de",mayor,"empleados")
print("Promedio edad sucursal Antofagasta:",  edad_ant / cant_em_ant )
print("Promedio edad ucursal Antofagasta:",  edad_cal / cant_em_cal )
print("Promedio edad sucursal Antofagasta:",  edad_ser / cant_em_ser )
print("El empleado con mayor edad es:",nombre_mayor)
print("Porcentajes de empleados que se encuentran entre 25-30 años:",por)
print("El empleado que tiene 33 años es:",edad_33)
print("La sucursal con la ponderacion menor es:",pon_menor)

