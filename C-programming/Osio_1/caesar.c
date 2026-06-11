#include "caesar.h"
#include <limits.h>
#include <string.h>

void caesarKoodaa(char mj[], char aakkosto[], char korvaavat[])
{
	unsigned char korvaus[UCHAR_MAX + 1];
	int i;

    for (i = 0; i <= UCHAR_MAX; ++i) {
        korvaus[i] = i;
    }

    for (i=0;i<strlen(aakkosto);++i) {
        korvaus[(unsigned char)aakkosto[i]] = korvaavat[i];
    }
	
	for (i=0;i<strlen(aakkosto);++i) {
		mj[i] = korvaus[(unsigned char) mj[i]];
	}
}