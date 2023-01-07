.model small
.stack ;Define segmento pila de la longitud especificada    
.data ;Define segmento datos NEAR con valores iniciales
Cadena1 DB "Hola mundo.$"  
.code ;Define segmento codigo

progama:
    mov ax,@data
    mov ds,ax
    mov dx,offset Cadena1
    mov ah,9
    int 21h
end progama