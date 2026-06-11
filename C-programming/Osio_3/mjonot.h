#include <stddef.h>

char ** kopioi_mjt(char **mjt, size_t lkm);

char ** jarjesta_mjt(char **mjt, size_t lkm, int (*vrt)(const char*, const char *));

void vaihda_paikkaa(char **mjt, int i, int j);