#include "kolmijako.h"
#include <stdlib.h>

void kolmijako_gen(void *t, size_t n, size_t koko, size_t vipu1, size_t vipu2,
                   int (*vrt)(const void *, const void *), size_t *p1, size_t *p2) {
    char *taulu = (char *)t;
    char *vipu1_osoitin = taulu + vipu1 * koko;
    char *vipu2_osoitin = taulu + vipu2 * koko;
    
    /* Alustetaan vipualkiot */
    size_t pienempi_vipu = (vrt(vipu1_osoitin, vipu2_osoitin) < 0) ? vipu1 : vipu2;
    size_t suurempi_vipu = (pienempi_vipu == vipu1) ? vipu2 : vipu1;
    
    /* Vaihdetaan vipualkiot taulukon alkuun */
    for (size_t i = 0; i < koko; ++i) {
        char temp = taulu[pienempi_vipu * koko + i];
        taulu[pienempi_vipu * koko + i] = taulu[i];
        taulu[i] = temp;
    }
    
    /* Vertailu ja vaihto */
    size_t pienempi_indeksi = 0;
    size_t suurempi_indeksi = n - 1;
    
    for (size_t i = 1; i < n; ++i) {
        char *nykyinen = taulu + i * koko;
        if (vrt(nykyinen, taulu) < 0) {
            /* Nykyinen on pienempi kuin vipualkiot, vaihdetaan pienemmän kanssa */
            for (size_t j = 0; j < koko; ++j) {
                char temp = taulu[pienempi_indeksi * koko + j];
                taulu[pienempi_indeksi * koko + j] = taulu[i * koko + j];
                taulu[i * koko + j] = temp;
            }
            ++pienempi_indeksi;
        } else if (vrt(nykyinen, vipu2_osoitin) > 0) {
            /* Nykyinen on suurempi kuin vipualkiot, vaihdetaan suuremman kanssa */
            for (size_t j = 0; j < koko; ++j) {
                char temp = taulu[suurempi_indeksi * koko + j];
                taulu[suurempi_indeksi * koko + j] = taulu[i * koko + j];
                taulu[i * koko + j] = temp;
            }
            --suurempi_indeksi;
        }
    }
    
    /* Vaihdetaan suurempi vipu oikealle paikalle */
    for (size_t i = 0; i < koko; ++i) {
        char temp = taulu[suurempi_vipu * koko + i];
        taulu[suurempi_vipu * koko + i] = taulu[suurempi_indeksi * koko + i];
        taulu[suurempi_indeksi * koko + i] = temp;
    }
    
    *p1 = pienempi_indeksi;
    *p2 = suurempi_indeksi + 1;
}