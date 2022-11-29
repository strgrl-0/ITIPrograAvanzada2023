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

def ship(): 
    date=[]; zone=[]; amt=[]
    inStore=np.zeros([6,6]); sent=np.zeros([10,10])

    arch=open('recibidos.txt', 'r')
    rline=arch.readline().strip()

    while rline != '':
        spl=rline.split(';')
        when=spl[0]; cInStore=spl[1]; ammt=int(spl[2])
        add(date,when); add(zone,cInStore); add(amt,ammt)
        rline=arch.readline().strip()
        print("Se realiza un despacho en "+cInStore+" el "+when)
    return(date,zone,amt)

    

    