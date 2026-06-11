#include "utf8.h"
#include <limits.h>
#include <stdio.h>

void utf8_koodaa(unsigned int merkki, unsigned char utf8[]) {
	int bits = 0;
	int i;
	int size = sizeof(unsigned int)*CHAR_BIT;
	
	for (i=0; i<size; ++i) {
		if ((merkki >> i) & 1) {
			bits = i;
		}
	}
	
	if (bits < 7) {
		utf8[0]=merkki;
		utf8[1]='\0';
		
	} else if (bits < 11) {
		utf8[0]=0;
		utf8[1]=0;
		utf8[2]='\0';
		
		utf8[0] = utf8[0] | (1<<7);
		utf8[0] = utf8[0] | (1<<6);
		utf8[1] = utf8[1] | (1<<7);
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<i)) {
				utf8[1] = utf8[1] | (1<<i);
			}
		}
		
		for (i = 0; i<5; ++i) {
			if ( merkki & (1<<(i+6))) {
				utf8[0] = utf8[0] | (1<<i);
			}
		}
		
	} else if (bits < 16) {
		utf8[0]=0;
		utf8[1]=0;
		utf8[2]=0;
		utf8[3]='\0';
		
		utf8[0] = utf8[0] | (1<<7);
		utf8[0] = utf8[0] | (1<<6);
		utf8[0] = utf8[0] | (1<<5);
		utf8[1] = utf8[1] | (1<<7);
		utf8[2] = utf8[1] | (1<<7);
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<i)) {
				utf8[2] = utf8[2] | (1<<i);
			}
		}
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<(i+6))) {
				utf8[1] = utf8[1] | (1<<i);
			}
		}
		
		for (i = 0; i<5; ++i) {
			if ( merkki & (1<<(i+12))) {
				utf8[0] = utf8[0] | (1<<i);
			}
		}
		
	} else if (bits < 21) {
		utf8[0]=0;
		utf8[1]=0;
		utf8[2]=0;
		utf8[3]=0;
		utf8[4]='\0';
		
		utf8[0] = utf8[0] | (1<<7);
		utf8[0] = utf8[0] | (1<<6);
		utf8[0] = utf8[0] | (1<<5);
		utf8[0] = utf8[0] | (1<<4);
		utf8[1] = utf8[1] | (1<<7);
		utf8[2] = utf8[1] | (1<<7);
		utf8[3] = utf8[1] | (1<<7);
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<i)) {
				utf8[2] = utf8[2] | (1<<i);
			}
		}
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<(i+6))) {
				utf8[1] = utf8[1] | (1<<i);
			}
		}
		
		for (i = 0; i<6; ++i) {
			if ( merkki & (1<<(i+12))) {
				utf8[0] = utf8[0] | (1<<i);
			}
		}
		
		for (i = 0; i<4; ++i) {
			if ( merkki & (1<<(i+18))) {
				utf8[0] = utf8[0] | (1<<i);
			}
		}
	}
}
/*
int main(void)
{

  unsigned int koodit[6] = {228, 49340, 49457, 12477, 12491, 12540};
  unsigned char utf8[5];
  int i = 0;

  for(i = 0; i < 6; ++i)
  {
    utf8_koodaa(koodit[i], utf8);
    printf("%s\n", utf8);
  }
  return 0;
}*/