#include "tetris.h"

int rivitaynna(char ruudukko[10]) {
	int rivi_taynna = 1;
	int j;
	for (j = 0; j < 10; ++j) {
            if (ruudukko[j] == ' ') {
                rivi_taynna = 0;
                break;
            }
        }
	return rivi_taynna;
}

void paivita(char ruudukko[20][10]) {
    int taydet_rivit = 0;
	int i;

    /* Käydään ruudukko alhaalta ylöspäin */
    for (i = 19; i >= 0; --i) {
		int j = i;
		int k;
		int l;

        /* Tutkitaan onko peräkkäisiä rivejä täynnä */
        while (rivitaynna(ruudukko[j])) {
			--j;
			++taydet_rivit;
		}
		
		if (taydet_rivit > 0) {
			for (k = i-taydet_rivit; k >= 0; --k) {
                for (l = 0; l < 10; ++l) {
                    ruudukko[k+taydet_rivit][l] = ruudukko[k][l];
                }
            }

            /* Tyhjennetään ylimmät rivit */
		    for (k = taydet_rivit; k >= 0; --k) {
		    	for (l = 0; l < 10; ++l) {
                     ruudukko[k][l] = ' ';
                }
		    }
            
		    taydet_rivit = 0;
        }
	}
}