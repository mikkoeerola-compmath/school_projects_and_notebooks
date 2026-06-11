"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.7 akronyymin muodostaminen
"""


def create_an_acronym(nimi):
    """
    Muodostetaan nimestä akronyymi eli nimien ensimmäiset kirjaimet isolla

    :param nimi: str, nimi, josta akronyymi muodostetaan
    :return: str, akronyymi
    """
    akronymi = ""
    nimen_osat = nimi.split(" ")
    for i in range(len(nimen_osat)):
        akronymi += nimen_osat[i][0]
    return akronymi.upper()


def main():
    ak = create_an_acronym(input())
    print(ak)

if __name__ == "__main__":
    main()
