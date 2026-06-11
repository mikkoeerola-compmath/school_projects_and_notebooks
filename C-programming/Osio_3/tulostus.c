#include <stdio.h>
#include "tulostus.h"

void tulostaDblTaulu(double *taulu, size_t lkm, const char *taulNimi, int tarkkuus, const char *tiedNimi) {
	FILE *td = fopen(tiedNimi, "w");
	size_t i = 0;
	
	if (td == NULL) {
		return;
	}
	
	for (i = 0; i<lkm; ++i) {
		fprintf(td, "%s[%ld] = %.*f\n", taulNimi, i, tarkkuus, taulu[i]);
	}
	
}