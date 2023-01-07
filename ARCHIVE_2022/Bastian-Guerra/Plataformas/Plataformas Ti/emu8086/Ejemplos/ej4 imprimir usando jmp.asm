include "emu8086.inc"
org 100h
mov ax,5
jmp etiqueta1
print "Esto no se va a imprimir"  
print "jmp hace que el progama salte"
print "A lo que esta en etiqueta1"
mov ax,10
etiqueta1:
print "AX sigue valiendo 5 debido a que nunca salto al segundo mov ax,10"
ret