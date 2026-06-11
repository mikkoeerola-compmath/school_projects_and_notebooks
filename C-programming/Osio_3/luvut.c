#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(double *)a > *(double *)b) - (*(double *)a < *(double *)b);
}

int main(void) {
    size_t koko = 2;
    size_t lukumaara = 0;
    double *luvut = malloc(koko * sizeof(double));
	double luku;
	double summa = 0.0;
	size_t i = 0;

    if (!luvut) {
        fprintf(stderr, "Muistin varaaminen epäonnistui\n");
        return 1;
    }

    while (scanf("%lf", &luku) == 1) {
		double *uusi_luvut = NULL;
        if (lukumaara == koko) {
            /* Taulukko täynnä, tuplaa koko ja varaa uudelleen muisti */
            koko *= 2;
            uusi_luvut = realloc(luvut, koko * sizeof(double));
            if (!uusi_luvut) {
                fprintf(stderr, "Muistin varaaminen epäonnistui\n");
                free(luvut);
                return 1;
            }
            luvut = uusi_luvut;
        }

        luvut[lukumaara++] = luku;
    }
	
	luvut = realloc(luvut, sizeof(double)*lukumaara);

    /* Lajittele luvut */
    qsort(luvut, lukumaara, sizeof(double), compare);

    /* Tulosta luvut, lukumäärä, summa ja keskiarvo */
    printf("Luettiin %ld lukua:", lukumaara);
    for (i = 0; i < lukumaara; ++i) {
        printf(" %.3f", luvut[i]);
    }

    for (i = 0; i < lukumaara; ++i) {
        summa += luvut[i];
    }

    printf("\nSumma: %.3f\n", summa);
    printf("Keskiarvo: %.3f\n", summa / lukumaara);

    /* Vapauta dynaamisesti varattu muisti */
    free(luvut);

    return 0;
}