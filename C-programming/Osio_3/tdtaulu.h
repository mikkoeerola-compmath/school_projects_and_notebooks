#include <stdio.h>

struct TdTaulu {
	unsigned int n;
	unsigned int alkioKoko;
	const char* tdNimi;
	FILE* td;
};

typedef struct TdTaulu TdTaulu;

TdTaulu *luoTdTaulu(unsigned int n, unsigned int alkioKoko, const char *tdNimi);
TdTaulu *avaaTdTaulu(const char *tdNimi);
void vapautaTdTaulu(TdTaulu *tdt);
int tdtLue(TdTaulu *tdt, unsigned int i, unsigned int lkm, void *arvo);
int tdtKirj(TdTaulu *tdt, unsigned int i, unsigned int lkm, const void *arvo);