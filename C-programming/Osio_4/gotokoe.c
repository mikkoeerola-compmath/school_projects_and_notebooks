#include "gotokoe.h"

int max2D(int **t2d, int kork, int lev) {
	int i = 0, j = 0;
	int suurin = t2d[0][0];
	
	ALKU:
	if(i >= kork)
		goto LOPPU;
	
	if(j >= lev)
		goto OHI;
	
	if(t2d[i][j] > suurin)
		goto SIJOITUS;
	
	j++;
	goto ALKU;
	
	OHI:
	  j = 0;
	  ++i;
	  goto ALKU;
	
	SIJOITUS:
	  suurin = t2d[i][j];
	  ++j;
	  goto ALKU;
	
	LOPPU:
	return suurin;
}