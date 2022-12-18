menor = 500
x = float(input("Ingrese un numero: "))

"""
Si se ingresan los numeros 4,5,1 y 0 el resultado arroja 0 tanto de orden izquierda-derecha
como derecha-izquierda
Si se ingresa como primer valor -1 imprime 500
Si se ingresa 100,1000,700 imprime 100

"""

while x != -1:
    if x < menor:
        menor = x
    else:
        x = float(input("Ingrese un numero: "))
else:
    print("no se puede calcular el numero mayor")
    print(menor)
