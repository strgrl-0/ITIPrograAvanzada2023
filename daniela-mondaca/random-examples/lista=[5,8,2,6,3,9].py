lista=[5,8,2,6,3,9]
print(lista)

for a in range(len(lista)-1): #a en longitd lista -1 (5)a:0, rango: 0,5. a:1, rango: 1,5
    print(str(a)+'\n')
    for b in range(a+1,len(lista)): #b:1, rango: 2, 6
        print(b)
        print(lista[a], lista[b])
        if lista[a]>lista[b]:#0, 0, nada.
            aux=lista[a]
            lista[a]=lista[b]
            lista[b]=aux
            print(lista[a], lista[b], aux)

print(lista)