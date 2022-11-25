CUADRO MACRO XI,YI,XF,YF,COLOR
MOV AX, 0600H ;
MOV BH, COLOR ; COLOR DE FONDO Y LETRA
MOV BL, 00H
MOV CH, YI ; Y INICIAL
MOV CL, XI ; X INICIAL
MOV DH, YF ; Y FINAL
MOV DL, XF ; X FINAL
INT 10h
ENDM
DESPLEGAR MACRO MENSAJE
MOV AH,09 ;****** MUESTRA MENSAJE *******
MOV DX,OFFSET MENSAJE
INT 21h
ENDM
POSICION MACRO X,Y
; **** POSICIONA EL CURSOR ********
MOV DH, Y ; POSICION EN Y
MOV DL, X ; POSICION EN X
MOV AH, 02
MOV BH, 00
INT 10H
ENDM
DATOS SEGMENT ;SEGMENTO DE DATOS
M1 DB "1",'$' 
M2 DB "2","$"  
M3 DB "3","$"
M4 DB "4","$"  
M5 DB "BASTIAN GUERRA","$"
datos ends
CODIGO SEGMENT
ASSUME CS: CODIGO,DS:DATOS,SS:PILA
PRINCIPAL PROC
MOV AX,DATOS
MOV DS,AX
cuadro 1,1,20,5,71 ;Cuadro color rojo
posicion 10,3 ;Posicion numero 1  
desplegar m1  ;Despliega numero 1   
cuadro 1,6,20,10,22 ;Cuadro color azul  
posicion 10,8 ;Posicion numero 2  
desplegar m2  ;Despliega numero 2 
cuadro 1,11,20,15,33 ;Cuadro color verde  
posicion 10,13 ;Posicion numero 2  
desplegar m3  ;Despliega numero 3 
cuadro 1,16,20,20,54 ;Cuadro color celeste  
posicion 10,18 ;Posicion numero 4  
desplegar m4  ;Despliega numero 4
cuadro 40,10,60,16,22 ;Cuadro color azul  
posicion 43,13 ;Posicion numero 4  
desplegar m5  ;Despliega numero 4
PRINCIPAL ENDP ;FIN DEL PROCEDIMIENTO
CODIGO ENDS ;FIN DEL SEGMENTO
END PRINCIPAL