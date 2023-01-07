"Falta añadir sacar porcentaje de n datos"


#Datos a pedir 
print("Ingrese en el nombre " + "fin" + " para finalizar")
nombre = input("Ingrese nombre del alumno:")

#Variables
alumno = 0
bp = 0
n = 0
po = 0
o = 0

while nombre != "fin":
    edad = int(input("Ingrese edad del alumno:"))
    estatura = float(input("Ingrese estatura del alumno(metros):"))
    peso = float(input("Ingrese peso del alumno(kilos):"))
    alumno = alumno + 1

    imc = (peso / (estatura ** 2))

    if imc < 18.50:
        print("Bajo peso")
        bp = bp + 1
    elif imc >= 18.50 and imc < 25:
        print("normal") 
        n = n + 1
    elif imc >= 25 and imc < 30:
        print("Preobeso") 
        po = po + 1
    elif imc >= 30:
        print("Obeso")
        o = o + 1

    nombre = input("Ingrese nombre del alumno:")

print("Total alumnos: ",alumno)
print("Total bajo peso: ",bp)
print("Total normal: ",n)
print("Total preobeso: ",po)
print("Total sobrepeso: ",o)


    

