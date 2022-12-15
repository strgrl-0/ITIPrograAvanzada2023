import numpy as np  #import numpy

def add(list,elm):          #add function
    list.append(elm)
    return list.index(elm)

def addifnt(list, elm):         #add if not there
    if elm not in list:
        list.append(elm)
    return list.index(elm)

def getKDA(kda):        #KDA calculation
    spltK=kda.split("/")
    k=int(spltK[0]); d=int(spltK[1]); a=int(spltK[2])
    k=k*0.7; a=a*0.3
    kdaP=round((k+a)/d,1)
    return kdaP

def ggIDLista(juegoS,Juegoflt,index):     #convierte la lista completa de elementos a indices numericos (contrasta Juego con JuegoNT, la lista sin repetición y devuelve un valor numerico de ello)
    for j in range(3):
        if juegoS[index] == Juegoflt[j]:
            ret=j
            break
    return ret

def ggID(JuegoNT):                       #convierte la lista de juegos sin repetir a indices numericos (la contrasta consigo misma)
    ret=[]
    for i in range(3):
        for j in range(3):
            if JuegoNT[i]==JuegoNT[j]:
                add(ret,j)
    return ret

def playerID(playerS,Playerflt,index):  #convierte la lista completa de elementos a indices numericos (contrasta Player con PlayerNT, la lista sin repeticion y devuelve un valor numerico de ello)
    for i in range(4):
        if playerS[index] == Playerflt[i]:
            ret=i
            break
    return ret

def playertoID(PlayerNT):               #convierte la lista de juegadores sin repetir a indices numericos (la contrasta consigo misma)
    ret=[]
    for j in range(4):
        for i in range(4):
            if PlayerNT[j] == PlayerNT[i]:
                add(ret,i)
    return ret
                                
        
    

arch=open("partidas.txt","r") #File reading and storage into lists
line=arch.readline().strip()

Juego=[]; JuegoListaNID=[]; JuegoNT=[] #Juego:Todos los juegos del archivo, en orden secuencial y formato str
JuegoNTNID=[]                          #JuegoListaNID: Todos los juegos del archivo, en orden secuencial y formato int
                                        #JuegoNT: Lista de juegos en el archivo sin repetición, en orden de aparición y formato str
                                        
Resultado=[]; kda=[]; TipoMatch=[]      #Resultado: Resultado de las partidas, en orden secuencial y formato str
                                        #kda: Kda(procesado) de las partidas, en orden secuencial y formato int
                                        #TipoMatch:Si una partida es clasificatoria o normal, en formato str
                                        
Player=[]; PlayerNT=[]; PlayerID=[]     #Player:Lista de jugadores que aparecen en el archivo, orden secuencial, sin filtro, str
                                        #PlayerNT: Lista de jugadores que aparecen en el archivo sin repetirse, orden secuencial, str
                                        #PlayerID: Lista de jugadores que aparecen en el archivo, secuencial, int   
while line != "":
    splt=line.split(",")                #order lists, they're getting complex and descriptions are required
    juegoS=splt[0]; ResultadoS=splt[1]; kdaS=splt[2]; TipoMatchS=splt[3]; PlayerS=splt[4]
    
    kdaP=getKDA(kdaS);                  #procesado sobre la marcha del kda, mientras se lee acorde a la función definida arriba
    
    add(Juego,juegoS); addifnt(JuegoNT,juegoS)              #Guardado de la lista de juegos en orden en el que aparecen, guardado de la lista de juegos en orden de aparición sin repetirse
    add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); #Guardado de los resultados, guardado del kda en base a el procesamiento de arriba, guardado del tipo de partida
    add(Player, PlayerS); addifnt(PlayerNT,PlayerS)    #Guardado de los jugadores en orden de aparición, guardado de los jugadores en orden de aparición sin repetirse
    line=arch.readline().strip()



