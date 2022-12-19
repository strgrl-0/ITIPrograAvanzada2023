#import numpy
import numpy as np


#not in use


#not in use, debugging purposes
'''
def prtlst():
    print(len(drv))
    for i in range(len(drv)):
        print(drv[i])
    print(len(car))
    for i in range(len(car)):
        print(car[i])
    print(len(km))
    for i in range(len(km)):
        print(km[i])
'''
#filter repeated elements (cars, names)
def addifnt(list, elm):
    if not elm in list:
        list.append(elm)
    return list.index(elm)

#access and arr creation
def detmtx():
    arch = open('drivers.txt', 'r', encoding='utf-8')
    crtmtr = arch.readline().strip(); fil = 0; 
    while crtmtr != '':
        crtmtr=arch.readline().strip()
        splt=crtmtr.split(";")
        if fil==0:
            col=len(splt)
        fil=fil+1
    mtx=np.zeros([fil,col],dtype='U25')
    arch.close()
    return(mtx, fil, col)

#list append function
def add(list, elm):
    list.append(elm)
    return list.index(elm)

#post list processing array filling
def farray(x):
    for fil in range(row):
        if x == 0:
            mtx[fil][x]=drv[fil]
        elif x == 1:
            mtx[fil][x]=car[fil]
        elif x == 2:
            mtx[fil][x]=km[fil]





#exec
drv = []
car = []
km = []
mtx, row, clmn=detmtx()


arch = open("drivers.txt", "r")
linea = arch.readline().strip()
while linea != "":
    partes = linea.split(";")
    drvs = partes[0]
    cars = partes[1]
    kms = int(partes[2])
    add(drv,drvs); add(car,cars); add(km,kms)
    linea = arch.readline().strip()

for col1 in range(clmn):
    farray(col1)

def mostused():
    max=0
    maxfreq=0
    for fil in range(row):
        c=0
        for i in range(row):
            if(mtx[fil][1]==mtx[i][1]):
                c+=1
        if c > max:
            max=c
            maxfreq=mtx[fil][1]
    return(maxfreq)

def mostkmsd():
    drvslt=[]
    for fil in range(row):
        addifnt(drvslt, mtx[fil][0])

    max=0
    driver=str
   
    for fil in range(len(drvslt)):
        mkms=0
        for i in range(row):
            if drvslt[fil]==mtx[i][0]:
                mkms=mkms+int(mtx[i][2])
        if mkms>max:
            max=mkms
            driver=drvslt[fil]
    return(driver)



most=mostused()
mdrv=mostkmsd()

print(most, mdrv)
#prtlst()
#print(mtx)



    
    
    
    
#matrix creation