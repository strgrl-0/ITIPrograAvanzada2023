"""
Clase 8  PPT ejercicios,ej1
"""

def mayor(arch):
    arch = open("ejercicio1.txt","r",encoding = "utf-8")
    linea = arch.readline().strip()
    val = []
    while linea != "":
        partes = linea.split()
        val.append(int(partes[0]))
        linea = arch.readline().strip()
        for a in range(len(val) - 1):
            for b in range(a + 1,len(val)):
                if val[a] < val[b]:
                    aux = val[a]
                    val[a] = val[b]
                    val[b] = aux
    return val[0:3]
  
arch = open("ejercicio1.txt","r",encoding = "utf-8")
ordenar = mayor(arch)
print(ordenar)