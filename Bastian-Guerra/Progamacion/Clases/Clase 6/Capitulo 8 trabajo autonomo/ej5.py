"""
Ejercicios libro guia Capitulo 8 ,ej 1
"""

def ingresarNumero(num):
    return num

def procesar(n):
    if (n / 7) == 1 or (n / 7) == -1 :
        return True
    elif (n / 7) > 1 or (n / 7) < -1 :
        return False

def escribirResultado(r):
    r = str(r)
    return r

#Desde aca llamamos a las funciones de arriba
def main():
    n = ingresarNumero(num)
    r = procesar(n)
    escribirResultado(r)


num = int(input("Ingresa numero para evaularlo en el parametro ingresarNumero: "))
n = int(input("Ingresa numero para evaularlo en el parametro n: "))
r = int(input("Ingresa numero para evaularlo en el parametro r: "))
resultado_numero = ingresarNumero(num) #IngresarNumero
procesar_numero = procesar(n) #Procesar
main()
print("Devolver numero en el parametro num",resultado_numero)
print("El numero ingresado es divisible por 7",procesar_numero)
