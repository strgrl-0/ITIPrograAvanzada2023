ORG 100h
MOV CX,8
MOV BX,1
MOV DL,2
comienzo:
    MOV AX,BX
    MUL DX
    MOV BX,AX
    LOOP comienzo
RET