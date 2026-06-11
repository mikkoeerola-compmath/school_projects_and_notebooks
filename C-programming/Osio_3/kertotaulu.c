#include "kertotaulu.h"
#include <stdlib.h>

Kertotaulu * luoKertotaulu(uint a, uint b, uint c, uint d) {
	if (b < a || d < c) {
		return NULL;
	} else {
		Kertotaulu *kt = malloc(sizeof(Kertotaulu));
		uint **ker = malloc((d-c+2)*sizeof(uint *));
		int i = 0;
		int j = 0;
		kt->a = a;
		kt->b = b;
		kt-> c = c;
		kt-> d = d;
		for (i=0; i<(d-c+2); ++i) {
			uint *ktrivi = malloc((b-a+2)*sizeof(uint));
			ker[i] = ktrivi;
		}
		
		for (i=0; i<d-c+2; ++i) {
			for (j=0; j<(b-a+2); ++j) {
				if (i==0 && j==0) {ker[i][j]=0;}
				else if (i==0) {ker[i][j] = a+j-1;}
				else if (j==0) {ker[i][j] = c+i-1;}
				else {ker[i][j]=(a+j-1)*(c+i-1);}
			}
		}
		kt->kertotaulu = ker;
		return kt;
	}
}

void tuhoaKertotaulu(Kertotaulu *kt) {
	int i = 0;
	for (i = 0; i < (kt->d-kt->c+2); ++i) {
		free(kt->kertotaulu[i]);
	}
	free(kt->kertotaulu);
	free (kt);
}