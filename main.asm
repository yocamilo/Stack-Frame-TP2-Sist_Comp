segment .text

    global main

multiply_floats:
    push ebp
    mov ebp,esp

    ;pusha ;guardar gp registers???
    fld dword   [ebp+8] ;load floating-point value in st0 porque +8??
    fmul dword  [ebp+12];multiplica lo que tenia en st0 por el otro parametro y resultado queda en st0

    leave
    ret
