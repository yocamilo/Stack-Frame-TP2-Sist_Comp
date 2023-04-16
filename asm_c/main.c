#include <stdio.h>
#include <stdlib.h>

extern float multiply_floats(float cripto_value_usd, float usd_to_change);

int main()
{
    if(sizeof(char*)==8){
        printf("\nC esta en 64 bits\n");    
    }
    else if(sizeof(char*)){
        printf("\nC esta en 32 bits\n");
    }
    float cripto_value_usd = 100;
    float usd_to_change = 3.5;
    float result = multiply_floats(cripto_value_usd, usd_to_change);
    
    printf("The result is: %f\n", result);
    return 0;
}