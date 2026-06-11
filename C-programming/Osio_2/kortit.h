enum Maa {
    HERTTA = 1,
    RUUTU,
    RISTI,
    PATA
};

enum Arvo {
    ASSA = 1,
    KAKKONEN,
    KOLMONEN,
    NELONEN,
    VIITONEN,
    KUUTONEN,
    SEISKA,
    KASI,
    YSI,
    KYMPPI,
    JATKA,
    ROUVA,
    KUNKKU
};

enum {
	MAA_LKM = 4,
	MAA_KOKO = 13,
	KORTTI_LKM = MAA_KOKO*MAA_LKM
};

typedef enum Maa Maa;
typedef enum Arvo Arvo;

extern const char *MAIDEN_NIMET[MAA_LKM+1];
extern const char *KORTTIEN_NIMET[MAA_KOKO+1];

struct Kortti {
    Maa maa;
    Arvo arvo;
};

typedef struct Kortti Kortti;

void tulostaKortti(Kortti kortti);
void tulostaKorttiOs(const Kortti *korttiOs);