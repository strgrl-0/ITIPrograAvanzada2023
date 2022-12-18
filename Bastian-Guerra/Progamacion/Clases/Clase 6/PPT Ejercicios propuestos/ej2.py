"""
PPT Ejercicios propuestos, ej2
Desplegar la suma total de los datos de distancia
"""

def entre(uno,dos):
    suma = 0
    c = 0
    restar = 0

    arch = open("rangos.txt","r")
    linea = arch.readline().strip()
    partes = linea.split(",")
    uno = int(partes[0])
    dos = int(partes[1])

    while linea != "":
        restar += 1
        partes = linea.split(",")
        uno = int(partes[0])
        dos = int(partes[1])
        for i in range(uno,dos):
            if i > 0:
                c = 0
                c += 1
                suma = (suma + c) 
        linea = arch.readline().strip()
    resultado = suma - restar
    return resultado

arch = open("rangos.txt","r")
linea = arch.readline().strip()
partes = linea.split(",")
uno = int(partes[0])
dos = int(partes[1])
while linea != "":
    partes = linea.split(",")
    uno = int(partes[0])
    dos = int(partes[1])
    linea = arch.readline().strip()

resultado = entre(uno,dos)
print(resultado)