for i in range(len(Juego)):
    gID=ggIDLista(Juego,JuegoNT,i); pID=playerID(Player,PlayerNT,i) #Convierte listas en formato str a formato ID usando las listas sin repetición
    add(PlayerID, pID); add(JuegoListaNID,gID)  #guarda dichas listas

gIDNT=ggID(JuegoNT)
add(JuegoNTNID,gIDNT)

def KDAdataF(Game,KDA,Plist):
    KDAdata=np.zeros([14,15])
    countG=0; countK=0; countP=0
    for f in range(14):            
                for cG in range(0,15,3):              #approach: sequential order, store Game/KDA/Player. a set of data = all 3 pieces
                    KDAdata[f][cG]=Game[countG]
                    countG+=1
                for cK in range(1,15,3):
                    KDAdata[f][cK]=KDA[countK]
                    countK+=1
                for cP in range(2,15,3):
                    KDAdata[f][cP]=Plist[countP]
                    countP+=1
    return(KDAdata)

def PDataF(Juego,JuegoNT,PlayerNT,Player):          #llena la matriz PData con la cantidad de partidas que se han jugado, los datos leidos verticalmente corresponden a las partidas del jugador,
    PData=np.zeros([5,4])                           #horizontalmente, corresponden al juego, las excepcion siendo la penultima fila (partidas totales por jugador en vertical, partidas totales)
    for f in range(4):                              #indiferentemente del jugador o juego en vertical. La ultima fila corresponde a indices numericos para indicar a que jugador pertenece cada
        for j in range(len(JuegoNT)):               #columna
            for i in range(len(Juego)):
                if Juego[i]==JuegoNT[j] and Player[i]==PlayerNT[f]: #el codigo funciona en base esta condicion logica. elige el indice de un jugador primero, despues un indice de la lista de juegos 
                    PData[j][f]+=1                      #sin repetir. contrasta ambas con los indices(que son comunes) de la lista de juegos completa y de jugadores, si ambos coinciden, agrega
    for c in range(4):                                  #un uno en la posicion de los indices de las listas sin repetir
        PData[3][c]=PData[0][c]+PData[1][c]+PData[2][c]
        PIDs=playertoID(PlayerNT)               #suma todas las partidas del jugador en una sola y la almacena, además, convierte y almacena el indice del jugador en la ultima fila
        PData[4][c]=PIDs[c]
    return PData

KDAdata=KDAdataF(JuegoListaNID,kda,PlayerID)
PData=PDataF(Juego,JuegoNT,PlayerNT,Player)

#PREGUNTA 1 - Jugador que mas jugo a un juego en especifico
print("---------Pregunta 1-----------")
for f in range(3):                                          #escanea la matriz y determina en simultaneo: 1-La cantidad de mas partidas jugadas por juego. 2-El jugador al que pertenecen dichas partidas
    max=int(PData[f][0]); JugadorST=PlayerNT[0]             
    for c in range(4):
        if max<PData[f][c]:
            max=int(PData[f][c])
            JugadorST=PlayerNT[c]

    print("El jugador que más jugó ",JuegoNT[f]," fue ",JugadorST," con ",max," partidas registradas")


#PREGUNTA 2 - Juego más jugado entre los 4
Tmax=np.zeros([1,3])                            
for c in range(3):                              #Primero, te reune todas las veces que un juego fue jugado
    for f in range(4):
        Tmax[0][c]=Tmax[0][c]+PData[c][f]

mat=np.zeros([2,3])                             #después asigna las ids numericas de los juegos a sus correspondientes partidas, en la fila de abajo. (use dos matrices diferentes? si, no se por que
for j in range(3):                              #tbh, es más complicado asi XDDDDDD, cosas de Daniela tuto, borra este parentesis cuando lo leas xdd, solo el parentesis)
    mat[0][j]=Tmax[0][j]; gID=ggID(JuegoNT)
    mat[1][j]=gID[j]


