#include <stdio.h>

float cripto_to_change(float cripto_value_usd, float usd_to_change) {
    if(sizeof(char*)==8){
        printf("\nEstoy en 64 bits\n");    
    }
    else if(sizeof(char*)){
        printf("\nEstoy en 32 bits\n");
    }
    

    printf("El valor de la criptomoneda es: %f\n", cripto_value_usd);
    printf("El valor de USD al cambio elegido es: %f\n",usd_to_change);

    float btc_to_change = usd_to_change * cripto_value_usd;
    
    printf("%f\n",btc_to_change);

    return(btc_to_change);
}

