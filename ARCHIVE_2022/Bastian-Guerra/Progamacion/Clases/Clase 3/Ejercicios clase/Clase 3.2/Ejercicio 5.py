"""
Bastian Guerra Valdés, ITI
"""
"""
Si ingresamos los valores, imprime el valor de jose
Si se ingresa el valor -1 finaliza el progama
"""

mayor = -1
nombreM = ""
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
nombreM = nombre
mayor = edad

if edad == -1:
    print("no se puede calcular el numero mayor")
else:
    if nombre == "":
        print("No se a ingresado ningun valor") 
    else:
        while edad != -1:
            if edad > mayor:
                mayor = edad
                nombreM = nombre
            else:
                nombre = input("Ingrese nombre: ")
                edad = int(input("Ingrese edad: "))
        else:
            print("Se a finalizado la entrada de datos")
            print(nombreM)
