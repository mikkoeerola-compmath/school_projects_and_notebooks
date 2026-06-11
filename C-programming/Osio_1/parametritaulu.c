#include <stdio.h>
#include <string.h>

// Funktio laskemaan leveydet
void laskeLeveydet(char *parametrit[], int parametrienMaara, int *leveys1, int *leveys2) {
    *leveys1 = snprintf(NULL, 0, "%d", parametrienMaara) + 2; // +2 ottaa huomioon välilyönnit
    *leveys2 = 2; // Vähintään kaksi merkkiä väliä reunojen ja tekstin välissä

    for (int i = 0; i < parametrienMaara; i++) {
        int pituus = strlen(parametrit[i]);
        if (pituus > *leveys2) {
            *leveys2 = pituus + 2; // +2 ottaa huomioon välilyönnit
        }
    }
}

// Funktio tulostamaan taulukko
void tulostaTaulukko(char *parametrit[], int parametrienMaara, int leveys1, int leveys2) {
    printf("%-*s| %-*s\n", leveys1, "Indeksi", leveys2, "Parametri");
    
    for (int i = 0; i < parametrienMaara; i++) {
        printf("%-*d| %-*s\n", leveys1, i + 1, leveys2, parametrit[i]);
        
        if (i < parametrienMaara - 1) {
            for (int j = 0; j < leveys1 + leveys2 + 1; j++) {
                printf("-");
            }
            printf("\n");
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc <= 1) {
        printf("Ei parametreja.\n");
        return 1;
    }

    int leveys1, leveys2;

    // Lasketaan leveydet
    laskeLeveydet(argv + 1, argc - 1, &leveys1, &leveys2);

    // Tulostetaan taulukko
    printf("#");
    for (int i = 0; i < leveys1 + leveys2 + 2; i++) {
        printf("#");
    }
    printf("#\n");

    tulostaTaulukko(argv + 1, argc - 1, leveys1, leveys2);

    printf("#");
    for (int i = 0; i < leveys1 + leveys2 + 2; i++) {
        printf("#");
    }
    printf("#\n");

    return 0;
}