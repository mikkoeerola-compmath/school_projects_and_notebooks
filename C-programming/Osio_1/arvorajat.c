#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char *argv[]) {
	
	int i;

    for (i = 1; i < argc; i++) {
		
        int arvo = atoi(argv[i]);

        printf("%d: ", arvo);

        if (arvo >= SCHAR_MIN && arvo <= SCHAR_MAX) {
            printf("signed char, ");
        }
        if (arvo >= 0 && arvo <= UCHAR_MAX) {
            printf("unsigned char, ");
        }
        if (arvo >= SHRT_MIN && arvo <= SHRT_MAX) {
            printf("short int, ");
        }
        if (arvo >= 0 && arvo <= USHRT_MAX) {
            printf("unsigned short int, ");
        }
        if (arvo >= INT_MIN && arvo <= INT_MAX) {
            printf("int");
        }

        printf("\n");
    }

    return 0;
}