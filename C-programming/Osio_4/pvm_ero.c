#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

#include "pvm_ero.h"

void pvm_ero(const char *pvm1, const char *pvm2) {
	struct tm a = {0};
	struct tm b = {0};
	time_t aikaA, aikaB;
	int da, ka, va = 0;
	int db, kb, vb = 0;
	int result1, result2;
	double inval = 0;
	char s1[50];
	char s2[50];
	char s[1000];
	
	result1 = sscanf(pvm1, "%2d.%2d.%4d", &da, &ka, &va);
	result2 = sscanf(pvm2, "%2d.%2d.%4d", &db, &kb, &vb);
	
	if(result1 != 3 || result2 != 3) {
		fprintf(stderr, "Parametri \"%s\" tai \"%s\" on laiton!\n",
			        pvm1, pvm2);
		return;
	}
	a.tm_mday = da;
	a.tm_mon = ka-1;
	a.tm_year = va-1900;
	a.tm_isdst = 0;
	
	b.tm_mday = db;
	b.tm_mon = kb-1;
	b.tm_year = vb-1900;
	b.tm_isdst = 0;
	
	aikaA = mktime(&a);
	aikaB = mktime(&b);
	
	/*printf("%d %d %d %d\n", va, a.tm_year+1900, vb, b.tm_year+1900);*/
	
	if (da != a.tm_mday || ka != a.tm_mon+1
	     || va != a.tm_year+1900) {
		fprintf(stderr, "Parametri \"%s\" tai \"%s\" on laiton!\n",
			        pvm1, pvm2);
		return;
	} else {
		if (db != b.tm_mday || kb != b.tm_mon+1
	         || vb != b.tm_year+1900) {
		    fprintf(stderr, "Parametri \"%s\" tai \"%s\" on laiton!\n",
	                pvm1, pvm2);
			return;
		}
	}
	
	inval = difftime(aikaA, aikaB);
	if(inval<0) {inval = -inval;}
	
	inval = inval / (60*60*24)+1;
	
	setlocale(LC_TIME, "fi_FI.utf8");
	
	strftime(s1, 50, "%A %d.%m.%Y", &a);
	strftime(s2, 50, "%A %d.%m.%Y", &b);
	
	if( difftime(aikaA, aikaB) > 0) {
		sprintf(s, "%s --> %s: yhteensä %.0f päivää\n",s2, s1, inval);
	} else {
		sprintf(s, "%s --> %s: yhteensä %.0f päivää\n",s1, s2, inval);
	}
	
	printf("%s", s);
}

/*int main(void) {
	pvm_ero("26.04.2016", "09.5.2013");
    pvm_ero("29.2.1900", "29.2.2000");
    pvm_ero("05.08.2016", "21.08.2016");
    pvm_ero("010.8.1957", "15.7.1930");
	
	return 0;
}*/