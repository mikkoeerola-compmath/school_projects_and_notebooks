#include "asteet.h"

float muunna(Lampotila a, Asteikko b) {
    if (a.asteikko == b) {
        return a.lampotila; /* Ei tarvitse muuntaa, jos asteikot ovat samat */
    }

    /* Muunnetaan Celsius-asteikolta */
    if (a.asteikko == Celsius) {
        if (b == Fahrenheit) {
            return a.lampotila * 1.8 + 32;
        } else if (b == Kelvin) {
            return a.lampotila + 273.15;
        }
    }

    /* Muunnetaan Fahrenheit-asteikolta */
    if (a.asteikko == Fahrenheit) {
        if (b == Celsius) {
            return (a.lampotila - 32) / 1.8;
        } else if (b == Kelvin) {
            return (a.lampotila - 32) / 1.8 + 273.15;
        }
    }

    /* Muunnetaan Kelvin-asteikolta */
    if (a.asteikko == Kelvin) {
        if (b == Celsius) {
            return a.lampotila - 273.15;
        } else if (b == Fahrenheit) {
            return (a.lampotila - 273.15) * 1.8 + 32;
        }
    }

    return 0; /* Palautetaan 0 oletuksena, jos jotain menee pieleen */
}

float erotus(Lampotila a, Lampotila b, Asteikko c) {
    /* Muunnetaan molemmat lämpötilat c-asteikolle ja lasketaan erotus */
    float a_c = muunna(a, c);
    float b_c = muunna(b, c);

    return a_c - b_c;
}