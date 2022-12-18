"""
BASTIAN GUERRA VALDES ITI
"""
arch = open("invocador.txt","r", encoding = "utf-8")
linea = arch.readline().strip().upper()

rojo = 0
disp = 0
cortar = ""
cable4 = ""
cable5 = ""


while linea != "":
    disp += 1
    partes = linea.split(",")
    cables = partes[0]
    a = cables
    a = int(a)
    cable1 = str(partes[1])
    cable2 = str(partes[2])
    cable3 = str(partes[3])
    if a > 3 :
        cables4 = str(partes[4])
        if a > 4:
            cables5 = str(partes[5])
    
    if a == 3:
        if cable1 != "rojo" and cable2 != "rojo" and cable3 != "rojo":
            cortar = "rojo"
        elif cable3 == "blanco":
            cortar = cable3
        elif cable1 == "azul" and cable2 == "azul":
            cortar == cable2
        else:
            cortar == cable3
    if a == 4:
        if cable1 == "rojo" or cable2 == "rojo" or cable3 == "rojo" or cable4 == "rojo":
            if cable1 == "rojo":
                rojo += 1
            if cable2 == "rojo":
                rojo += 1
            if cable3 == "rojo":
                rojo += 1
            if cable4 == "rojo":
                rojo += 1
            if rojo > 1:
                cortar == cable4
        elif cable4 == "amarillo" and cable1 != "rojo" and cable2 != "rojo" and cable3 != "rojo":
            cortar = cable1
        elif rojo == 1:
            cortar = cable2
        elif cable2 == "amarillo" and cable3 == "amarillo":
            cortar = cable4
        else:
            cortar = cable3
            
print("Dispositivo",disp,"tiene",cables)
