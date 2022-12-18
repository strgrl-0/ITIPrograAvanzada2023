"""
Bastian Guerra Valdés, ITI , Ejercicio 1 clase 3
"""


n = int(input("Ingresa un numero: "))
x = 1
c = 0

while x <= n:
    if n % x == 0:
        c = c + 1
    x = x + 1
if c == 2:
    print("Es numero ingresado ",n," es primo")
else:
    print("Es numero ingresado ",n," no es primo")
