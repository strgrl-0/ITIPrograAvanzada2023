.model small
.stack
.data
Cadena1 DB "Hola mundo.$"
.code

progama:
    mov ax,@data
    mov ds,ax
    mov dx,offset Cadena1
    mov ah,9
    int 21h
end progama