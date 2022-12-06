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
datos ends
CODIGO SEGMENT
ASSUME CS: CODIGO,DS:DATOS,SS:PILA
PRINCIPAL PROC
MOV AX,DATOS
MOV DS,AX    
;Cuadro:
;PI X,PI Y, PF X, PF Y, COLOR
;Posicion:
;EJE X, EJE Y
;Desplegar:
;(Variable)  
; ----Desplegar cuadros----
;Linea verde
cuadro 10,4,11,5,33 ;Cuadro color verde 1
cuadro 13,4,14,5,33 ;Cuadro color verde 2
cuadro 16,4,17,5,33 ;Cuadro color verde 3
cuadro 19,4,20,5,33 ;Cuadro color verde 4
cuadro 22,4,23,5,33 ;Cuadro color verde 5
cuadro 25,4,26,5,33 ;Cuadro color verde 6
cuadro 28,4,29,5,33 ;Cuadro color verde 7
cuadro 31,4,32,5,33 ;Cuadro color verde 8
cuadro 34,4,35,5,33 ;Cuadro color verde 9
cuadro 37,4,38,5,33 ;Cuadro color verde 10
cuadro 40,4,41,5,33 ;Cuadro color verde 11
cuadro 43,4,44,5,33 ;Cuadro color verde 12
cuadro 46,4,47,5,33 ;Cuadro color verde 13
cuadro 49,4,50,5,33 ;Cuadro color verde 14 
;Linea rosada   
cuadro 10,7,11,8,81 ;Cuadro color rosado 1
cuadro 13,7,14,8,81 ;Cuadro color rosado 2
cuadro 16,7,17,8,81 ;Cuadro color rosado 3
cuadro 19,7,20,8,81 ;Cuadro color rosado 4
cuadro 22,7,23,8,81 ;Cuadro color rosado 5
cuadro 25,7,26,8,81 ;Cuadro color rosado 6
cuadro 28,7,29,8,81 ;Cuadro color rosado 7
cuadro 31,7,32,8,81 ;Cuadro color rosado 8
cuadro 34,7,35,8,81 ;Cuadro color rosado 9
cuadro 37,7,38,8,81 ;Cuadro color rosado 10
cuadro 40,7,41,8,81 ;Cuadro color rosado 11
cuadro 43,7,44,8,81 ;Cuadro color rosado 12
cuadro 46,7,47,8,81 ;Cuadro color rosado 13
cuadro 49,7,50,8,81 ;Cuadro color rosado 14 
;Linea amarilla    
cuadro 10,10,11,11,100 ;Cuadro color amarrillo 1    
cuadro 13,10,14,11,100 ;Cuadro color amarrillo 1
cuadro 16,10,17,11,100 ;Cuadro color amarrillo 3
cuadro 19,10,20,11,100 ;Cuadro color amarrillo 4
cuadro 22,10,23,11,100 ;Cuadro color amarrillo 5
cuadro 25,10,26,11,100 ;Cuadro color amarrillo 6
cuadro 28,10,29,11,100 ;Cuadro color amarrillo 7
cuadro 31,10,32,11,100 ;Cuadro color amarrillo 8
cuadro 34,10,35,11,100 ;Cuadro color amarrillo 9
cuadro 37,10,38,11,100 ;Cuadro color amarrillo 10
cuadro 40,10,41,11,100 ;Cuadro color amarrillo 11
cuadro 43,10,44,11,100 ;Cuadro color amarrillo 12
cuadro 46,10,47,11,100 ;Cuadro color amarrillo 13
cuadro 49,10,50,11,100 ;Cuadro color amarrillo 14    
;Linea roja
cuadro 10,13,11,14,70 ;Cuadro color rojo 1 
cuadro 13,13,14,14,70 ;Cuadro color rosado 2
cuadro 16,13,17,14,70 ;Cuadro color rosado 3
cuadro 19,13,20,14,70 ;Cuadro color rosado 4
cuadro 22,13,23,14,70 ;Cuadro color rosado 5
cuadro 25,13,26,14,70 ;Cuadro color rosado 6
cuadro 28,13,29,14,70 ;Cuadro color rosado 7
cuadro 31,13,32,14,70 ;Cuadro color rosado 8
cuadro 34,13,35,14,70 ;Cuadro color rosado 9
cuadro 37,13,38,14,70 ;Cuadro color rosado 10
cuadro 40,13,41,14,70 ;Cuadro color rosado 11
cuadro 43,13,44,14,70 ;Cuadro color rosado 12
cuadro 46,13,47,14,70 ;Cuadro color rosado 13
cuadro 49,13,50,14,70 ;Cuadro color rosado 14 
;Pelota blanca
cuadro 28,18,29,19,120 ;Pelota blanca  
;Plataforma azul 
cuadro 22,22,23,23,22 ;Plataforma azul 1
cuadro 25,22,26,23,22 ;Plataforma azul 2 
cuadro 28,22,29,23,22 ;Plataforma azul 3 
cuadro 31,22,32,23,22 ;Plataforma azul 4
cuadro 34,22,35,23,22 ;Plataforma azul 5 
; ----Creacion movimiento----   
cuadro 28,18,29,19,0 ;Cuadro negro  
cuadro 29,19,30,20,120 ;Pelota blanca 
cuadro 29,19,30,20,0 ;Cuadro negro
cuadro 31,21,32,22,120 ;Pelota blanca  
cuadro 31,21,32,22,0 ;Cuadro negro 
cuadro 31,22,32,23,22 ;Plataforma azul 4
cuadro 22,22,23,23,0 ;Cuadro negro plataforma azul 1
cuadro 37,22,38,23,22 ;Plataforma azul 6 
cuadro 33,19,34,20,120 ;Pelota blanca


PRINCIPAL ENDP ;FIN DEL PROCEDIMIENTO
CODIGO ENDS ;FIN DEL SEGMENTO
END PRINCIPAL