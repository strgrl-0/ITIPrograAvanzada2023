"""
Bastian Guerra Valdes, Clase 2, Ejercio 4, ITI.
"""
"""
Pregunta por un numero y realiza las siguientes operaciones:
Si el numero es positivo, súmale 3 veces su valor. De lo contrario réstale 2 veces la mitad de su valor.
Si el numero es impar, mayor que 25 o menor que -10, multiplícalo además por 4 e imprime por pantalla “Impar”. De lo contrario divídelo en 3 e imprime “Quizá es Par”.
Si el numero original es mayor que el ultimo resultado intercambia los valores de las variables e imprímelas.
Si el numero es cero, imprime “Fin”.
"""

num_ori = float(input("Ingresa un numero: "))
num = num_ori
par = num % 2
a = 0
b = 0
c = 0
x4 = 0
div_3 = 0
div_2 = 0


if num_ori == 0 :
    print("Fin")
else:
    if num > 0 :
        x3 = float(num * 3)
        print(x3)
        num = x3
    else:
        div_2 = float(num / 2)
        mul = float(div_2 * 2)
        res = float((num) + (mul))
        print(res)
        num = res
  

    if par == 0 or num > 25 or num < -10:
        x4 = float(num * 4)
        print("Impar")
        num = x4
    else:
        div_3 = float(num / 3)
        print("Quizá es par")
        num = div_3

    if num_ori > num:
        a = num_ori
        b = x4
        x4 = a
        num_ori = b
        print("Numero original:",x4)
        print("Numero final:",num_ori)

    if num_ori > num:
        a = num_ori
        c = div_3
        div_3 = a
        num_ori = c
        print(div_3)
        print(num)




