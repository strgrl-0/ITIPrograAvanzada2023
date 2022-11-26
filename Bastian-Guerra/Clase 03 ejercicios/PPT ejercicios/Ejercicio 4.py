"""
Bastian Guerra Valdés, ITI
"""
mayor = -1
nombreM = ""
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
nombreM = nombre
mayor = edad

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

    


