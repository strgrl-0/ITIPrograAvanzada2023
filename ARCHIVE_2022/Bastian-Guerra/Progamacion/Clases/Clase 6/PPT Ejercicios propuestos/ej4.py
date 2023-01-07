"""
PPT Ejercicios propuestos, ej4
Numero primo, retornas true o false.
"""

def esPrimo(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
        return True
    
    
num = int(input("Ingrese numero a evaluar: "))
resultado = esPrimo(num)
print(resultado)