import numpy as np

def add(list,elm):          #add function
    list.append(elm)
    return list.index(elm)

def addifnt(list, elm):
    if elm not in list:
        list.append(elm)
    return list.index(elm)

def getKDA(kda):        #KDA calculation
    spltK=kda.split("/")
    k=int(spltK[0]); d=int(spltK[1]); a=int(spltK[2])
    k=k*0.7; a=a*0.3
    kdaP=round((k+a)/d,1)
    return kdaP

def ggIDLista(juegoS):
    games=["LOL","VALORANT","OVERWATCH"]
    for i in range(3):
        if juegoS == games[i]:
            ret=i
    return ret

def ggID(Juegos):
    games=["LOL","VALORANT","OVERWATCH"]; ret=[]
    for i in range(3):
        for j in range(3):
            if Juegos[i]==games[j]:
                add(ret,j)
    return ret

def playerID(playerS):
    jugadores=["PABLO","JOSE","ALFONSO","JUAN"]
    for i in range(4):
        if playerS == jugadores[i]:
            ret=i
    return ret

def playertoID(PlayerNT):
    jugadores=["PABLO","JOSE","ALFONSO","JUAN"]; ret=[]
    for j in range(4):
        for i in range(4):
            if PlayerNT[j] == jugadores[i]:
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
    
    kdaP=getKDA(kdaS); gID=ggIDLista(juegoS); pID=playerID(PlayerS)
    
    add(Juego,juegoS); add(JuegoListaNID,gID); addifnt(JuegoNT,juegoS) 
    add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); 
    add(Player, PlayerS); addifnt(PlayerNT,PlayerS); add(PlayerID, pID)
    
    line=arch.readline().strip()

gIDNT=ggID(JuegoNT)
addifnt(JuegoNTNID,gIDNT)



def KDAdataF(Game,KDA,Plist):
    KDAdata=np.zeros([14,15])
    countG=0; countK=0; countP=0
    for f in range(14):            #Counts need a littler more thinking
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

def PDataF(Juego,PlayerNT,Player):
    PData=np.zeros([5,4])
    Juegos=["LOL","VALORANT","OVERWATCH"]
    for f in range(4):
        for j in range(len(Juegos)):
            for i in range(len(Juego)):
                if Juego[i]==Juegos[j] and Player[i]==PlayerNT[f]:
                    PData[j][f]+=1
    for c in range(4):
        PData[3][c]=PData[0][c]+PData[1][c]+PData[2][c]
        PIDs=playertoID(PlayerNT)
        PData[4][c]=PIDs[c]
    return PData



KDAdata=KDAdataF(JuegoListaNID,kda,PlayerID)
print(KDAdata, '\n')

PData=PDataF(Juego,PlayerNT,Player)
print(PData)


print("---------Funcion 1-----------")
playedWhat=["LOL","VALORANT","OVERWATCH"]
for f in range(3):
    max=int(PData[f][0]); JugadorST=PlayerNT[0]
    for c in range(4):
        if max<PData[f][c]:
            max=int(PData[f][c])
            JugadorST=PlayerNT[c]

    print("El jugador que más jugó ",playedWhat[f]," fue ",JugadorST," con ",max," horas registradas")


#FUNC 2 - Juego más jugado entre los 4
Tmax=np.zeros([1,3])
for c in range(3):
    for f in range(4):
        Tmax[0][c]=Tmax[0][c]+PData[c][f]

mat=np.zeros([2,3])
for j in range(3):
    mat[0][j]=Tmax[0][j]; gID=ggID(JuegoNT)
    mat[1][j]=gID[j]

max=mat[0][0]; max1=mat[1][0]; a=int(0)

for i in range(3):
    if max>a:
        max=mat[0][i]
        max1=mat[1][i]
    else:
        max=a
        
def retMPlayed(MasJugadoProc):
    for i in range(3):
        if MasJugadoProc==JuegoNTNID[0][i]:
            ret=JuegoNT[i]
    return ret
        
Mplayed=retMPlayed(max1)
print('\n')
print("--------------Funcion 2-------------")
print("El juego más jugado fue ",Mplayed,"con ",max," horas en total")

#Take Average KDA 
def avgKDA(array):
    totalKDA=0;  TtT=0              #fix ltr
    for i in range(14):
        for j in range(1,15,3):
            totalKDA=array[i][j]
            TtT=+1
    totalKDA=totalKDA/TtT
    return totalKDA

TtT=avgKDA(PData)
print(TtT)


'''

def PDataF(Juego,PlayerNT,Player):
    PData=np.zeros([4,4]); tmMain=[]
    Juegos=["LOL","VALORANT","OVERWATCH"]
    
    for j in range(len(Juegos)):
        cont=0
        for i in range(len(Juego)):
            if Juego[i]==Juegos[j] and Player[i]==PlayerNT[0]:
                cont+=1
        add(tmMain,cont)
    return tmMain


'''