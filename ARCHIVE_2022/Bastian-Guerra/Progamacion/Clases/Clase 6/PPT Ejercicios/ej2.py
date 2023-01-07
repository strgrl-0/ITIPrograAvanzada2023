"""
Clase 06 Ejercicios, ej2
"""
#Arreglar for suma  y mul

def entre(n1,n2,som):
    suma = 0
    multiplicacion = 0
    if som == "suma":
        for i in range (n1,n2):
            suma = n1 + n2
        return suma
    if som == "multiplicacion":
        for i in range (n1,n2):
            multiplicacion = n1 * n2
            return multiplicacion
            
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
som = input("Ingrese accion a realizar (suma o multiplicacion): ")
while som != "suma" and som != "multiplicacion":
    som = input("Error,ingrese el tipo de accion nuevamente(suma o multiplicacion): ")

resultado = entre(n1,n2,som)
print("El resultado de los datos ingresado entre",n1,"y",n2,"es",resultado,"realizando",som)
