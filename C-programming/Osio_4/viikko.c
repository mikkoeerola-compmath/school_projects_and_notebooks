#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#include "viikko.h"

 void viikko(int pv, int kk, int vuosi) {
	 struct tm *aika = malloc(sizeof(struct tm));
	 int i = 0;
	 char s[40];
	 time_t temp;
	 
	 aika->tm_mday = pv;
	 aika->tm_mon = kk-1;
	 aika->tm_year = vuosi-1900;
	 
	 temp = mktime(aika);
	 
	 aika = localtime(&temp);
	 
	 if (aika->tm_wday == 0) {
		 aika->tm_mday = aika->tm_mday - 6;
	 } else {
		 aika->tm_mday = aika->tm_mday - aika->tm_wday + 1;
	 }
	 
	 temp = mktime(aika);
	 aika = localtime(&temp);
	 
	 for (i = 0; i<7; ++i) {
		 strftime(s, 40, "%A %d. %B %Y", aika);
		 printf("%s\n", s);
		 aika->tm_mday += 1;
		 temp = mktime(aika);
		 aika = localtime(&temp);
	 }
 }