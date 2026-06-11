#include "vaihto.h"

void vaihda(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}
void jarjesta(int *a, int *b, int *c) {
	if (*a < *b ) {
		if ( *a < *c ) {
			if ( *b < *c) {
				return;
			} else {
				vaihda(b,c);
			}
		} else {
			vaihda(a,c);
			vaihda(b,c);
		}
	} else if ( *c < *b ) {
		vaihda(a,c);
		vaihda(c,b);
	} else if ( *c < *a ) {
		vaihda(a,b);
		vaihda(b,c);
	} else {
		vaihda(a,b);
	}
}