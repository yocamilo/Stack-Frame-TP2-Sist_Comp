segment .text
    global main
main:
    push ebp
    mov ebp,esp

    ;pusha ;guardar gp registers???
    fld dword   [ebp+8]
    fmul dword  [ebp+12]

    leave
    ret
