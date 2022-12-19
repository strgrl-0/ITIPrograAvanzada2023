#requiere recibir la cantidad de entradas que se desean comprar y el tipo de entrada. debe retornar monto que se debe cancelaR por cada venta

def ventas(ticketa,tt):
    values=[20000, 30000, 40000, "Cancha", "Platea", "VIP", "cancha", "platea", "vip"] #index = 0,1,2; 3,4,5
    
    if tt == values[3]or values[6]:
        ticketp=ticketa*values[0]
    elif tt == values[4] or values[7]:
        ticketp=ticketa*values[1]
    elif tt == values[5] or values[8]:
        ticketp=ticketa*values[2]
    
    return(ticketp)

ticketa=int(input("Ingresa numero de tickets"+'\n')); tt=str(input("Ingresa tipo de ticket"+'\n'))
ticketp=ventas(ticketa,tt)
print(ticketp)