#include "fibonacci.h"
#include <stdlib.h>
#include <stdio.h>

char * fib_jono_mj(unsigned int n) {
	char *x = malloc(sizeof(char));
	int i = 0;
	int fib_ee = 0;
	int fib_e = 1;
	int kap = 1;
	int pit = 0;
	char *temp = NULL;
	x[0] = '\0';
	
	if (n<1) {
		return x;
	}
	
	temp = realloc(x, 2*sizeof(char));
	if (temp != NULL) {
		x = temp;
		sprintf(x, "%d\0", fib_ee);
	}
	if (n<2) {
		return x;
	}
	temp = realloc(x, 8*sizeof(char));
	if (temp != NULL) {
		x = temp;
		sprintf(&x[1], ", %d\0", fib_e);
	}
	if(n<3) {
		temp = realloc(x,5*sizeof(char));
		x = temp;
		return x;
	}
	
	kap = 8;
	pit = 5;

	
	for (i=2; i<n; ++i) {
		unsigned int m = 3; /* välimerkki ja lopetusmerkit*/
		unsigned int tmp = 0;
		int fib_i = fib_e+fib_ee;
        for(tmp = fib_i; tmp > 9; tmp /= 10) {
            m += 1;
	    }
		if (pit+m > kap) {
			while (pit+m > kap) {
			    kap = 2*kap;
		    }
			temp = realloc(x, kap*sizeof(char));
			if (temp != NULL) {
				x =temp;
			}
		}
		
	    sprintf(&x[pit-1], ", %d\0", fib_i);
		pit += m;
		fib_ee = fib_e;
		fib_e = fib_i;
	}
	
	printf("pit: %d kap: %d\n", pit, kap);
	temp = realloc(x, (pit)*sizeof(char));
	x = temp;
	return x;
}