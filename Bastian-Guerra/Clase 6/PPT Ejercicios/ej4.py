"""
Clase 06 Ejercicios, ej4
"""

def total(pro):
    #Variables cantidad
    cant_toma = 0
    cant_cebo = 0
    cant_papas = 0
    cant_zana = 0
    cant_lechu = 0
    cant_beta = 0
    #Variables precios
    pre_toma = 0
    pre_cebo = 0
    pre_papas = 0
    pre_lechu = 0
    pre_beta = 0
    #Leer archivo
    arch_art = open("articulos.txt","r",encoding = "utf-8")
    linea_art = arch_art.readline().strip().lower()
    arch_pre = open("precios.txt","r",encoding = "utf-8")
    linea_pre = arch_pre.readline().strip().lower()
    
    while linea_art != "" and linea_pre != "":
        linea_art = arch_art.readline().strip().lower()
        linea_pre = arch_pre.readline().strip().lower()
        partes_art = linea_art.split(",")
        uno_art = partes_art[0]
        dos_art = partes_art[1]
        partes_pre = linea_pre.split(",")
        uno_pre = partes_pre[0]
        dos_pre = partes_pre[1]
        #Tomate
        if uno_art == "tomate":
            cant_toma = dos_art
        if uno_pre == "tomate":
            pre_toma = dos_pre
        #Zanahoria
        if uno_art == "zanahoria":
            cant_zana = dos_art
        if uno_pre == "zanahoria":
            pre_zana = dos_pre
        #Cebolla
        if uno_art == "cebolla":
            cant_cebo = dos_art
        if uno_pre == "cebolla":
            pre_cebo = dos_pre
        #Papas
        if uno_art == "papas":
            cant_papas = dos_art
        if uno_pre == "papas":
            pre_papas = dos_pre
        #Lechuga
        if uno_art == "lechuga":
            cant_lechu = dos_art
        if uno_pre == "lechuga":
            pre_lechu = dos_pre
        #Betarraga
        if uno_art == "betarraga":
            cant_beta = dos_art
        if uno_pre == "betarraga":
            pre_beta = dos_pre
        #Retornar valor producto
        if pro == "tomate":
            total_toma = cant_toma * pre_toma
            return total_toma
        if pro == "zanahoria":
            total_zana = cant_zana * pre_zana
            return total_zana
        if pro == "cebolla":
            total_cebo = cant_cebo * pre_cebo
            return total_cebo
        if pro == "papas":
            total_papas = cant_papas * pre_papas
            return total_papas
        if pro == "lechuga":
            total_lechu = cant_lechu * pre_lechu
            return total_lechu
        if pro == "betarraga":
            total_beta = cant_beta * pre_beta
            return total_beta


pro = input("Ingrese el producto a comprar: ").lower()
while pro != "tomate" and pro != "zanahoria" and pro != "cebolla" and pro != "papas" and pro != "lechuga" and pro != "betarraga":
    pro = input("Error,ingrese el producto a comprar: ").lower()

desc = total(pro) 
print(desc)
# print("Se aplico un 30% de descuento en la compra, el valor a pagar es $",desc)



        


    
    


