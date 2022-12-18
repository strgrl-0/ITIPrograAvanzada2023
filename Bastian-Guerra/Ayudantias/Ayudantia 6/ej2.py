"""
Ayudantia 6,ej2
#Problema:
Utilizando funciones cree un programa que, dado un archivo llamado texto.txt, imprima
por pantalla el siguiente cálculo:
"""
def leer(archivo):
    arch = open(archivo,"r",encoding = "utf-8")
    linea = arch.readline().strip()
    
    texto = ""
    
    while linea != '':
        for i in linea:
            texto = texto + str(i)
        linea = arch.readline().strip()
    return texto
    
def calculo(texto):
    ce = 0
    cp = 0
    cc = 0
    clam = 0
    clom = 0

    for i in texto:
        if i == " ":
            ce += 1
        if i == ".":
            cp += 1
        if i == ",":
            cc += 1
        if i == "a":
            clam += 1
        if i == "o":
            clom += 1 
    
    if cc == 0 or clom == 0:
        print("error")
    else:
        operatoria = ce * (cp / cc) + (clam / clom)
        print(round(operatoria,2))
        
texto = leer("texto.txt")
calculo(texto)