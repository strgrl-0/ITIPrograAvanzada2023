"""
PPT Ejercicios propuestos, ej1
calcular factorial de un numero con una funcion
"""
def factorial(num):
    if num < 0:
            print("El numero factorial no puede ser menor que 0")
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact
    
num = int(input("Ingrese numero: "))
resultado = factorial(num)
print(resultado)
        