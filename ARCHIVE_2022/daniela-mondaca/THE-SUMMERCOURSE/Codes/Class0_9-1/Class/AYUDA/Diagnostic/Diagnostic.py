import numpy as np

#read
arch=open("ciudades.txt","r")
line=arch.readline().strip()
    #lstArea
cities=[];citiesSel=[]


#selectiveappend
def selA(list,elm):
    if (elm not in list):
        list.append(elm)
        

while(line!=''):
    cities.append(line)
    selA(citiesSel,line)
    line=arch.readline().strip()
    
#req2-code
def cityCounter(cities_total,citiesUnrepeated):
    items=0
    for i in range(len(citiesUnrepeated)):
        items+=i
    cityCount=np.zeros([1,items])

    for i in range(len(citiesUnrepeated)):
        for j in range(len(cities_total)):
            if(citiesUnrepeated[i]==cities_total[j]):
                cityCount[0][i]=cityCount[0][i]+1
    #show
    for i in range(len(citiesUnrepeated)):
        print(str(citiesUnrepeated[i])+" tiene "+str(cityCount[0][i])+" reservas"+'\n')
    return cityCount
#req3 and 4-code
def mostNless(countMTX,cities_Unrepeated):
    max=0;current=0;count=0
    for j in range(len(countMTX)):
        current=countMTX[0][j]
        if current>max:
            max=current
            count=j
    print("La ciudad que mas se repite es "+str(cities_Unrepeated[count]))
            
    

##########EXEC area
#main block below
#req1
totalRSV=int(len(cities))
print("El total de reservas en el archivo es "+str(totalRSV)+'\n')
#req2-exec
cityCount=cityCounter(cities,citiesSel)
mostNless(cityCount,citiesSel)







########debug
#print(citiesSel)



