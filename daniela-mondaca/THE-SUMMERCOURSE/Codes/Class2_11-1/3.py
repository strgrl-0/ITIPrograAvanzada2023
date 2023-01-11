ii=False;prom=0
for i in range(5):
    inp=int(input("Ingresa"+'\n'))
    if(inp<0):
        print("No se puede calcular el promedio")
        ii=True
        break
    prom+=inp

print("El promedio es "+str(prom/5))
