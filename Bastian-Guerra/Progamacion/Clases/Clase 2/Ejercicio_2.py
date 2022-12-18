"""
Bastian Guerra Valdes, Clase 2, Ejercio 2, ITI.
"""
"""
Escribe un programa que pregunte por dos números y que realice lo siguiente:
Que diga si la división entre el valor 1 y el valor 2 es entera, en caso contrario que entregue el resto.
Si la división se indetermina, mostrar mensaje de error.
Que muestre cual de los valores es mayor, cual es menor o que muestre si son iguales.
Que diga si el mayor es múltiplo del menor
"""

print("--------------------------")
print("Ingrese dos números:")
print("--------------------------")
"""Datos a ingresar"""
print("--------------------------")
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
print("--------------------------")
if b == 0:
    """Mensaje de error"""
    print("--------------------------")
    print("El valor es indeterminado")
    print("--------------------------")
else:
    """Operaciones"""
    div = a / b
    res = a % b
    div_ent = a // b
    if div == div_ent:
        print("--------------------------")
        print("La división es entera:",int(div))
        print("--------------------------")
    else:
        print("La división no es entera, el resto es:" , res)
        print("--------------------------")
    if a > b :
        print("El primer valor es mayor", a)
        print("--------------------------")
    else:
        print("El segundo valor es mayor", a)
        print("--------------------------")
    if a == b :
        print("Ambos valores son iguales", "El primer número ingresado es:",a,"Y el segundo número ingresado es:",b)
        print("--------------------------")
    if res == 0:
        print("El número mayor es multiplo del menor")
        print("--------------------------")
    else:
        print("El número mayor no es multiplo del menor")
        print("--------------------------")
        
        


    
    
    