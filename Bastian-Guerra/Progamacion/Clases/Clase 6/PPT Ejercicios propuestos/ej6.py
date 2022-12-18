"""
PPT Ejercicios propuestos, ej6
Calcular distancia recorrida a partir de su velocidad y tiempo
*Vehiculo no acelera
"""

def distancia(vel,tiempo):
    dis = vel * tiempo
    return dis
    
    
vel = float(input("Ingrese velocidad:"))
tiempo = float(input("Ingrese tiempo:"))
while tiempo < 0:
    tiempo = float(input("El tiempo no puede ser negativo, ingrese nuevamente: "))
resul = distancia(vel,tiempo)
print(resul,"m/s")
#Falta generar tabla

