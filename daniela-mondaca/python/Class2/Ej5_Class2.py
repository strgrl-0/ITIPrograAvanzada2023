#Class, Ej 5

num=int(input("Ingresa un número"+'\n'))
narr=[]
#evaluate even or uneven 
end=False
if (num==0):
    end = True



if (num>0):
    narr.insert(0, int(num*3+num))
else:
    narr.insert(0, int(num-num*2))

isPair=num%2
narr.insert(1,0)


######################################

if(isPair!=0):
    if (narr[0]>25):
        narr.insert(1, narr[1]*4)
        print("Impar")
    elif(narr[0]<-10):
        narr.insert(1, narr[1]*4)
        print("Impar")
else:
    narr.insert(1, narr[1]/3)
    print("Quiza es par")

if(num>narr[1]):
    narr.insert(2, narr[1])
    narr[1]=num
    num=narr[2]
    print(narr[1])
    print(num)
if(end==True):
    print("Fin")
