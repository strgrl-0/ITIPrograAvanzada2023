CUADRO MACRO XI,YI,XF,YF,COLOR ;definir funcion cuadro
MOV AX, 0600H ; AX = Direccion de memoria 0600H
MOV BH, COLOR ; COLOR DE FONDO Y LETRA 
MOV BL, 00H ; BL = Direccion de memoria 00H
MOV CH, YI ; Y INICIAL
MOV CL, XI ; X INICIAL
MOV DH, YF ; Y FINAL
MOV DL, XF ; X FINAL
INT 10h    ; Llama a la interrupcion 10h para mostrar texto en pantalla
ENDM       ; Fin de la macro
DESPLEGAR MACRO MENSAJE  ;Desplegar variable
MOV AH,09 ;##### MUESTRA MENSAJE ####
MOV DX,OFFSET MENSAJE
INT 21h   ;Llama a la interrupcion 21h para mostrar texto en pantalla
ENDM
POSICION MACRO X,Y ; Definir funcion de posicion
; **** POSICIONA EL CURSOR ********
MOV DH, Y ; POSICION EN Y
MOV DL, X ; POSICION EN X
MOV AH, 02 ; AH = 02, asignacion directa
MOV BH, 00 ; BH = 00, asignacion directa
INT 10H   ; Llama a la interrupcion 10h para mostrar texto en pantalla
ENDM
DATOS SEGMENT ;SEGMENTO DE DATOS
M1 DB "1",'$' ;Guardar datos. "1"
M2 DB "2","$" ;Guardar datos. "2" 
M3 DB "3","$" ;Guardar datos. "3"
M4 DB "4","$" ;Guardar datos. "4" 
M5 DB "DANIELA MONDACA","$" ;Guardar datos. "DANIELA MONDACA"
datos ends    ; FIN SEGMENTO DE DATOS   

CODIGO SEGMENT;SEGMENTO DE CODIGO
ASSUME CS: CODIGO,DS:DATOS,SS:PILA; Asume CS = CODIGO, DS = DATOS, SS = Pila

PRINCIPAL PROC
MOV AX,DATOS
MOV DS,AX
CUADRO 1,1,20,5,71 ;Cuadro rojo
POSICION 10,3 ;Posicion numero 1  
DESPLEGAR M1  ;Despliega numero 1
   
CUADRO 1,6,20,10,22 ;Cuadro azul  
POSICION 10,8 ;Posicion numero 2  
DESPLEGAR M2  ;Despliega numero 2 

CUADRO 1,11,20,15,33 ;Cuadro verde  
POSICION 10,13 ;Posicion numero 3  
DESPLEGAR M3  ;Despliega numero 3 

CUADRO 1,16,20,20,54 ;Cuadro celeste  
POSICION 10,18 ;Posicion numero 4  
DESPLEGAR M4  ;Despliega numero 4

CUADRO 40,10,60,16,22 ;Cuadro azul
POSICION 43,13 ;Posicion numero 5  
DESPLEGAR M5  ;Despliega numero 5

PRINCIPAL ENDP ;FIN DEL PROCEDIMIENTO
CODIGO ENDS ;FIN DEL SEGMENTO DE CODIGO
END PRINCIPAL