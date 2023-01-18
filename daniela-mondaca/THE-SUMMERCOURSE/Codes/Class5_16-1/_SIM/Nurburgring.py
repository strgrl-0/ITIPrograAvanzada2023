arch=open('nurburgring.txt','r')
line=arch.readline().strip()

#vars

Empresa='';CantidadModelos=0;FundadaEn=0;Pais=''
NombreModelo='';Minutos=0.0;Segundos=0.0;Year=0

print1=False
#counters
FastestEnterpriseModel=float(0); initFastest=9999

FastestComp2=float(0); initFast2=9999

initslow=-1; slowestOf2018=0

avgTCount=0; avgSPD=0; avgTSum=0; avgT=0

CarsTotal720=0; CarsUnder720=0

#printers
empresaP=''; countryP=''; fastest_modelP=''; timeP=0.0; yrP=0

FastestOA=''; empFOA=''; timeFOA=0.0

S2018model=''; S2018Brand=''; S2018Time=0




while(line!=''):
    split1=line.split(',');split2=line.split(';')
    if(',' in line):
        EmpresaS=split1[0];CantidadModelos=split1[1];FundadaEn=split1[2];Pais=split1[3] 
        
        FastestEnterpriseModel=float(0); initFastest=9999
        
        if(print1==True):
            print(empresaP+"("+countryP+") con "+fastest_modelP+" con tiempo "+str(timeP)+" en "+str(yrP))
        
    elif(';'in line):
        NombreModelo=split2[0];Minutos=float(split2[1]);Segundos=float(split2[2]);Year=int(split2[3])
        
        timeCount=Minutos*60+Segundos;  FastestEnterpriseModel=timeCount; FastestComp2=timeCount; slowestOf2018=timeCount  
        
        #performance enterprises
        if(FastestEnterpriseModel<initFastest):
            initFastest=FastestEnterpriseModel
            empresaP=EmpresaS; countryP=Pais; fastest_modelP=NombreModelo; timeP=timeCount;yrP=Year
            print1=True
        #fastest of all
        if(FastestComp2<initFast2):
            initFast2=FastestComp2
            FastestOA=NombreModelo; empFOA=EmpresaS; timeFOA=timeCount
            
        #slowest of 2018
        if(slowestOf2018>initslow and Year=='2018'):
            initslow=slowestOf2018
            S2018model=NombreModelo; S2018Brand=EmpresaS; S2018Time=timeCount
            
        #avgtime
        avgTCount+=1; avgTSum+=timeCount
        
        #lowerthan720, over 2010
        if(Year>=2010 and timeCount<440):
            CarsUnder720+=1
            CarsTotal720+=1
        elif(Year>=2010):    
            CarsTotal720+=1
            
    line=arch.readline().strip()


#Avg speed calculation
avgT=round(avgTSum/avgTCount,2); avgT2=avgT
avgT2=avgT2/3600; avgT2=avgT2*1000
avgSPD=round(20600/avgT2,2)
#calculate 720 prcnt
prcnt720=0.0
prcnt720=CarsUnder720/CarsTotal720*100
#lastprint
print(empresaP+"("+countryP+") con "+fastest_modelP+" con tiempo "+str(timeP)+" en "+str(yrP))
print("2) El mas rapido es "+FastestOA+" de "+empFOA+" con un tiempo de ",str(timeFOA)+" segundos")
print("3) El mas lento del 2018 es "+S2018model+" de "+S2018Brand+" con un tiempo de "+str(S2018Time)+" Segundos")
print("4) La velocidad promedio corresponde a "+str(avgSPD)+" km/h considerando un tiempo promedio de "+str(avgT))
print("5) El porcentaje de autos con tiempos inferiores a 7 minutos 20 segundos desde 2010 es "+str(prcnt720))