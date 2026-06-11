"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.13 Pisin järjestetty alimerkkijono
"""


def longest_substring_in_order(teksti):
    """
    Etsii pisimmän aakkosjärjestyksessä olevan alimerkkijonon.
    palauttaa yhtäpitkistä alimerkkijonoista lähimpänä merkkijonon
    alkua olevan.

    :param teksti: str, tutkittava merkkijono pienin kirjaimin
    :return: str, pisin aakkosjärjestyksessä löytynyt merkkijon
     + erikoistapaukset
    """
    if len(teksti) <= 1:
        return teksti
    pisin = ""
    for i in range(len(teksti) - 1):
        j = i
        alimerkkijono = teksti[i]
        while j < len(teksti) - 1 and teksti[j] < teksti[j+1]:
            alimerkkijono += teksti[j+1]
            j += 1
        if len(alimerkkijono) > len(pisin):
            pisin = alimerkkijono
    return pisin


def main():
    pisin_alimerkkijono = longest_substring_in_order("aaaac")
    print(pisin_alimerkkijono)


if __name__ == "__main__":
    main()
