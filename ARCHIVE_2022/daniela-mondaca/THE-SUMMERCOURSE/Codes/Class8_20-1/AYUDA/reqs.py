file=open('aleatorios.txt','r')
line=file.readline().strip()

#lists
name=[]; age=[]

while(line!=''):
    split=line.split(',')
    name.append(split[0]); age.append(int(split[1]))
    line=file.readline().strip()
    
print(str(name)+'\n')
print(age)

def NameToID(name):
    j=0; IDs=[]
    for i in range(len(name)): 
        IDs.append(j)
        j+=1
    return(IDs)

def mintomax(numbers):
    mintomax=[]; mintomax.append(numbers)
    for i in range(len(mintomax)-1):
        for j in range(i+1,len(mintomax)):
            if(mintomax[i]<mintomax[j]):
                aux=mintomax[i]
                mintomax[i]=mintomax[j]
                mintomax[j]=aux 
                
            
    return(mintomax)
IDs=NameToID(name)
print(IDs)

mtmax=mintomax(age)
print('\n')
print(mtmax)
    