"""
Bastian Guerra Valdes,ITI
"""

arch = open("puntajes psu.txt", encoding = "utf-8")
linea = arch.readline().strip()

while linea != "": #Mientas la linea sea distinta de "" osea nada, lee lo que esta dentro del archivo
    partes = linea.split(",") #Separador entre los elementos 
    alumno = partes[0]
    universidad = partes[1]
    puntaje = int(partes[2])
    print(alumno, ",", universidad, ",", puntaje)
    linea= arch.readline().strip()

