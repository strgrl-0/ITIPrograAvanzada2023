TITLE Estructura basica

DATOS SEGMENT;Iniciar segmento 
;DECLARACION DE VARIABLES-------------------------- 

;--------------------------    
DATOS ENDS;Cerrar segmento    

PILA SEGMENT  
;Define el almacen de la pila 

 DS 64 DUP(0)
    
PILA ENDS  

CODIGO SEGMENT
;Define el procedimiento

INICIO PROC FAR ;FAR sirve para llamar desde otro segmento,NEAR desde el mismo segmento

ASSUME DS:DATOS,CS:CODIGO, SS:PILA
PUSH DS
MOV AX,0
PUSH AX

MOV AX,DATOS
MOV DS,AX
MOV ES,AX
;Codigo aqui -----------------------------------------------

;Registros en ensamblador                                                          

;AX-BX-CX-DX SE PUEDEN DIVIDIR EN 2, EN PARTE ALTA Y BAJA CON 8 BITS EN SU INTERIOR      

;AX - Registro acumulador,resultados,lectura,etc (Dividido AH / AL).
;BX - Registro base o indice (Dividido BH / BL).
;CX - Registro contador (Operaciones de iteracion como ciclos) (Dividido CH / CL).
;DX - Registro de datos (dividido DH / DL). 
    
;SI - Registro indice fuente.
;DI - Registro indice destino.
;BP - Apuntador base, manipula la pila sin afectar a el registro de segmentos.
;SP - Apuntador de pila,almacena datos. 

;Suma en ensamblador
MOV AL,5 ;5 pasa a AL, entonces AL = 5(AL TIENE 8 BITS, soporta hasta 255)
ADD AL,7 ;Suma 5 contenido en AL + 7   

;Resta en ensamblador
MOV AL,5 ;5 pasa a AL, entonces AL = 5
SUB AL,3 ;Resta 5 contenido en AL - 3  

;Multiplicacion en ensamblador
  
;Multiplicacion de tipo BYTE 
;AX 255(Capacidad maxima)
MOV AL,150 ;Multiplicando
MOV BL,2   ;Multiplicador
MUL BL     ;Guarda resultado en AX 

;Multiplicacion de tipo WORD
;DX/AX 65535(Capacidad maxima)
MOV AX,300 ;Multiplicando
MOV BX,500 ;Multiplicador
MUL BX     ;Guarda resultado en AX

RET
INICIO ENDP
CODIGO ENDS

END INICIO