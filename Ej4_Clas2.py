#Program 4, class 2
#Global Capture
CAPT=[]
a=int(0)


#Data capture
def askcat():
    CATa=[]
    for i in range(3):
        global a
        nota=str("Nota catedra ")
        CATa.insert(i,float(input(nota+str(i)+'\n')))
        CAPT.insert(a,CATa[i])
        a=a+1
        #CAPT 0-2 = cat values


def catSH():
    catSHH=[]
    for i in range(2):
        global a 
        nota=str("Nota prueba corta ")
        catSHH.insert(i,float(input(nota+str(i)+'\n')))
        CAPT.insert(a,catSHH[i])
        a=a+1
        #CAPT 3-4 = catSH

def WRKSHP():
    Wrk=[]
    for i in range(1):
        nota=str("Nota taller")
        Wrk.insert(i,float(input(nota+'\n')))
        CAPT.insert(a,Wrk[i])
        alumni=int(input("Numero de alumnos taller"+'\n'))

        if (alumni) in range(2,4):
            if (alumni==2):

                if(Wrk[i]==6.8):
                    Wrk.insert(i, Wrk[i]+0.2)
                    CAPT.insert(a,Wrk[i])

                elif(Wrk[i]==6.9):
                    Wrk.insert(i, Wrk[i]+0.1)
                    CAPT.insert(a,Wrk[i])


                elif(Wrk[i]>=7):    
                    pass

                else:
                    Wrk.insert(i, Wrk[i]+0.3)
                    CAPT.insert(a,Wrk[i])
                        
            elif (alumni==3):
                        
                Wrk.insert(i, Wrk[i]+0.3)
                CAPT.insert(a,Wrk[i])
        else:
                print("El numero ingresado no es valido")
                

            #CAPT 5 = wrkshp.grade, bonus



#Processing
def CATpr():
    catSHavr=float(((CAPT[3]+CAPT[4])/2)*0.1)
    CATavr=float() #CAT grade
    mlt=[0.2, 0.3, 0.4]
    for i in range(3):
        Cont=float(CAPT[i]*mlt[i])
        CATavr=Cont+CATavr
    CATavr=CATavr+catSHavr
    CAPT.insert(6, CATavr) #grade strge
    

#RecEx func
def ExREC():
        RCG=float(input("Nota examen de recalificaion: "+'\n'))
        if (RCG>=3.96):
            print("Calificado con nota: 4.0")
        else:
            print("Reprobado con nota: "+str(RCG)+'\n')

#decimal list creation
def RCval():
    global val; val=[]; i=float(3.56)
    while(len(val)<41):
        val.append(i)
        i=i+0.01

#check if in RecEx range
def chck():
    for i in range(40):
        if(round(ACG,2)==round(val[i],2)):
            ExREC()


    

#////////EXECUTION


askcat()
catSH()
WRKSHP()
CATpr()

#AC
ACG=float(CAPT[5]*0.3 + CAPT[6]*0.7)

RCval()
chck()


#Check if pass
if (ACG<3.56):
    print("No aprueba, calificacion: "+str(ACG)+'\n')
elif(ACG>3.95):
    print("Aprueba con calificacion: "+str(ACG)+'\n')