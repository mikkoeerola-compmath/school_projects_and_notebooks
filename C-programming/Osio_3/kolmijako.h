#include <stddef.h>

void kolmijako_gen(void *t, size_t n, size_t koko, size_t vipu1, size_t vipu2,
                   int (*vrt)(const void *, const void *), size_t *p1, size_t *p2);