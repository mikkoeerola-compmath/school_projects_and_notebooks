#include "piste3d.h"
#include <math.h>
#include <stdio.h>

double etaisyys(Piste3D a, Piste3D b) {
	return sqrt(pow(a.x-b.x,2)+pow(a.y-b.y,2)+pow(a.z-b.z,2));
}

void tulosta(Piste3D p, int tarkkuus) {
	printf("(%.*f, %.*f, %.*f)", tarkkuus, p.x, tarkkuus, p.y, tarkkuus, p.z);
}