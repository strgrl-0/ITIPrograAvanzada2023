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

def ggID(juegoS):
    games=["LOL","VALORANT","OVERWATCH"]
    for i in range(3):
        if juegoS == games[i]:
            ret=i
    return ret

def playerID(playerS):
    jugadores=["PABLO","JOSE","ALFONSO","JUAN"]
    for i in range(4):
        if playerS == jugadores[i]:
            ret=i
    return ret
                                
        
    

arch=open("partidas.txt","r") #File reading and storage into lists
line=arch.readline().strip()
Juego=[]; JuegoNID=[]; Resultado=[]; kda=[]; TipoMatch=[]; Player=[]; PlayerNT=[]; PlayerID=[]
while line != "":
    splt=line.split(",")
    juegoS=splt[0]; ResultadoS=splt[1]; kdaS=splt[2]; TipoMatchS=splt[3]; PlayerS=splt[4]
    kdaP=getKDA(kdaS); gID=ggID(juegoS); pID=playerID(PlayerS)
    add(Juego,juegoS); add(JuegoNID,gID); add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); add(Player, PlayerS); addifnt(PlayerNT,PlayerS); add(PlayerID, pID)
    line=arch.readline().strip()

print (JuegoNID, '\n', kda,'\n', PlayerNT,'\n')  #debug line for testing


def KDAdataF(Game,KDA,Plist):
    KDAdata=np.zeros([14,15])
    countG=0; countK=0; countP=0
    for f in range(14):            #Counts need a littler more thinking
                for cG in range(0,15,3):            #possible approach, reorder items after the matrix placement
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
    PData=np.zeros([4,4]); tmMain=[]
    Juegos=["LOL","VALORANT","OVERWATCH"]
    for f in range(4):
        for j in range(len(Juegos)):
            for i in range(len(Juego)):
                if Juego[i]==Juegos[j] and Player[i]==PlayerNT[f]:
                    PData[j][f]+=1
    for c in range(4):
        PData[3][c]=PData[0][c]+PData[1][c]+PData[2][c]
    return PData



KDAdata=KDAdataF(JuegoNID,kda,PlayerID)
print(KDAdata, '\n')

Mtest=PDataF(Juego,PlayerNT,Player)
print(Mtest)


for c in
    for f in

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