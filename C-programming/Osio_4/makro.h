#ifdef OTE_DEBUG
   #include <stdio.h>
#endif

#define PII 3.141592653589793
#define MJ2(a) #a
#define MJ(a) MJ2(a)

#ifndef DESIMAALIT
  #define DESIMAALIT 3
#endif

#ifndef TYYPPI
  #define TYYPPI unsigned char
#endif

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) < (b) ? (b) : (a))
#define MIN3(a, b, c) ((c) < MIN(a, b) ? (c) : MIN(a, b))
#define MAX3(a, b, c) ((c) < MAX(a, b) ? MAX(a, b) : (c))
#define MIN4(a, b, c, d) ((d) < MIN3(a, b, c) ? (d) : MIN3(a, b, c))
#define MAX4(a, b, c, d) ((d) > MAX3(a, b, c) ? (d) : MAX3(a, b, c))

#ifdef OTE_DEBUG
  #define debug(msg) fprintf(stderr, msg)
#else
  #define debug(msg)
#endif