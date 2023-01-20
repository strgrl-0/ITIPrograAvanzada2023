import os
import random
archivo=open('aleatorios.txt','w')
lista_aleatorios=[]

nombres = ['Juan','Felipe','Catalina','Hernan','Marcelo','Rodrigo','Maria','Pedro','Nicolas','Bastian','Raul','Gato','Perro','Samantha','Copito','Fergus','Daniela','Gabriel','Amelia','Victor','Sebastian']
total=len(nombres)-1
print(len(nombres))
for i in range(1,len(nombres)):
  i=random.randint(1,20)
  lista_aleatorios.append(i)
  
  nombre = nombres[random.randint(0,total)]
  archivo.write(f"{nombre},{str(i)}\n")
  nombres.remove(nombre)
  total-=1
archivo.close()
print(lista_aleatorios)