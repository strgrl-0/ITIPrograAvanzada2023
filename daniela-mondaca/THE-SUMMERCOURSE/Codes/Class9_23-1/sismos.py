

#var def
Ciudad=[]; intensGMercalli=[]; CityNoRepeat=[]


#unrepeated
def addNR(list, elm):
    if elm not in list:
        list.append(elm)
        
def getMin(CityNR, CitiesR, Mercalli):   
    #first index = city, second index = mercalli
    indx=0; temp=[]
    for a in range(len(CityNR)):
        init=float(99.9)
        for i in range(len(CitiesR)): 
            if(CityNR[a]==CitiesR[i]):
                indx=CitiesR.index(CitiesR[i],i)
                
                if(Mercalli[indx]<init):
                    addNR(temp,CityNR[a])
                    init=Mercalli[indx]
        temp.append(init)      
    return(temp)

def getMaxnP(CityNR, CitiesR, Mercalli):
    
    indx=0; temp=[]; prom=0.0; promCalc=[]; count=0
    for a in range(len(CityNR)):
        init=float(-1)
        for i in range(len(CitiesR)):
            if(CityNR[a]==CitiesR[i]):
                indx=CitiesR.index(CitiesR[i],i)
                prom+=Mercalli[indx]; count+=1
                if(Mercalli[indx]>init):
                    addNR(temp,CityNR[a]); addNR(promCalc,CitiesR[a])
                    init=Mercalli[indx]
        temp.append(init)           
        promCalc.append(round(prom/count,2))
    return(temp, promCalc)               

                #print(CitiesR.index(CitiesR[i],i))
#EXEC BLOCK


#archi=str(input("Ingrese el nombre del archivo"+'\n'))
file=open('test.txt','r')
line=file.readline().strip()

while(line!=''):
    split=line.split(',')
    Ciudad.append(split[0]); intensGMercalli.append(float(split[1])); addNR(CityNoRepeat,split[0])
    line=file.readline().strip()

#req1
MinList=getMin(CityNoRepeat, Ciudad, intensGMercalli); MaxList, promedio=getMaxnP(CityNoRepeat, Ciudad, intensGMercalli)
#print(promedio)


def ordenarMayor(list):
    for i in range(1,(len(list)),2):
        for j in range(1, (len(list)),2):
            if(list[i]>list[j]):
                aux=list[i]
                list[i]=list[j]
                list[j]=aux
    return(list)

def ordenarMenor(list):
    for i in range(1,(len(list)),2):
        for j in range(1, (len(list)),2):
            if(list[i]<list[j]):
                aux=list[i]
                list[i]=list[j]
                list[j]=aux
    return(list)


#req2         
mayorIntensidadR=ordenarMayor(promedio)
print("Las ciudades con mayor promedio de intensidad registrado son (de mayor intensidad a menor): ")
for j in range(1,6,2):
    print(str(mayorIntensidadR[j])+" con "+str(mayorIntensidadR[j+1])+" Mercalli")

#givesomespace
print('\n')

#req3     
menorIntensidadR=ordenarMenor(promedio)   
print("Las ciudades con menor promedio de intensidad registrado son (de menor intensidad a mayor): ")
for j in range(0,6,2):
    print(menorIntensidadR[j]+" con "+str(menorIntensidadR[j+1])+" Mercalli")

#req4
masFPais=ordenarMayor(MaxList)
print('Los sismos más fuertes del país fueron:')
for j in range(0,6,2):
    print('Sismo '+str(masFPais[j+1])+' en '+masFPais[j])

print('\n')

#req5
masFPais=ordenarMenor(MinList)
print('Los sismos menos fuertes del país fueron:')
for j in range(0,6,2):
    print('Sismo '+str(masFPais[j+1])+' en '+masFPais[j])

#req6
ct=0; nonRepeat=[]; avg=0
for i in range(len(CityNoRepeat)):
    c=0; holder=0
    for j in range(len(Ciudad)):
        if(CityNoRepeat[i]==Ciudad[j]):
            ct+=1; c+=1
            addNR(nonRepeat,CityNoRepeat[i])
            holder+=intensGMercalli[j]
    nonRepeat.append(holder*c/100)

print("Cantidad total de sismos analizados: "+str(ct))
print("El promedio de sismos por ciudad es: ")
for i in range(0,len(nonRepeat),2):
    print(str(round(nonRepeat[i+1],2))+' en '+nonRepeat[i])

#Beaten @ 01:12:48


#debug
#print(CityNoRepeat); print(Ciudad)