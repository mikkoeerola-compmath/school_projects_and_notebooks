#include <stddef.h>
#include <stdio.h>
#include "genhaku.h"

size_t etsi(void *mista, size_t n, void *mita, size_t m, size_t koko) {
	size_t i = 0;
	size_t j = 0;
	char *a = mista;
	char *b = mita;
	int is_found = 1;
	
	for (i = 0; i <= n-m; ++i) {
		for (j=0; j<m; ++j) {
			size_t k = 0;
			int is_same = 1;
			for (k=0; k < koko; ++k) {
				if (a[(i+j)*koko+k] != b[j*koko+k]) {
					is_same = 0;
					break;
				}
			}
			if (!is_same) {
				is_found = 0;
				break;
			} else {
				is_found = 1;
			}
		}
		if (is_found) {
			return i;
		}
	}
	return n;
}