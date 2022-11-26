"""
BASTIAN GUERRA VALDES ITI
"""
#Leer archivo
arch = open("dispositivos.txt","r", encoding = "utf-8")
linea = arch.readline().strip().lower()
#Variables
#Cantidad dispositivos
disp = 0
#numeros de cables rojos
rojo = 0
#Numeros de cables amarillos
amar = 0
#Numero de cables negros
negro = 0
#porcentaje
por = 0
#Variable que guarda que cable se cortara en texto
cortar = ""
#Guarda la variable de un cable cortado
cable_cortar = ""
#Suma 1 cada vez que se corta el segundo cable
cable2_cortar = 0

while linea != "":
    disp +=1
    partes = linea.split(",")
    cables = partes[0]
    cables = int(cables)
    #Si la cantidad de cables es 3
    if cables == 3:
        #Se resetea el numero rojo
        rojo = 0
        cables = 3
        #Se aplica lower para que todos los str esten en minusculas
        cable1 = str(partes[1]).lower()
        cable2 = str(partes[2]).lower()
        cable3 = str(partes[3]).lower()
        #Comprobacion
        if cable1 != "rojo" and cable2 != "rojo" and cable3 != "rojo":
            cortar = "segundo cable"
            cable_cortar = cable2
            cable2_cortar += 1
        elif cable3 == "blanco":
            cortar = "ultimo cable"
            cable_cortar = cable3
        elif cable2 == "azul" and cable1 == "azul":
            cortar = "Cortar segundo cable azul"
            cable_cortar = cable2
            cable2_cortar += 1
        print("dispositivo",disp,"tiene,",cables,"cables")
        print("cortar el",cortar,"(".strip(),cable_cortar.lower(),")")
    #Si son 4 cables
    elif cables == 4:
        #reset
        rojo = 0
        cable1 = str(partes[1]).lower()
        cable2 = str(partes[2]).lower()
        cable3 = str(partes[3]).lower()
        cable4 = str(partes[4]).lower()
        #Si un cable es rojo se suma 1
        if cable1 =="rojo":
            rojo += 1
        if cable2 =="rojo":
            rojo += 1
        if cable3 =="rojo":
            rojo += 1
        if cable4 =="rojo":
            rojo += 1
        #Comprobacion
        if rojo > 1:
            cortar = "ultimo cable"
            cable_cortar = cable4
        else:
            if cable4 == "amarillo" and rojo == 0:
                cortar = "primer cable"
                cable_cortar = cable1
            else:
                if rojo == 1:
                    cortar = "segundo cable"
                    cable_cortar = cable2
                    cable2_cortar += 1
                else:
                    if cable2 == "amarillo" and cable3 == "amarillo":
                        cortar = "ultimo cable"
                        cable_cortar = cable4
                    else:
                         cortar = "tercer cable"
                         cable_cortar = cable3
        print("dispositivo",disp,"tiene,",cables,"cables")
        print("cortar el",cortar,"(".strip(),cable_cortar.lower(),")") 
    #Si son 5 cables
    elif cables == 5:
        #Reset numeros amarillo y negro
         amar = 0
         negro = 0
         cable1 = str(partes[1]).lower()
         cable2 = str(partes[2]).lower()
         cable3 = str(partes[3]).lower()
         cable4 = str(partes[4]).lower()
         cable5 = str(partes[5]).lower()
         #Cable si es amarillo
         if cable1 =="amarillo":
             amar += 1
         if cable2 =="amarillo":
             amar += 1
         if cable3 =="amarillo":
             amar += 1
         if cable4 =="amarillo":
             amar += 1
         if cable5 =="amarillo":
             amar += 1 
         #Cable si es negro
         if cable1 =="negro":
            negro += 1
         if cable2 =="negro":
            negro += 1
         if cable3 =="negro":
            negro += 1
         if cable4 =="negro":
            negro += 1
         if cable5 =="negro":
            negro += 1
        #Comprobacion
         if cable5 == "negro":
             cortar = "cuarto cable"
             cable_cortar = cable4
         elif cable3 == "rojo" and amar > 1:
             cortar = "tercer cable"
             cable_cortar = cable3
         elif negro == 0:
             cortar = "segundo cable"
             cable_cortar = cable2
             cable2_cortar += 1
         else:
             cortar = "primer cable"
             cable_cortar = cable1
         print("dispositivo",disp,"tiene,",cables,"cables")
         print("cortar el",cortar,"(".strip(),cable_cortar.lower(),")") 
    #Lee una nueva linea de texto
    linea = arch.readline().strip().lower()
#Saca el porcentaje del cuantas veces se corto el segundo cable
por = (cable2_cortar / disp) * 100
#Cantidad de dispositivos
print("Se analizaron",disp,"dispositivos")
#Cuantas veces se corto el segundo cable
print("El cable 2 se corto",cable2_cortar,"veces.",por,"% del total")