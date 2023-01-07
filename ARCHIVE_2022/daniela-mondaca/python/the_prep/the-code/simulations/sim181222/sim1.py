import numpy as np #import np

####ADD
def add(list,elm):
    list.append(elm)
    return list.index(elm)

####ADDIFNT
def addifnt(list,elm):
    if not elm in list:
        list.append(elm)
    return list.index(elm)

#####LISTS

#-RAW cAPTURE
CiudadA1=[]; CiudadA2=[]; dst=[]

CiudadB1=[]; CiudadB2=[]; query=[]

#FILTERED
CiudadFTOT=[]

#-NUM IDS
IDCiudadA1=[]; IDCiudadA2=[]

IDCiudadB1=[]; IDCiudadB2=[]

#-Ciudad connections
IDCiudadAs=[IDCiudadA1,IDCiudadA2]; IDCiudadBs=[IDCiudadB1,IDCiudadB2]

IDCiudadGEN=[IDCiudadAs,IDCiudadBs]

CiudadAs=[CiudadA1,CiudadA2]; CiudadBs=[CiudadB1,CiudadB2]

CiudadGEN=[CiudadAs,CiudadBs]

def toNUMid(dict,input,output):
        for j in range(len(dict)):
            for i in range(len(input)):
                if dict[j]==input[i]:
                    add(output,j)
                

for i in range (2):
    files=["dist.txt","query.txt"]
    arch=open(files[i],"r")
    readline=arch.readline().strip()
    
    while readline!="":
        spl=readline.split(",")
        cities1=[CiudadA1,CiudadB1]; cities2=[CiudadA2,CiudadB2]; qorDST=[dst,query]

        #cities1[i]=spl[0]; cities2[i]=spl[1]; qorDST[i]=spl[2]
        add(cities1[i],spl[0]); add(cities2[i],spl[1]); add(qorDST[i],spl[2])
        readline=arch.readline().strip()

for i in range(len(CiudadGEN)):
    for f in range(len(CiudadGEN)):
        for j in range(len(CiudadGEN[i][f])):
            addifnt(CiudadFTOT,CiudadGEN[i][f][j])



#to NUM
for i in range(2):
    toNUMid(CiudadFTOT,CiudadAs[i],IDCiudadAs[i])
    toNUMid(CiudadFTOT,CiudadBs[i],IDCiudadBs[i])

#toArr
Arr0=np.zeros([3,len(CiudadA1)])
Arr1=np.zeros([3,len(CiudadA2)])

#fill
Arrs=[Arr0,Arr1]

for i in range(2):
    count=0
    for f in range(len(Arrs[i])):
        for c in range(5):
            Arrs[i][f][c]=1

print(Arr0,'\n','\n',Arr1,'\n')
print(CiudadFTOT)
print(IDCiudadAs,IDCiudadBs)
print(CiudadAs,'\n',CiudadBs)