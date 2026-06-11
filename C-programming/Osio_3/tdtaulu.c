#include "tdtaulu.h"
#include <stdlib.h>
#include <string.h>

TdTaulu *luoTdTaulu(unsigned int n, unsigned int alkioKoko, const char *tdNimi) {
    TdTaulu *tdt = (TdTaulu *)malloc(sizeof(TdTaulu));
	unsigned char nolla = 0;
	unsigned int i = 0;

    if (tdt == NULL) {
        return NULL; /* Muistin varaaminen epäonnistui */
    }

    tdt->n = n;
    tdt->alkioKoko = alkioKoko;

    /* Kopioidaan tdNimi */
    tdt->tdNimi = (const char *)malloc(strlen(tdNimi) + 1);
    if (tdt->tdNimi == NULL) {
        free(tdt);
        return NULL; /* Muistin varaaminen epäonnistui */
    }
    strcpy((char *)tdt->tdNimi, tdNimi);

    tdt->td = fopen(tdNimi, "wb+");
	
	if (tdt->td == NULL) {
        free((char *)tdt->tdNimi);
        free(tdt);
        return NULL; /* Tiedoston avaaminen epäonnistui */
    }
	
	/* Kirjoitetaan tiedoston alkuun arvot n ja alkioKoko */
    fwrite(&n, sizeof(unsigned int), 1, tdt->td);
    fwrite(&alkioKoko, sizeof(unsigned int), 1, tdt->td);

    /* Nollataan loput tiedostosta */
    for (i = 0; i < n * alkioKoko; ++i) {
        fwrite(&nolla, 1, 1, tdt->td);
    }

    return tdt;
}

TdTaulu *avaaTdTaulu(const char *tdNimi) {
    TdTaulu *tdt = (TdTaulu *)malloc(sizeof(TdTaulu));

    if (tdt == NULL) {
        return NULL; /* Muistin varaaminen epäonnistui */
    }

    /* Kopioidaan tdNimi */
    tdt->tdNimi = (const char *)malloc(strlen(tdNimi) + 1);
    if (tdt->tdNimi == NULL) {
        free(tdt);
        return NULL; /* Muistin varaaminen epäonnistui */
    }
    strcpy((char *)tdt->tdNimi, tdNimi);

    tdt->td = fopen(tdNimi, "rb+");
    if (tdt->td == NULL) {
        free((char *)tdt->tdNimi);
        free(tdt);
        return NULL; /* Tiedoston avaaminen epäonnistui */
    }

    /* Luetaan tiedoston alusta arvot n ja alkioKoko */
    fread(&tdt->n, sizeof(unsigned int), 1, tdt->td);
    fread(&tdt->alkioKoko, sizeof(unsigned int), 1, tdt->td);

    return tdt;
}

void vapautaTdTaulu(TdTaulu *tdt) {
    fclose(tdt->td);
    free((char *)tdt->tdNimi);
    free(tdt);
}

int tdtLue(TdTaulu *tdt, unsigned int i, unsigned int lkm, void *arvo) {
    /* Tarkista, että luku ei mene tiedoston loppurajan yli */
    if (i + lkm > tdt->n) {
        return 1; /* Laiton indeksi */
    }

    /* Siirry kohtaan, josta luku aloitetaan */
    fseek(tdt->td, sizeof(unsigned int) + sizeof(unsigned int) + i * tdt->alkioKoko, SEEK_SET);

    /* Lue tiedostosta arvot */
    fread(arvo, tdt->alkioKoko, lkm, tdt->td);

    return 0;
}

int tdtKirj(TdTaulu *tdt, unsigned int i, unsigned int lkm, const void *arvo) {
    /* Tarkista, että kirjoitus ei mene tiedoston loppurajan yli */
    if (i + lkm > tdt->n) {
        return 1; /* Laiton indeksi */
    }

    /* Siirry kohtaan, johon kirjoitetaan */
    fseek(tdt->td, sizeof(unsigned int) + sizeof(unsigned int) + i * tdt->alkioKoko, SEEK_SET);

    /* Kirjoita tiedostoon arvot */
    fwrite(arvo, tdt->alkioKoko, lkm, tdt->td);

    return 0;
}