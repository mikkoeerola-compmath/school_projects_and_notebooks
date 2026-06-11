#include "murtoluku.h"
#include <stdio.h>

int gcd(int a, int b)
{
    int temp;
    while (b != 0)
    {
        temp = a % b;

        a = b;
        b = temp;
    }
    return a;
}

Murtoluku supistettuML(int os, int nim) {
	Murtoluku ml;
	int syt;
	
	if (nim < 0) {
		os = -1*os;
		nim = -1*nim;
	}
	
	if (nim == 0) {
		ml.os = 0;
		ml.nim = 1;
		return ml;
	}
	
	if(os == 0) {
		ml.os = os;
		ml.nim = nim;
		return ml;
	}
	
	if (os < 0) {
		syt = gcd(-os, nim);
	} else {
		syt = gcd(os, nim);
	}
	
	ml.os = os/syt;
    ml.nim = nim/syt;
	return ml;
}

Murtoluku lisaaML(Murtoluku a, Murtoluku b) {
	return supistettuML(a.os*b.nim+b.os*a.nim, a.nim*b.nim);
}

Murtoluku vahennaML(Murtoluku a, Murtoluku b) {
	return supistettuML(a.os*b.nim-b.os*a.nim, a.nim*b.nim);
}

Murtoluku kerroML(Murtoluku a, Murtoluku b) {
	return supistettuML(a.os*b.os, a.nim*b.nim);
}

Murtoluku jaaML(Murtoluku a, Murtoluku b) {
	return supistettuML(a.os*b.nim, a.nim*b.os);
}

void tulostaML(Murtoluku ml) {
	if (ml.os == 0) {
		printf("0");
	} else if (ml.nim == 1) {
		printf("%d", ml.os);
	} else {
		printf("%d/%d",ml.os, ml.nim);
	}
}