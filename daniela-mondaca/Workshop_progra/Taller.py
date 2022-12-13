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

arch=open("partidas.txt","r") #File reading and storage into lists
line=arch.readline().strip()
Juego=[]; JuegoNT=[]; Resultado=[]; kda=[]; TipoMatch=[]; Player=[]
while line != "":
    splt=line.split(",")
    juegoS=splt[0]; ResultadoS=splt[1]; kdaS=splt[2]; TipoMatchS=splt[3]; PlayerS=splt[4]
    kdaP=getKDA(kdaS)
    add(Juego,juegoS); add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); add(Player, PlayerS); addifnt(JuegoNT,juegoS)
    line=arch.readline().strip()

print (Juego, kda)  #debug line for testing


def KDAdataF(Game,KDA,Plist):
    KDAdata=np.zeros([10,10])
    count=0
    for i in range(len(Plist)):
        for Plist[i] in Plist:
            for f in range(len(Plist)):
                Counti=0                    #Counts need a littler more thinking
                for cG in range(0,11,2):
                    Counti+=1; count+=1
                    KDAdata[f][cG]=Game[Counti]
                for cK in range(1,11,2):
                    Counti+=1; count+=1
                    KDAdata[f][cK]=KDA[Counti]
    return()