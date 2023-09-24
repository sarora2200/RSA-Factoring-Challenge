#include <stdio.h>
/**
 * main - check the code
 *
 * Return: Always 0
*/

long long int factorize(long long int n) {
    long long int factor1 = 2;

    while (n % factor1 != 0) {
        if (factor1 <= n) {
            factor1++;
        } else {
            return -1; /* Unable to find factors in time */
        }
    }

    return factor1;
}

int main(void) {
    long long int num = 239809320265259;
    long long int factor1, factor2;

    factor1 = factorize(num);

    if (factor1 == -1) {
        printf("Unable to find factors in time.\n");
        return -1;
    }

    factor2 = num / factor1;
    printf("%lld = %lld * %lld\n", num, factor1, factor2);

    return 0;
}
