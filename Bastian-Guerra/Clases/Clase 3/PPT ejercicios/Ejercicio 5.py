"""
Bastian Guerra Valdés, ITI
"""


nota = 0
nota_mayor = 0
nota_menor = 0
nota_mayor_4 = 0
nota_menor_4 = 0
nombre = ""
total_notas = 0
pro_nota_mayor_4 = 0
pro_nota_menor_4 = 0
guardar_nota_mayor = 0
guardar_nota_menor = 0
guardar_nombre_mayor = ""
guardar_nombre_menor = ""
nombre = input("Ingrese nombre: ").upper()

while (nombre) != "FIN":
    nombre = input("Ingrese nombre: ").upper()
    nota = float(input("Ingrese nota: "))
    total_notas = total_notas + 1
    if nota >= 1 and nota <= 7:
        if nota >= 4.0:
            guardar_nota_mayor = nota
            guardar_nombre_mayor = nombre
            nota_mayor_4 = nota_mayor_4 + 1
            nota_mayor = nota_mayor + nota
            pro_nota_mayor_4 = nota_mayor / nota_mayor_4

        if nota >= guardar_nota_mayor:
            guardar_nota_mayor = nota
            guardar_nombre_mayor = nombre
        else:
            guardar_nota_menor = nota
            guardar_nombre_menor = nota
            nota_menor_4 = nota_menor_4 + 1
            nota_menor = nota_menor + nota
            pro_nota_menor_4 = nota_menor / nota_menor_4

        if nota <= guardar_nota_menor:
            guardar_nota_menor = nota
            guardar_nombre_menor = nombre
    else:
        print("La nota fue mal ingresada")
    

print("Total de notas ingresadas: ",total_notas)
print("Cantidad de notas mayores o iguales a 4.0: ",nota_mayor_4,"",pro_nota_mayor_4,"")
print("     La menor fue: ",guardar_nota_menor,"(",guardar_nombre_menor,")")
print("Cantidad de notas menores a 4.0: ",nota_menor_4,"",pro_nota_menor_4,"")
print("     La mayor fue: ",guardar_nota_mayor,"(",guardar_nombre_mayor,")")