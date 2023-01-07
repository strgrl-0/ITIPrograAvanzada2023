"""
PPT Ejercicios propuestos, ej3
Pedir por teclado la cantidad de areas a calcular(Triangulo,rectangulo o circulo)
"""

def areas(figuras):
    c = 0
    for i in range(figuras):
       c+= 1
       pi = 3.14
       forma = input("Ingrese la figura a calcular area(Triangulo,rectangulo,circulo): ").lower()
       while forma != "triangulo" and forma != "circulo" and forma != "rectangulo":
           forma = input("Error,Ingrese forma nuevamente(Triangulo,rectangulo,circulo): ").lower()
       if forma == "triangulo":
           text_tri = "El area del triangulo es:"
           base_tri = float(input("Ingrese base triangulo: "))
           altura_tri = float(input("Ingrese altura triangulo: "))
           area_tri = (base_tri * altura_tri) / 2
           return  text_tri,area_tri
       if forma == "rectangulo":
           text_rec = "El area del rectangulo es:"
           base_rec = float(input("Ingrese base cuadrado: "))
           altura_rec = float(input("Ingrese altura cuadrado: "))
           area_rec = (base_rec * altura_rec) 
           return text_rec,area_rec
       if forma == "circulo":
           text_cir = "El area del circulo es"
           radio = float(input("Ingrese radio circulo: "))
           area_cir = pi * (radio * radio)
           return text_cir,area_cir
              
figuras = int(input("Ingrese la cantidad de figuras a sacar el area: "))
for i in range (figuras):
    re_fig = areas(figuras)
    print(re_fig)