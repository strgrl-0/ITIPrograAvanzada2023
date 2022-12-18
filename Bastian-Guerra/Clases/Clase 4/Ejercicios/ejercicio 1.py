"""
Bastian Guerra Valdes,ITI
"""

mayor = -1
menor = 10*10
cont = 0
numero = 0
total = 0

archivo = open("edades.txt","r", encoding = "utf-8")
linea = archivo.readline().strip()
while linea != "":
    cont += 1
    linea = int(linea)
    numero = linea
    total = total + numero
    linea = archivo.readline().strip()
    print(linea)
        
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print("El total es: ",total)
print("El numero mayor es: ",mayor)
print("El numero menor es:" ,menor)
print("El promedio es: ",total/cont)
