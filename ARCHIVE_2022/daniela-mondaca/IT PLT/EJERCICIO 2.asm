CUADRO MACRO XI,YI,XF,YF,COLOR;definir funcion cuadro
MOV AX, 0600H ; AX = 0600H, a traves de asignacion directa
MOV BH, COLOR ; COLOR DE FONDO Y LETRA
MOV BL, 00H   ; BL = 00H, a traves de asignacion directe
MOV CH, YI ; Y INICIAL
MOV CL, XI ; X INICIAL
MOV DH, YF ; Y FINAL
MOV DL, XF ; X FINAL
INT 10h    ; Llama a la interrupcion 10h para mostrar texto en pantalla
ENDM       ; Fin de la macro
DESPLEGAR MACRO MENSAJE
MOV AH,09 ;****** MUESTRA MENSAJE *******
MOV DX,OFFSET MENSAJE
INT 21h    ;Llama a la interrupcion 21h para mostrar texto en pantalla
ENDM
POSICION MACRO X,Y
; **** POSICIONA EL CURSOR ********
MOV DH, Y ; POSICION EN Y
MOV DL, X ; POSICION EN X
MOV AH, 02 ; AH = 02, a traves de asignacion directa
MOV BH, 00 ; BH = 00, a traves de asignacion directa
INT 10H   ; Llama a la interrupcion 10h para mostrar texto en pantalla
ENDM
DATOS SEGMENT ;SEGMENTO DE DATOS //Se deja vacio
datos ends
CODIGO SEGMENT
ASSUME CS: CODIGO,DS:DATOS,SS:PILA
PRINCIPAL PROC
MOV AX,DATOS
MOV DS,AX    
;Cuadro (Inicial X,Inicial Y, Final X, Final Y, COLOR)
;Posicion (X, Y)
;Mostrar cuadros
;Linea verde
CUADRO 10,4,11,5,33 ;Cuadro color verde 1
CUADRO 13,4,14,5,33 ;Cuadro color verde 2
CUADRO 16,4,17,5,33 ;Cuadro color verde 3
CUADRO 19,4,20,5,33 ;Cuadro color verde 4
CUADRO 22,4,23,5,33 ;Cuadro color verde 5
CUADRO 25,4,26,5,33 ;Cuadro color verde 6
CUADRO 28,4,29,5,33 ;Cuadro color verde 7
CUADRO 31,4,32,5,33 ;Cuadro color verde 8
CUADRO 34,4,35,5,33 ;Cuadro color verde 9
CUADRO 37,4,38,5,33 ;Cuadro color verde 10
CUADRO 40,4,41,5,33 ;Cuadro color verde 11
CUADRO 43,4,44,5,33 ;Cuadro color verde 12
CUADRO 46,4,47,5,33 ;Cuadro color verde 13
CUADRO 49,4,50,5,33 ;Cuadro color verde 14
 
;Linea rosada   
CUADRO 10,7,11,8,81 ;Cuadro color rosado 1
CUADRO 13,7,14,8,81 ;Cuadro color rosado 2
CUADRO 16,7,17,8,81 ;Cuadro color rosado 3
CUADRO 19,7,20,8,81 ;Cuadro color rosado 4
CUADRO 22,7,23,8,81 ;Cuadro color rosado 5
CUADRO 25,7,26,8,81 ;Cuadro color rosado 6
CUADRO 28,7,29,8,81 ;Cuadro color rosado 7
CUADRO 31,7,32,8,81 ;Cuadro color rosado 8
CUADRO 34,7,35,8,81 ;Cuadro color rosado 9
CUADRO 37,7,38,8,81 ;Cuadro color rosado 10
CUADRO 40,7,41,8,81 ;Cuadro color rosado 11
CUADRO 43,7,44,8,81 ;Cuadro color rosado 12
CUADRO 46,7,47,8,81 ;Cuadro color rosado 13
CUADRO 49,7,50,8,81 ;Cuadro color rosado 14
 
;Linea amarilla    
CUADRO 10,10,11,11,100 ;Cuadro color amarrillo 1    
CUADRO 13,10,14,11,100 ;Cuadro color amarrillo 1
CUADRO 16,10,17,11,100 ;Cuadro color amarrillo 3
CUADRO 19,10,20,11,100 ;Cuadro color amarrillo 4
CUADRO 22,10,23,11,100 ;Cuadro color amarrillo 5
CUADRO 25,10,26,11,100 ;Cuadro color amarrillo 6
CUADRO 28,10,29,11,100 ;Cuadro color amarrillo 7
CUADRO 31,10,32,11,100 ;Cuadro color amarrillo 8
CUADRO 34,10,35,11,100 ;Cuadro color amarrillo 9
CUADRO 37,10,38,11,100 ;Cuadro color amarrillo 10
CUADRO 40,10,41,11,100 ;Cuadro color amarrillo 11
CUADRO 43,10,44,11,100 ;Cuadro color amarrillo 12
CUADRO 46,10,47,11,100 ;Cuadro color amarrillo 13
CUADRO 49,10,50,11,100 ;Cuadro color amarrillo 14
    
;Linea rosado
CUADRO 10,13,11,14,70 ;Cuadro color rosado 1 
CUADRO 13,13,14,14,70 ;Cuadro color rosado 2
CUADRO 16,13,17,14,70 ;Cuadro color rosado 3
CUADRO 19,13,20,14,70 ;Cuadro color rosado 4
CUADRO 22,13,23,14,70 ;Cuadro color rosado 5
CUADRO 25,13,26,14,70 ;Cuadro color rosado 6
CUADRO 28,13,29,14,70 ;Cuadro color rosado 7
CUADRO 31,13,32,14,70 ;Cuadro color rosado 8
CUADRO 34,13,35,14,70 ;Cuadro color rosado 9
CUADRO 37,13,38,14,70 ;Cuadro color rosado 10
CUADRO 40,13,41,14,70 ;Cuadro color rosado 11
CUADRO 43,13,44,14,70 ;Cuadro color rosado 12
CUADRO 46,13,47,14,70 ;Cuadro color rosado 13
CUADRO 49,13,50,14,70 ;Cuadro color rosado 14
 
;Pelota blanca
CUADRO 28,18,29,19,120 ;Pelota blanca   

;Plataforma azul 
CUADRO 22,22,23,23,22 ;Plataforma azul 1
CUADRO 25,22,26,23,22 ;Plataforma azul 2 
CUADRO 28,22,29,23,22 ;Plataforma azul 3 
CUADRO 31,22,32,23,22 ;Plataforma azul 4
CUADRO 34,22,35,23,22 ;Plataforma azul 5  

;MOVIMIENTO 
CUADRO 28,18,29,19,0 ;Cuadro negro  
CUADRO 29,19,30,20,120 ;Pelota blanca 
CUADRO 29,19,30,20,0 ;Cuadro negro
CUADRO 31,21,32,22,120 ;Pelota blanca  
CUADRO 31,21,32,22,0 ;Cuadro negro 
CUADRO 31,22,32,23,22 ;Plataforma azul 4
CUADRO 22,22,23,23,0 ;Negro en p azul 
CUADRO 37,22,38,23,22 ;Plataforma azul 6 
CUADRO 33,19,34,20,120 ;Pelota blanca


PRINCIPAL ENDP ;FIN DEL PROCEDIMIENTO
CODIGO ENDS ;FIN DEL SEGMENTO
END PRINCIPAL