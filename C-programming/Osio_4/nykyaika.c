#include <time.h>
#include <stdio.h>

int main(void) {
	time_t aika = time(NULL);
    struct tm *b = localtime(&aika);
	size_t n = 23;
	char s[23];


    switch(b->tm_wday) {
	    case 1: {
	        printf("Maanantai");
			break;
		}
	    case 2: {
	       printf("Tiistai");
		   break;
		}
	    case 3: {
	       printf("Keskiviikko");
		   break;
		}
	    case 4: {
	       printf("Torstai");
		   break;
		}
	    case 5: {
	       printf("Perjantai");
		   break;
		}
	    case 6: {
	       printf("Lauantai");
		   break;
		}
	    case 7: {
	       printf("Sunnuntai");
		   break;
		}
    }

    strftime(s, n, " %d.%m.%Y klo %H:%M\n",b);
	printf("%s",s);
	
	return 0;
}