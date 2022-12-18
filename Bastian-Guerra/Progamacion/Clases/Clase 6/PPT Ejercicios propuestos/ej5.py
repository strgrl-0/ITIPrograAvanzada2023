"""
PPT Ejercicios propuestos, ej5
"n" como parametro, calcule nuevo "n":
    n es par, n = n/2
    n es impar, n = 3n+1
    Repita el proceso hasta que “n” sea igual a 1 y retorne la cantidad de 
    iteraciones que hubo que realizar hasta llegar a “1”.
"""

def nuevo(n): 
    while n != 1:
      #Par
      if (n / 2) == 1 or (n / 2) == -1:
          n = n/2
          return "El numero ingresado es par, el nuevo numero generado es:",n
      #Impar
      if (n / 2) > 1 or (n / 2) < -1:
          n = (3 * n) + 1
          return "El numero ingresado es impar, el nuevo numero generado es:",n

def uno(n):
    c = 0
    while n != 1:
        #Hasta que n == 1
        while n < 1:
             n += 1
             c += 1
        while n > 1:
             n -= 1
             c += 1
        return "Cantidad iteraciones",c
         
n = int(input("Ingrese numero: "))
par_impar = nuevo(n)
iteraciones = uno(n)
print(par_impar,iteraciones)
