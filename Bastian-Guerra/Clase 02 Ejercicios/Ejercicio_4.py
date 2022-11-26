"""
Bastian Guerra Valdes, Clase 2, Ejercio 4, ITI.
"""
"""
Usando las reglas de evaluación de la asignatura (diapositiva siguiente), escribe un programa que pregunte:
Las notas de las 3 pruebas
Las notas de 2 evaluaciones cortas (supongamos que en el semestre solamente se tomarán 2 pruebas cortas)
Las nota de taller y la cantidad de alumnos.
Con esos datos, calcula la nota final de la asignatura. Obviamente, si la nota no le alcanza para aprobar directamente, pero sí para el examen recuperativo, pregunta dicha nota antes de indicar si aprobó finalmente la asignatura o no.
Si el taller fue realizado en parejas, bonificar la nota de taller en 0,3 decimas.
"""

pru_1 = float(input("Ingrese la primera nota: "))
pru_2 = float(input("Ingrese la segunda nota: "))
pru_3 = float(input("Ingrese la tercera nota: "))
eva_01 = float(input("Ingrese la nota de la primera evaulacion: "))
eva_02 = float(input("Ingrese la nota de la segunda evaulacion: "))
tall = float(input("Ingrese nota del taller: "))
alum_tall = float(input("Ingrese la cantidad de alumnos del taller: "))

"""Pc = promedio notas catedra //  NC = promedio notas con las cortas"""
pc = ((eva_01 + eva_02) / 2) 
nc = ((pru_1 * 0.2) + (pru_2 * 0.3) + (pru_3 * 0.4) + (pc * 0.1))
nfa = float(0)
exrec_cat = 0
rec_tall = 0
a = 0
b = 0
c = 0
z = 0
x = 0


"""Acumulacion de decimas si se tiene 2 estudiantes en el taller"""
if alum_tall < 2 or alum_tall > 3:
    print("No alcanza el minimo de integrantes o excede el maximo de integrantes")
    tall = float(1.0)
else:
    if alum_tall == 2 : 
        tall = float(tall + 0.3)
        print("El numero de integrantes de taller es de 2, se le agregan 0.3 decimas")

"""Si el usuario se va a examen de recalificacion o no, aprobando catedra"""

if nc >= 4:
    print("Paso sin necesidad de examen en catedra, queda con promedio en catedra:",nc)
    nfc = nc
    a = 1
else:
    if nc >= 3.50 and nc <= 3.94:
        print("Se va a recalificación en catedra")
        rec_cat = float(input("Nota de recalificacion en catedra: "))
        exrec_cat = float(rec_cat)
    if exrec_cat >= float(4.0):
            print("Paso el examen de recalificacion, queda con promedio en catedra:",exrec_cat)
            nfc_ = float((exrec_cat))
            a = 1
            c = 1
    else:
            print("No alcanzo la nota para pasar el examen en catedra, su promedio fue:",exrec_cat) 
            z = 1   

"""Si el usuario aprueba taller"""

if tall >= 4:
    print("Paso sin necesidad de examen en taller, queda con promedio en taller:",tall)
    b = 1
else:
    if tall >= 3.50 and tall <= 3.94:
        print("Se va a recalificacion en taller")
        rec_tall = float(input("Nota de recalificacion en taller: "))
        tall = float((rec_tall))
    if tall >= float(4.0):
            print("Paso el examen de recalificacion en el taller, queda con promedio en taller:",tall)
            b = 1
    else:
            print("No alcanzo la nota para pasar el examen en taller, su promedio fue:",tall)    
            x = 1

"""Si no se va a examen de recalificacion en catedra y taller, calcula el promedio final"""
if c == 0 :
    nfc = nc
else:
    nfc = nfc_

if a == 1 and b == 1:
    print("Usted aprobo tanto catedra como el taller")
    print("Su promedio fue de catedra fue:",nfc)
    print("Su promedio fue de taller fue:",tall)
    nfa = ((nfc * 0.7) + (tall * 0.3))
    print("Su promedio final es:",nfa)
else:
    if x == 1 or z == 1:
        print("No cumple con el requisito minimo de haber aprobado catedra y taller al mismo tiempo")




    
    
    




   

