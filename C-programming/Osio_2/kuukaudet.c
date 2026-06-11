#include "kuukaudet.h"
#include <ctype.h>
#include <string.h>
#include <stdio.h>

int karkausvuosi(int vuosiluku) {
	return ((vuosiluku % 4 == 0) & (vuosiluku % 100 != 0)) || vuosiluku % 400 == 0;
}

char kkPituus(const char *kkNimi, int vuosiluku) {
    char lowercaseName[10];
	int i;
	int monthIndex = -1;
	
    for (i = 0; i < kkNimi[i]; i++) {
        lowercaseName[i] = tolower(kkNimi[i]);
    }
    lowercaseName[i] = '\0';

    
    for (i = 0; i < KK_LKM; i++) {
        if (strcmp(lowercaseName, KK_NIMET[i]) == 0) {
            monthIndex = i;
            break;
        }
    }

    if (monthIndex == -1) {
        return -1;
    }

    return KK_PAIVAT[karkausvuosi(vuosiluku)][monthIndex];
}

/*
char kkPituus(const char *kkNimi, int vuosiluku) {
	char days = -1;
	int i;
	
	for (i = 0; i < KK_LKM; ++i) {
		int j;
		
		for (j=0;j<strlen(kkNimi);++j) {
			printf("%d %c %c\n", j, KK_NIMET[i][j], tolower(kkNimi[j]));
			if (KK_NIMET[i][j] == tolower(kkNimi[j])) {
				if (j+1 == strlen(kkNimi)) {
				    days = KK_PAIVAT[karkausvuosi(vuosiluku)][i];
					return days;
			    }
				continue;
			} else {
				break;
			}
		}
		

		    if (KK_NIMET[i][j] == tolower(kkNimi[j])) {
				continue;
			} else {
				break;
			}
			
			if (j+1 == strlen(kkNimi)) {
				days = KK_PAIVAT[karkausvuosi(vuosiluku)][i];
			}
		}
    }
	return days;
}*/

/*
int main() {
	printf("Helmikuu 2016: %d päivää\n", kkPituus("Helmikuu", 2016));
    printf("Helmikuu 2100: %d päivää\n", kkPituus("helmikuu", 2100));
    printf("Helmi kuu 2100: %d päivää\n", kkPituus("helmi kuu", 2100));
	printf("Kesäkuu 2100: %d päivää\n", kkPituus("kesäkuu", 2100));
	printf("Lokakuu 2100: %d päivää\n", kkPituus("lokAKuu", 2100));
	
	return 0;
}*/
