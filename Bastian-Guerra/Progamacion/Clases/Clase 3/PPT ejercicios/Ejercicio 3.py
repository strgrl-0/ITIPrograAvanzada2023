"""
Bastian Guerra Valdes,ITI,Clase 3, Ejercicio 3
"""
print("¿Progamacion o Progamacion avanzada?")
menu = input("Ingrese asignatura: ").lower()
c_alumnos_proga = 0
c_notas_proga = 0
c_alumnos_progaav = 0
c_notas_progaav = 0

if menu == "progamacion" or menu == "progamacion avanzada":
    while menu  != "salir":
        if menu == "progamacion":
            print("¿Donde desea ingresar o salir?  (asistencia, promedio final, salir)")
            op = input("Ingrese opcion: ").lower()
            if op == "salir":
                menu = "salir"
            if op == "asistencia":
                clases_si = int(input("Ingrese las clases asistidas: "))
                clases_no = int(input("Ingrese las clases no asistidas: "))
                total_clases = clases_si + clases_no
                pro_asis = total_clases / 2
                c_alumnos_proga += 1 
            elif op == "promedio final":
                salir_pro = ""
                while salir_pro != "salir" :
                    n1 = float(input("Ingrese la primera nota: "))
                    n2 = float(input("Ingrese la segunda nota: "))
                    n3 = float(input("Ingrese la tercera nota: "))
                    if ((n1 < 1 or n1 > 7) or (n2 < 1 or n2 > 7)  or (n3 < 1 or n3 > 7)):
                        print("Uno de los numeros fue mal ingresado, ingresalos nuevamente: ")
                        n1 = float(input("Ingrese la primera nota: "))
                        n2 = float(input("Ingrese la segunda nota: "))
                        n3 = float(input("Ingrese la tercera nota: "))
                        pro_notas = (n1 + n2 + n3) / 3
                        print("Promedio final de notas: ",pro_notas)
                        c_notas_proga += 1
                        salir_pro = input("¿Desea salir? (si/no)").lower()
                        if salir_pro == "si" :
                            salir_pro = "salir"
                        else: salir_pro = ""
                    else:
                        pro_notas = (n1 + n2 + n3) / 3
                        print("Promedio final de notas: ",pro_notas)
                        c_notas_proga += 1
                        salir_pro = input("¿Desea salir? (si/no)").lower()
                        if salir_pro == "si" :
                           salir_pro = "salir"
                        else: salir_pro = ""
        elif menu == "progamacion avanzada":
            print("¿Donde desea ingresar o salir?  (asistencia, promedio final, salir)")
            op = input("Ingrese opcion: ").lower()
            if op == "salir":
                menu = "salir"
            if op == "asistencia":
                clases_si = int(input("Ingrese las clases asistidas: "))
                clases_no = int(input("Ingrese las clases no asistidas: "))
                total_clases = clases_si + clases_no
                pro_asis = total_clases / 2
                c_alumnos_progaav += 1 
            elif op == "promedio final":
                salir_pro = ""
                while salir_pro != "salir" :
                    n1 = float(input("Ingrese la primera nota: "))
                    n2 = float(input("Ingrese la segunda nota: "))
                    n3 = float(input("Ingrese la tercera nota: "))
                    if ((n1 < 1 or n1 > 7) or (n2 < 1 or n2 > 7)  or (n3 < 1 or n3 > 7)):
                        print("Uno de los numeros fue mal ingresado, ingresalos nuevamente: ")
                        n1 = float(input("Ingrese la primera nota: "))
                        n2 = float(input("Ingrese la segunda nota: "))
                        n3 = float(input("Ingrese la tercera nota: "))
                        pro_notas = (n1 + n2 + n3) / 3
                        print("Promedio final de notas: ",pro_notas)
                        c_notas_progaav += 1
                        salir_pro = input("¿Desea salir? (si/no)").lower()
                        if salir_pro == "si" :
                            salir_pro = "salir"
                        else: salir_pro = ""
                    else:
                        pro_notas = (n1 + n2 + n3) / 3
                        print("Promedio final de notas: ",pro_notas)
                        c_notas_progaav += 1
                        salir_pro = input("¿Desea salir? (si/no)").lower()
                        if salir_pro == "si" :
                           salir_pro = "salir"
                        else: salir_pro = ""
    print("Cantidad de alumnos consultados en progamacion, promedio asistencia: ",c_alumnos_proga)
    print("Cantidad de alumnos consultados en progamacion, promedio final: ",c_notas_proga)
    print("Cantidad de alumnos consultados en progamacion avanzada, promedio asistencia: ",c_alumnos_progaav)
    print("Cantidad de alumnos consultados en progamacion avanzada, promedio final: ",c_notas_progaav)
else:
    print("Error, valor no ingresado correctamente")


