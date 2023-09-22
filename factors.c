#include <stdio.h>

void factorize(int n) {
int i;
for (i = 2; i <= n; i++) {
if (n % i == 0) {
printf("%d=%d*%d\n", n, i, n/i);
return;
}
}
}

int main(int argc, char *argv[]) {
int n;
if (argc != 2) {
printf("Usage: %s <file>\n", argv[0]);
return (1);
}

FILE *file = fopen(argv[1], "r");
if (!file) {
perror("Error opening file");
return (1);
}

while (fscanf(file, "%d", &n) == 1) {
factorize(n);
}

fclose(file);
return (0);
}

