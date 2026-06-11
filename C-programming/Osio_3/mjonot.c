#include "mjonot.h"
#include <string.h>
#include <stdlib.h>

char ** kopioi_mjt(char **mjt, size_t lkm) {
	char **kop = malloc(lkm*sizeof(char*));
	int i = 0;
	for (i=0; i<lkm;++i) {
		int p = strlen(mjt[i]);
		char *mj = malloc(p+1);
		
		strcpy(mj,mjt[i]);
		kop[i] = mj;
	}
	
	return kop;
}

void vaihda_paikkaa(char **mjt, int i, int j) {
    char *temp = mjt[i];
    mjt[i] = mjt[j];
    mjt[j] = temp;
}

char ** jarjesta_mjt(char **mjt, size_t lkm, int (*vrt)(const char*, const char *)) {
	char ** kop = kopioi_mjt(mjt, lkm);
	int i = 0;
	int j = 0;
	
	/* Bubble sort algoritmi */
	for ( i = 0; i < lkm - 1; ++i) {
        for ( j = 0; j < lkm - i - 1; ++j) {
            if (!(*vrt)(kop[j], kop[j + 1])) {
                vaihda_paikkaa(kop, j, j + 1);
            }
        }
    }
	
	return kop;
}