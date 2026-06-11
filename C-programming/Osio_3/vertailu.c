#include "rectangle.h"
#include "vertailu.h"
#include <string.h>

int rectAlaVrt(const void *a, const void *b) {
	Rectangle * const *x = a;
	Rectangle * const *y = b;
	int alaA = (*x)->width*(*x)->height;
	int alaB = (*y)->width*(*y)->height;
	
	return (alaA < alaB) ? -1 : (alaA == alaB ? 0 : 1); 
}

int rectXyVrt(const void *a, const void *b) {
	Rectangle * const *x = a;
	Rectangle * const *y = b;
	int ans = 0;
	
	if ((*x)->origin.x < (*y)->origin.x) {
		ans = -1;
	} else {
		if ((*x)->origin.x > (*y)->origin.x) {
			ans = 1;
		} else {
			ans = ((*x)->origin.y < (*y)->origin.y)? -1 :
			(((*x)->origin.y == (*y)->origin.y)? 0: 1);
		}
	}
	return ans;
}

int rectLeveysVrt(const void *a, const void *b) {
	Rectangle * const *x = a;
	Rectangle * const *y = b;
	
	return ((*x)->width < (*y)->width) ? 1 : (((*x)->width > (*y)->width)? -1 : 0);
}

int mjPitAakkosVrt(const void *a, const void *b) {
	char * const *x = a;
	char * const *y = b;
	int ans = 0;
	
	if (strlen(*x) < strlen(*y)) {
		ans = 1;
	} else {
		if (strlen(*x) > strlen(*y)) {
			ans = -1;
		} else {
			ans = strcmp(*x,*y);
		}
	}
	return ans;
}