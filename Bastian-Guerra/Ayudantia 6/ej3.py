"""
Ayudantia 6, ej3
"""
#Funciones
def pedirNumero(numero):
    numero = int(input("Ingrese numero a evaular: "))
    if numero == 0:
        return "Finalizar progama"
    else:
        return numero
   
def esPar(numero):
    if numero == 0 :
        return "El numero ingresado fue 0"
    elif numero % 2 == 0:
        return "El numero ingresado es par"
    else:
        return "El numero ingresado no es par"

def esPrimo(numero):
  for i in range(2,numero):
    if (numero % i) == 0:
      return False
  return True
 
#Variables
n = 1
#Solicitar datos
while n != 0:
    n = pedirNumero(n)
    par = esPar(n)
    print(par)
    primo = esPrimo(n)
    print(primo)
else:
    print("Finalizar")
    