#include <string.h>
#include <math.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
	double arvo = 0;
	int exp = -127;
	int sign;
	int i;
	
	for (i = 0; i < 23; ++i) {
		if (argv[1][32-23+i] == '1') {
			arvo += pow(2,-i-1);
		}
	}
	printf("%.15f\n", arvo+1);
	
	for (i=0; i < 8; ++i) {
		if (argv[1][i+1] == '1') {
			exp += pow(2,8-i-1);
		}
	}
	printf("%d\n", exp);
	
	if (argv[1][0] == '1') {
		printf("-\n");
		sign = -1;
	} else {
		printf("+\n");
		sign = 1;
	}
	
	printf("%.15f\n", sign*((1+arvo)*pow(2,exp)));
	return 0;
}