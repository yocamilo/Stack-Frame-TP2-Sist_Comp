#include <stdio.h>
#include <stdlib.h>

extern float multiply_floats(float cripto_value_usd, float usd_to_change);

int main()
{
    float cripto_value_usd = 100;
    float usd_to_change = 3.5;
    float result = multiply_floats(cripto_value_usd, usd_to_change);
    
    printf("The result is: %f\n", result);
    return 0;
}