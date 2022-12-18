"""
BASTIAN GUERRA ITI
"""
#Hacer calculo de que linea es mayor que las demas

arch = open("invocador.txt","r", encoding = "utf-8")
linea = arch.readline().strip().upper()
menu = 0
partida_normal = 0
partida_solo = 0
partida_flex = 0
top = 0
sup = 0
jg = 0
adc = 0
mid = 0
kda = 0
asesi = 0
muer = 0
asis = 0
por = 0
vic = 0
der = 0
total = 0
mayor = -1
carril = ""

while linea != "":
    partes = linea.split(",")
    tipo_partida = str(partes[0])
    carril = str(partes[1])
    campeon = str(partes[2])
    asesinatos = int(partes[3])
    muertes = int(partes[4])
    asistencias = int(partes[5])
    fin_de_partida = str(partes[6])
    linea = arch.readline().strip()

    if tipo_partida == "NORMAL":
        partida_normal += 1
    if tipo_partida == "SOLO":
        partida_solo += 1
        vic += 1
    if tipo_partida == "FLEX":
        partida_flex += 1
        vic += 1
    if carril == "TOP":
        top += 1
    if carril == "JG":
        jg += 1
    if carril == "MID":
        mid += 1
    if carril == "ADC":
        adc += 1
    if carril == "SUP":
        sup += 1
        
    asesi = asesi + asesinatos
    muer = muer + muertes
    asis = asis + asistencias
    total += 1
                
if top > jg and top > mid and top > adc and top > sup:
    mayor = top
    carril = "Top"
else:
    if jg > top and jg > mid and jg > adc and jg > sup:
        mayor = jg
        carril = "Jg"
    else:
       if  mid > top and mid > jg and mid > adc and mid > sup:
            mayor = mid
            carril = "Mid"
       else:
           if adc > top and adc > jg and adc > mid and adc > sup:
               mayor = adc
               carril = "Adc"
           else:
               mayor = sup
               carril = "Sup"
               
kda = (asesi / muer) + (asis / muer)
por = vic  / total 

if menu != 5:
        while menu != 5:
            print("--------------------")
            print("MENU")
            print("--------------------")
            print("1) Cantidad de partidas jugadas")
            print("2) Carril preferido")
            print("3) KDA")
            print("4) Porcentaje de victorias Clasificatorias")
            print("5) Salir")
            print("--------------------")
            op = int(input("Ingrese una opcion:"))
            while op < 1 or op > 5 :
                error = int(input("Ingrese una opcion válida:"))
                op = error
            if op == 1:
                print("Partidas jugadas")
                print("Normales:",partida_normal)
                print("Clasificatorias Solo/Duo:",partida_solo)
                print("Clasificatorias Flexibles:",partida_flex)
            elif op == 2:
                print("Carril preferido")
                print(carril)
            elif op == 3:
                print("KDA",kda)
            elif op == 4:
                print("Victorias en clasificatorias:",por * 100, "%")
            elif op == 5:
                print("GG")
                menu = 5
    






