#include "geometria.h"
#include <math.h>

const long double PII = 3.14159265358979323846L;

double ympyranAla(double sade)
{
	return PII*sade*sade;
}

double pallonTilavuus(double sade)
{
	return (4.0/3.0)*PII*pow(sade,3);
}