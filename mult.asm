section .text

    global multiply_floats

multiply_floats:
    enter 8, 0          ; establecer un marco de pila de 8 bytes

    fld dword [ebp + 8]     ;carga el valor del primer argumento cripto_value_usd en st0.
    fmul dword [ebp + 12]   ;multiplica el valor en st0 por segundo argumento usd_to_change, el resultado se almacena en st0.

    leave               ; restaurar el marco de pila
    ret                 ; retornar
