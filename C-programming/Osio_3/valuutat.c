#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <stdlib.h>

struct Valuutta {
	double kurssi;
	char* nimi;
};

typedef struct Valuutta Valuutta;

double hae_kurssi(const Valuutta *kurssit, size_t lukumaara, const char *nimi) {
	size_t i = 0;
    for (i = 0; i < lukumaara; ++i) {
        if (strcmp(kurssit[i].nimi, nimi) == 0) {
            return kurssit[i].kurssi;
        }
    }
    return -1.0; 
}

void paivita_kurssi(Valuutta **kurssit, size_t *lukumaara, const char *nimi, double uusi_kurssi) {
	size_t i = 0;
	int is_new = 1;
    for (i = 0; i < *lukumaara; ++i) {
        if (strcmp((*kurssit)[i].nimi, nimi) == 0) {
            /* Päivitetään kurssi, jos valuutta löytyy */
            (*kurssit)[i].kurssi = uusi_kurssi;
            is_new = 0;
        }
    }
	
	if(!is_new) {
		return;
	} else {
	/* Lisätään uusi valuutta */
		Valuutta uusi_valuutta;
		/* Varataan muistia uudelle taulukolle */
		*kurssit = realloc(*kurssit, (*lukumaara + 1) * sizeof(Valuutta));
		uusi_valuutta.kurssi = uusi_kurssi;
		uusi_valuutta.nimi = malloc(strlen(nimi)+1);
		strcpy(uusi_valuutta.nimi, nimi);
		
		if (!(*kurssit)) {
			fprintf(stderr, "Muistin varaaminen epäonnistui\n");
			exit(EXIT_FAILURE);
		}

		(*kurssit)[*lukumaara] = uusi_valuutta;
		/* printf("%s %f\n", (*kurssit)[*lukumaara].nimi, (*kurssit)[*lukumaara].kurssi);*/
		++(*lukumaara);
	}
}

void vapauta_kurssit(Valuutta *kurssit, size_t lukumaara) {
	size_t i = 0;
    for (i = 0; i < lukumaara; ++i) {
        free(kurssit[i].nimi);
    }
    free(kurssit);
}

int vertaa_valuuttoja(const void *a, const void *b) {
    return strcmp(((Valuutta *)a)->nimi, ((Valuutta *)b)->nimi);
}


int main(void) {
	size_t lkm = 0;
	Valuutta *kurssit = malloc(lkm*sizeof(Valuutta));
	char rivi[81];
	char f[81];
	double x = 0.0;
	char nimi[4];
	size_t i = 0;
	
	while (1) {
		fgets(rivi, 81, stdin);
		sscanf(rivi, "%s", f);
		if (strcmp(f, "kurssi") == 0) {
			sscanf(rivi, "%*s%s%lf", nimi, &x);
			paivita_kurssi(&kurssit, &lkm, nimi, x);
	    } else if(strcmp(f,"muunna") == 0) {
			sscanf(rivi, "%*s%lf%s", &x, nimi);
		    if (hae_kurssi(kurssit, lkm, nimi) < 0) {
				printf("Valuutan %s kurssia ei ole tiedossa!\n", nimi);
			} else {
				double eurot = x / hae_kurssi(kurssit, lkm, nimi);
				printf("%.3f %s = %.3f EUR\n", x, nimi, eurot);
			}
		} else if ( strcmp(f, "kurssit") == 0) {
			qsort(kurssit, lkm, sizeof(Valuutta),
               vertaa_valuuttoja);
            for (i = 0; i < lkm; ++i) {
                printf("%s %.3f\n", kurssit[i].nimi, kurssit[i].kurssi);
            }
	    } else if (strcmp(f,"lopeta") == 0) {
			vapauta_kurssit(kurssit, lkm);
			return 0;
		}
		else {
			printf("Tunnistamaton komento");
		}
	}
	return 0;
}