;output:com
org 100h
.data
    msg db "mensaje 1 Hello world $"
    msg2 db "mensaje 2 Hello",24h
.code
    mov ax,@data
    mov ds,ax
    mov dx,offset msg
    mov ah,9
    int 21h
    mov ax,@data
    mov ds,ax
    mov dx,offset msg2
    mov ah,9
    int 21h
.exit