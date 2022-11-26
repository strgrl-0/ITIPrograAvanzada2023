#Diego Marti­nez C7

'''----------------------------------------------------------------------------
-------------------------------- FUNCIONES ------------------------------------
----------------------------------------------------------------------------'''

def Menu_principal():
    print('''\n----------------------------------------------------------------
                           MENU
----------------------------------------------------------------
          1) Cantidad de partidas jugadas
          2) Carril preferido
          3) KDA
          4) Porcentaje de victimas en clasificatorias
          5) Salir    
----------------------------------------------------------------''')
    
'''----------------------------------------------------------------------------
-------------------------------- VARIABLES ------------------------------------
----------------------------------------------------------------------------'''

contador = 0
tipo_partida = 0
carril = 0
campeon = 0
asesinatos = 0 
muertes = 0
asistencias = 0
fin_de_partida = 0
numerop_normal = 0
numerop_solo = 0
numerop_flex = 0
TOP = 0
MID = 0
JG = 0 
ADC = 0
SUPP = 0
canal_fav = ''
asesinatos_totales = 0
asistencias_totales = 0
muertes_totales = 0
contador_victorias_solo = 0
contador_victorias_flex = 0
victorias = 0

'''----------------------------------------------------------------------------
------------------------- LECTURA DE ARCHIVOS ---------------------------------
----------------------------------------------------------------------------'''

arch = open('invocador.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

'''----------------------------------------------------------------------------
------------------------------ PROGRAMA ---------------------------------------
----------------------------------------------------------------------------'''

while linea != '':
    partes = linea.split(',')
    tipo_partida = str(partes [0])
    carril = str(partes [1])
    campeon = str(partes [2])
    asesinatos = int(partes [3])
    asesinatos_totales += asesinatos
    muertes = int(partes [4])
    muertes_totales += muertes
    asistencias = int(partes [5])
    asistencias_totales += asistencias
    fin_de_partida = str(partes [6])
    linea = arch.readline().strip()

# 1ra opción del menú:
    
    if tipo_partida == 'NORMAL':
        numerop_normal += 1
    if tipo_partida == 'SOLO':
        numerop_solo += 1
    if tipo_partida == 'FLEX':
        numerop_flex += 1
        
#2da opción del menú:
    
    if carril == 'TOP':
        TOP += 1 
    if carril == 'MID':
        MID += 1
    if carril == 'JG':
        JG += 1
    if carril == 'ADC':
        ADC += 1
    if carril == 'SUPP':
        SUPP += 1
        
    if TOP > MID and TOP > JG and TOP > ADC and TOP > SUPP:
        canal_fav = 'Superior'
    else:
        if MID > TOP and MID > JG and MID > ADC and MID > SUPP:
            canal_fav = 'Central'
        else: 
            if JG > TOP and JG > MID and JG > ADC and JG > SUPP:
                canal_fav = 'Jungla'
            else:
                if ADC > TOP and ADC > MID and ADC > JG and ADC > SUPP:
                    canal_fav = 'Tirador'
                else: 
                    if SUPP > TOP and SUPP > MID and SUPP > JG and SUPP > ADC:
                        canal_fav = 'Soporte'
                    
#4ta opción del menú:
         
    if fin_de_partida == 'VICTORIA' and tipo_partida == 'SOLO': 
        contador_victorias_solo += 1
    if fin_de_partida == 'VICTORIA' and tipo_partida == 'FLEX': 
        contador_victorias_flex += 1
    if fin_de_partida == 'VICTORIA':
        victorias += 1
        
victorias_clasificacion = contador_victorias_solo + contador_victorias_flex
porcentaje = float((100 *48)//68)         
  
#3ra opción del menú:
    
KDA = (asesinatos_totales/muertes_totales)+(asistencias_totales/muertes_totales)

# Menú
        
while contador != 1:
    
    Menu_principal()
    opcion = int(input('\nIngrese una opción: '))
    if opcion == 1:
        print('\nPartidas jugadas: ')
        print('\n1) Normales:', numerop_normal)
        print('\n1) Clasificatorias Solo/Duo:', numerop_solo)
        print('\n1) Clasificatorias Flexibles:', numerop_flex)
    if opcion == 2:
        print ('\nCarril Preferido:', canal_fav)
    if opcion == 3:
        print('\nKDA es de:', KDA)
    if opcion == 4:
        print('\nVictorias en Clasificaciones:', porcentaje, '%')
    if opcion == 5:
        print('\nGG')
        contador += 1  
        
    while contador != 1:
        Menu_principal()
        opcion = int(input('\nIngrese una opción válida: '))
        if opcion == 1:
            print('\nPartidas jugadas: ')
            print('\n1) Normales:', numerop_normal)
            print('\n1) Clasificatorias Solo/Duo:', numerop_solo)
            print('\n1) Clasificatorias Flexibles:', numerop_flex)
        if opcion == 2:
            print ('\nCarril Preferido:', canal_fav)
        if opcion == 3:
            print('\nKDA es de:', KDA)
        if opcion == 4:
            print('\nVictorias en Clasificaciones:', porcentaje, '%')
        if opcion == 5:
            print('\nGG')
            contador += 1        