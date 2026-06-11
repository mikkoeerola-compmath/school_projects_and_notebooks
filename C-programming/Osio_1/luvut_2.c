#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int check_div(int a, int div[], int size)
{
	int result = 1;
	int i = 0;
	while (result && i<size) {
		if (a%div[i]==0) {result = 0;}
		++i;
	}
	return result;
}

int is_last(int a, int b, int div[], int size)
{
	int i;
	int result = 1;
	for (i=a+1; i<=b;++i) {
		if (check_div(i, div, size)) {result = 0;} 
	}
	return result;
}

int main(int argc, char *argv[])
{
    int a = atoi(argv[1]);
	int b = atoi(argv[2]);
	int div[SHRT_MAX];
    int i;
	int j;
	for (j=0;j<argc-3;++j) {
		div[j] = atoi(argv[j+3]);
	}
    for (i=a; i<=b;++i) {
        if(check_div(i, div, argc-3)){
		    printf("%d",i);
		    if (is_last(i, b, div, argc-3) == 0) {
		        printf(" ");
	        } else {printf("\n");}
		}
    }
	return 0;
}
