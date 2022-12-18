"""
Clase 06 Ejercicios, ej1
"""

def ventas(tipo,cantidad):
    if tipo == "cancha":
        precio = 20000
    if tipo == "platea":
        precio = 30000
    if tipo == "vip":
        precio = 40000
    total = cantidad * precio
    return total

tipo = input("Ingrese el tipo de entrada a comprar(cancha,platea,vip): ").lower()
while tipo != "cancha" and tipo != "platea" and tipo != "vip":
    tipo = input("Error,ingrese el tipo de entrada nuevamente(cabcga,platea,vip): ")
cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))

valor_entrada = ventas(tipo,cantidad)
print(valor_entrada)
        



