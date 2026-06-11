typedef unsigned int uint;

struct Kertotaulu {
	uint a;
	uint b;
	uint c;
	uint d;
	uint **kertotaulu; 
};

typedef struct Kertotaulu Kertotaulu;

Kertotaulu * luoKertotaulu(uint a, uint b, uint c, uint d);

void tuhoaKertotaulu(Kertotaulu *kt);