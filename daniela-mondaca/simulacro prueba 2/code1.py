#data format = y/m/d
#arrays = 6,6. 100,100.
#si una ubicación fuera a tener más de 100 items, se despachan inmediatamente 100 items, se conserva el excedente.



#import numpy
import numpy as np

def addifnt(list, elm):
    if not elm in list:
        list.append(elm)
    return list.index(elm)

def add(list, elm):
    list.append(elm)
    return list.index(elm)

def zAs(nStore):
    spls=nStore.split('-')
    zone=spls[0]; sector=spls[1]
    return(zone, sector)
        
        
    
def ship(): 
    date=[]; zone=[]; sector=[]; amt=[]
    inStore=np.zeros([6,6]); sent=np.zeros([10,10])

    arch=open('recibidos.txt', 'r')
    rline=arch.readline().strip()

    while rline != '':
        spl=rline.split(';')
        when=spl[0]; cInStore=spl[1]; ammt=int(spl[2])
        zoneR, sectorR=zAs(cInStore)
        add(date,when); add(zone,zoneR); add(sector,sectorR); add(amt,ammt)
        rline=arch.readline().strip()
    return(date,zone,sector,amt)

datext,zonext,sectext,amtext=ship()

print(datext,zonext,sectext,amtext)



    

    