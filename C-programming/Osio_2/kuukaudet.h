enum
{
 TAMMIKUU = 0,
 HELMIKUU,
 MAALISKUU,
 HUHTIKUU,
 TOUKOKUU,
 KESAKUU,
 HEINAKUU,
 ELOKUU,
 SYYSKUU,
 LOKAKUU,
 MARRASKUU,
 JOULUKUU,
 KK_LKM
};

const char *KK_NIMET[KK_LKM] = {"tammikuu", "helmikuu", "maaliskuu", "huhtikuu",
"toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu",
"joulukuu"};

const char KK_PAIVAT[2][KK_LKM] = {{31,28,31,30,31,30,31,31,30,31,30,31},
{31,29,31,30,31,30,31,31,30,31,30,31}};

int karkausvuosi(int vuosiluku);

char kkPituus(const char *kkNimi, int vuosiluku);