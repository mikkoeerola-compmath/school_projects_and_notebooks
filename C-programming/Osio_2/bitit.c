#include "bitit.h"
#include <stdio.h>
#include <limits.h>

void kaannaScharBitit(signed char *x) {
	int i;
	int size = CHAR_BIT;
	int bith;
	int bitr;

	for (i = 0; i < size/2; ++i) {
		bith = (1<<(size-i-1)& *x)? 1 : 0;
		bitr = (1<<(i)& *x)? 1 : 0;
		if (bith != bitr) {
			if (bitr == 1) {
				*x = (1<<(size-i-1)) | *x;
			} else {
				*x = ~(1<<(size-i-1)) & *x;
			}
			if (bith == 1) {
				*x = 1<<(i)| *x;
			} else {
				*x = ~(1<<i) & *x;
			}
		}
	}
}

void kaannaShortBitit(short *x) {
	int i;
	int size = CHAR_BIT*sizeof(short);
	int bith;
	int bitr;

	for (i = 0; i < size/2; ++i) {
		bith = (1<<(size-i-1)& *x)? 1 : 0;
		bitr = (1<<(i)& *x)? 1 : 0;
		if (bith != bitr) {
			if (bitr == 1) {
				*x = (1<<(size-i-1)) | *x;
			} else {
				*x = ~(1<<(size-i-1)) & *x;
			}
			if (bith == 1) {
				*x = 1<<(i)| *x;
			} else {
				*x = ~(1<<i) & *x;
			}
		}
	}
}

void kaannaIntBitit(int *x) {
	int i;
	int size = CHAR_BIT*sizeof(int);
	int bith;
	int bitr;

	for (i = 0; i < size/2; ++i) {
		bith = (1<<(size-i-1)& *x)? 1 : 0;
		bitr = (1<<(i)& *x)? 1 : 0;
		if (bith != bitr) {
			if (bitr == 1) {
				*x = (1<<(size-i-1)) | *x;
			} else {
				*x = ~(1<<(size-i-1)) & *x;
			}
			if (bith == 1) {
				*x = 1<<(i)| *x;
			} else {
				*x = ~(1<<i) & *x;
			}
		}
	}
}

void kaannaLongBitit(long *x) {
	int i;
	int size = CHAR_BIT*sizeof(long);
	int bith;
	int bitr;

	for (i = 0; i < size/2; ++i) {
		bith = (1L<<(size-i-1)& *x)? 1 : 0;
		bitr = (1L<<(i)& *x)? 1 : 0;
		if (bith != bitr) {
			if (bitr == 1) {
				*x = (1L<<(size-i-1)) | *x;
			} else {
				*x = ~(1L<<(size-i-1)) & *x;
			}
			if (bith == 1) {
				*x = 1L<<(i)| *x;
			} else {
				*x = ~(1L<<i) & *x;
			}
		}
	}
}

/*
int main() {
	long int x = 2015;
	signed char xs = x;
	short xss = x;
	int xi = x;
	kaannaScharBitit(&xs);
	kaannaShortBitit(&xss);
	kaannaIntBitit(&xi);
	kaannaLongBitit(&x);
	return 0;
}*/