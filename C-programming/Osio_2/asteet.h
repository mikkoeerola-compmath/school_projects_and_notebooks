enum Asteikko {
    Celsius,
    Fahrenheit,
    Kelvin
};

struct Lampotila {
    float lampotila;
    enum Asteikko asteikko;
};

typedef enum Asteikko Asteikko;
typedef struct Lampotila Lampotila;

float muunna(Lampotila a, Asteikko b);
float erotus(Lampotila a, Lampotila b, Asteikko c);