include "emu8086.inc" ;Declaramos libreria
org 100h

print "Hola mundo" ;Imprimir cadena
gotoxy 10,5 ;Va hacia direccion 10 en x,5 en y (Posicion pantalla)
putc 83 ;Imprimir caracter 65 de ASCII que es caracter A    
putc 85 ;Imprime U en ASCII
putc 83 ;Imprimir S en ASCII 
gotoxy 10,6 ;Va hacia direccion 10 en x, 6 en y (Posicion pantalla)
putc "B" ;Imprime B                                                
