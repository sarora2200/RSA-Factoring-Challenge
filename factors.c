#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */

int main(void)
{
long long int num[] = {4, 12, 34, 128, 1024, 4958, 1718944270642558716715,
	9, 99, 999, 9999, 9797973, 49, 239809320265259};
int num_count = sizeof(num) / sizeof(num[0]);

for (int i = 0; i < num_count; i++)
{
long int factor1 = 2;
long int factor2;

while (num[i] % factor1)
{
if (factor1 <= num[i])
{
factor1++;
}
else
{
return (-1);
}
}
factor2 = num[i] / factor1;
printf("%lld=%ld*%ld\n", num[i], factor2, factor1);
}

return (0);
}
