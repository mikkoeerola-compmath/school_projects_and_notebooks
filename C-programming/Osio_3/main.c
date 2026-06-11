#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>
#include <string.h>

#include "signaalit.h"

int main(int argc, char *argv[])
{
	char syoterivi[100]; 
    int* taulukko = NULL; 
    int taulukonKoko = 0; 
    int lkm = 0; 
	
	signal(SIGFPE, hoidaSIGFPE);
    signal(SIGSEGV, hoidaSIGSEGV);
	
	while (1) {
        
        if (fgets(syoterivi, sizeof(syoterivi), stdin) == NULL) {
            break;
        }
		
		switch (setjmp(paluuTila)) {
			case 0: {
				char komento[20];
                int a, b;
				
				if (sscanf(syoterivi, "lisää %d %d", &a, &b) == 2) {
                        
                        if (lkm == taulukonKoko) {
                            taulukonKoko += 5; /* Voit säätää tarvittaessa kasvatusaskelta */
                            taulukko = realloc(taulukko, taulukonKoko * sizeof(int));
                        }

                        
                        arvo = a/b;
						taulukko[lkm++] = arvo;
						
                    } else if (sscanf(syoterivi, "tulosta %d", &a) == 1) {
                     
						printf("%d\n", taulukko[a]);
						
                    } else if (strcmp(syoterivi, "tulosta\n") == 0) {
                        // Tulosta kaikki arvot
                        for (int i = 0; i < lkm; i++) {
							if (i == 0) {
								printf("%d", taulukko[i]);
							} else {
								printf(" %d", taulukko[i]);
							}
                        }
                        printf("\n");
                    } else {
                        goto LOPPU;
                    }
            }
		    case SIGFPE:
                printf("Aiheutui signaali SIGFPE\n");
                break;

            case SIGSEGV:
                printf("Aiheutui signaali SIGSEGV\n");
                break;

            default:
                printf("Aiheutui signaali UNKNOWN\n");
                break;

			}
		}
		LOPPU:
		exit(1);
}