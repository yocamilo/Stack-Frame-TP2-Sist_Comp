#include <stdio.h>
#include <stdlib.h>

extern float multiply_floats(float cripto_value_usd, float usd_to_change);
float cripto_to_change(float cripto_value_usd, float usd_to_change);

int main(int argc ,char **argv){
    float cripto_value_usd = atof(argv[1]);
    float usd_to_change = atof(argv[2]);

    cripto_to_change(cripto_value_usd,usd_to_change);

    return 0;
}

float cripto_to_change(float cripto_value_usd, float usd_to_change) {
    printf("#################################################################\n");
    printf("C ## El valor de la criptomoneda es: %.2f\n", cripto_value_usd);
    printf("C ## El valor de USD al cambio elegido es: %.2f\n",usd_to_change);

    float result = multiply_floats(cripto_value_usd, usd_to_change);
    
    printf("C ## El valor de la cripto en la moneda seleccionada es: %.2f\n",result);
    printf("#################################################################\n");
    return(result);
}