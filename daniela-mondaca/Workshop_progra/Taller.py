def add(list,elm):          #add function
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
Juego=[]; Resultado=[]; kda=[]; TipoMatch=[]; Player=[]
while line != "":
    splt=line.split(",")
    juegoS=splt[0]; ResultadoS=splt[1]; kdaS=splt[2]; TipoMatchS=splt[3]; PlayerS=splt[4]
    kdaP=getKDA(kdaS)
    add(Juego,juegoS); add(Resultado,ResultadoS); add(kda,kdaP); add(TipoMatch, TipoMatchS); add(Player, PlayerS)
    line=arch.readline().strip()

print (Juego, kda)  #debug line for testing