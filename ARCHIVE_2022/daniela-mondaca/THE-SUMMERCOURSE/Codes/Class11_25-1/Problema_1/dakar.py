#Daniela Ignacia Mondaca Rodriguez




import numpy as np

file=open('tiempos.txt','r')
line=file.readline().strip()

#def lists
pilot=[]; pilotNR=[]; cat=[]; catNR=[]; stg=[]; stgNR=[]; h=[]; m=[]; s=[]
#def metodos de agregado lista

def addNR(list,elm):
    if(elm not in list):
        list.append(elm)

def add(list,elm):
    list.append(elm)


while(line!=''):
    sep=line.split(',')

    add(pilot,sep[0]); addNR(pilotNR, sep[0])
    add(cat,sep[1].upper()); addNR(catNR,sep[1].upper())
    add(stg,sep[2]); addNR(stgNR,sep[2])
    add(h,int(sep[3])); add(m,int(sep[4])); add(s,int(sep[5]))

    line=file.readline().strip()

#crear matriz
mainARR=np.zeros([len(pilot),4])

#llenar
for i in range(len(pilot)):
    mainARR[i][0]=h[i]
    mainARR[i][1]=m[i]
    mainARR[i][2]=s[i]
    mainARR[i][3]=i

#errCTRL

keepM=True; keepE=True; keepC=True

while(keepM==True):
    if(keepE==True):
        Etapa=input("Que etapa desea analizar?"+'\n').upper()
        if(Etapa not in stgNR):
            print("La etapa no existe, reingrese la etapa a analizar"+'\n')
            keepC=False
            
        else:
            keepE==False
            keepC=True

    if(keepC==True):
        Category=input("Motos o SxS?"+'\n').upper()
        if(Category not in catNR):
            print("La categoria no existe, reingrese"+'\n')
            keepE=False
        else:
            keepC=False
            keepM=False

def procA(matriz, etapaLista, categoriaLista, etapaInput, categoriaInput, piloto):
    pointer=0
    for i in range(len(etapaLista)):
        if(etapaInput==etapaLista[i] and categoriaInput==categoriaLista[i]):
            pointer=etapaLista.index(etapaLista[i],i,i)
            print(pointer)

#EXEC
procA(mainARR,stg,cat,Etapa,Category,pilot)