max=mat[0][0]; start=mat[1][0]              #Determina el mayor y el juego al que pertenece la cifra mayor (en id numerico)
for i in range(3):
    if max>start:
        max=mat[0][i]
        max1=mat[1][i]
    else:
        max=start
        
def retMPlayed(MasJugadoProc):                  #convierte el id numerico a la forma original, str
    for i in range(3):
        if MasJugadoProc==JuegoNTNID[0][i]:
            ret=JuegoNT[i]
    return ret
        
Mplayed=retMPlayed(max1)
print('\n')
print("--------------Pregunta 2-------------")
print("El juego más jugado fue ",Mplayed,"con ",max," partidas en total")       #muestra los datos

#Pregunta 3 - KDA Promedio GRAL
def avgKDA(array):
    totalKDA=0;  TtT=0              
    for i in range(14):                 #simple. toma el array del kda, escanea solo los kda del mismo y cuenta cuantos elementos son usando un acumulador. después hace un calculo simple de promedio
        for j in range(1,15,3):
            totalKDA=array[i][j]
            TtT=+1
    totalKDA=totalKDA/TtT
    return totalKDA

IndiferentGralKDA=avgKDA(KDAdata)
print('\n'); print("----------------------Pregunta 3--------------")                                #muestra los datos, nada mas nada menos
print("El KDA general, considerando todas las partidas, indiferente de juego o jugador es: ", IndiferentGralKDA)


#Pregunta 4 - Mejor KDA por juego
def scanKDAaG(KDAarray,gameNamesID):
    single=np.zeros([3,5]); cont=[0,0,0]; cK=0    
    for f in range(14):                                                 #escanea los indices de juegos almacenados en kdaData (de manera secuencial) y almacena el kda correspondiente a ese par de datos
        for cG in range(0,15,3):                    #3 contadores (en formato de una lista) mantienen tracking de que no sean mas de 5 datos, los mismos contadores junto a un if cortan el ciclo una vez
            cK=cG+1                                 #la matriz se llenó
            for i in range(3):
                    if gameNamesID[0][i]==KDAarray[f][cG]:
                        single[i][cont[i]]=KDAarray[f][cK]
                        if cont[i]<=3:
                            cont[i]+=1
                        else:
                            break
    return single
                                               #procesamiento. encontrar el kda más alto en cada juego y lo guarda junto a un indice correspondiente al juego en la fila de abajo
def encontrarMejor(first5Array,gameNTID):
    best=np.zeros([2,3]); 
    for f in range(3):
        firstV=first5Array[f][0]
        best[0][f]=firstV; best[1][f]=gameNTID[0][f]
        for c in range(5):
            current=first5Array[f][c]
            if firstV<current:
                best[0][f]=current

    return best


KDAscanned=scanKDAaG(KDAdata,JuegoNTNID); best=encontrarMejor(KDAscanned,JuegoNTNID)   

def gameIDNTtoStr(first5array,gamestr,gameID,mejor):         #Salida. Conversion Ids a string y procesamiento output
    print("\n")
    print("-----------Pregunta 4------------")
    print("Los mejores KDA son los siguientes")
    print('\n')
    for comp in range(3):
        for c in range(3):
            if first5array[1][comp]==gameID[0][c]:
                print("En", gamestr[c],":",mejor[0][c])
                
gameIDNTtoStr(best,JuegoNT,JuegoNTNID,best)


#Pregunta 5 - Cantidad total de partidas jugadas

def totalMatches(matchesArr):                   #otro simplecito suma las partidas totales, indiferente de juego o jugador (las totales estaban almacenadas por jugador en la matriz PData, came
    total=0                                     #in handy)
    for i in range(4):
        total=total+matchesArr[3][i]
    return(total)

matchesTot=totalMatches(PData)                  #Muestra datos
print('\n'); print("----------------Pregunta 5---------------")
print("La cantidad total de partidas jugadas es: ", matchesTot)
