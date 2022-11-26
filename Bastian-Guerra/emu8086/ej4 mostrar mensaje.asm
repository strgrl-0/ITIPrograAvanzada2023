;output: com
org 100h
.data
    msg db "Hello world",24h ; 24h = signo dolar ASCII
.code
    mov ax,@data ;Llama al segmento de datos
    mov ds,ax
    mov dx,offset msg
    mov ah,9 ;Interrumpe 21h para mostrar un mensaje terminado en $
    int 21h
.exit ; Genera instrucciones del int 21h funcion 4ch para salida progama, se ve en interrumpciones en la seccion help en int21h