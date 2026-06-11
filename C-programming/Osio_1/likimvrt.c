#include "likimvrt.h"
#include <math.h>

static double toleranssi = 0.000001;

double lueToleranssi() {
    return toleranssi;
}

void asetaToleranssi(double uusiToleranssi) {
    toleranssi = uusiToleranssi;
}

int doubleVrt(double a, double b) {
    return (fabs(a - b) <= toleranssi) ? 1 : 0;
}