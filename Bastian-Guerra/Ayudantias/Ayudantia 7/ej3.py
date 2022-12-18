"""
Ayudantia 7,j3
Cree un programa que declare tres arreglos: lista1, lista2, lista3 de cinco enteros cada
uno,para la lista1 y lista2 debe pedir que se ingresen los valores por teclado,
luego calcule lista3 = lista1+lista2.
"""

def agregar(lista,elemento):
    lista.append(elemento)
  
lista1 = []
lista2 = []
lista3 = []    
   
for i in range(5):
    print("Usted va a ingresar el elemento de la lista",i)
    n1 = int(input("Ingrese numero a ingresar a la lista 1: "))
    n2 = int(input("Ingrese numero a ingresar a la lista 2: "))
    agregar(lista1,n1)   
    agregar(lista2,n2)    
    n3 = n1 + n2
    agregar(lista3,n3)

print("El resultado de la lista3 = lista1 + lista2:",lista3)




