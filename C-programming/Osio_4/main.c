#include <stdio.h>
#include <stdlib.h>
#include "makro.h"

int main(int agrc, char *argv[])
{
  TYYPPI s = atof(argv[1]);
  TYYPPI t = atof(argv[2]);
  TYYPPI u = atof(argv[3]);
  TYYPPI v = atof(argv[4]);
  int d = DESIMAALIT; /* Lyhentää alla olevaa printf-kutsua... */
  /* C-kääntäjä yhdistää peräkkäin annetut vakiomerkkijonot. */
  /* Esim. "sana" " ja " "toinen" yhdistyisi muotoon "sana ja toinen". */
  debug("Pii: " MJ(PII) "\n");
  printf("Arvojen %.*f ja %.*f minimi ja maksimi: %.*f ja %.*f\n",
                  d, (double) s, d, (double) t,
                  d, (double) MIN(s, t), d, (double) MAX(s, t));
  printf("Arvojen %.*f, %.*f, ja %.*f minimi ja maksimi: %.*f ja %.*f\n",
                  d, (double) t, d, (double) u, d, (double) v,
                  d, (double) MIN3(t, u, v), d, (double) MAX3(t, u, v));
  printf("Arvojen %.*f, %.*f, %.*f ja %.*f minimi ja maksimi: %.*f ja %.*f\n",
                  d, (double) s, d, (double) t, d, (double) u, d, (double) v,
                  d, (double) MIN4(s, t, u, v), d, (double) MAX4(s, t, u, v));
  return 0;
}