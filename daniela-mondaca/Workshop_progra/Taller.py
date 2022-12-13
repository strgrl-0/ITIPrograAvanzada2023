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

arch=open("partidas.txt","r") #File reading and storage into lists
line=arch.readline().strip()
Juego=[]; JuegoNID=[]; Resultado=[]; kda=[]; TipoMatch=[]; Player=[]; PlayerNT=[] 
while line != "":
    splt=line.split(",")
    juegoS=splt[0]; ResultadoS=splt[1]; kdaS=splt[2]; TipoMatchS=splt[3]; PlayerS=splt[4]
    kdaP=getKDA(kdaS); gID=ggID(juegoS)
    add(Juego,juegoS); add(JuegoNID,gID); add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); add(Player, PlayerS); addifnt(PlayerNT,PlayerS)
    line=arch.readline().strip()

print (JuegoNID, '\n', kda,'\n', PlayerNT,'\n')  #debug line for testing


def KDAdataF(Game,KDA,Plist):
    KDAdata=np.zeros([4,10])


KDAdata=KDAdataF(JuegoNID,kda,PlayerNT)
print(KDAdata)


'''
    countG=0; countK=0
    for i in range(len(Plist)):
        if Plist[i]=="PABLO":
            for f in range(len(Plist)):            #Counts need a littler more thinking
                for cG in range(0,10,2):
                    KDAdata[f][cG]=Game[countG]
                    countG+=1
                for cK in range(1,10,2):
                    KDAdata[f][cK]=KDA[countK]
                    countK+=1
    return(KDAdata)
'''