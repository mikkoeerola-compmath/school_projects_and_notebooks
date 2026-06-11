"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 9.7 Yhteystiedot sanakirjana
"""


def read_file(tiedosto_nimi):
    """
    Lukee tiedostosta yhteystietoja ja tallentaa ne hakemistoksi. Tiedostossa
    ensimmäisellä rivillä on otsikot. Ulomman sanakirjan avaimet ovat rivin
    alussa ja ovat kontaktien nimiä ja niihin liittyy yhteystiedot sanakirja
    muodossa. Sisemmän sanakirjan avaimet ovat otsikkorivillä esitellyt tiedot
    ja hyötykuormat kyseiset tiedot littyen tiettyy kontaktiin. Oletuksena on,
    että tiedosto on oikeassa muodossa.

    :param tiedosto_nimi: str, Tiedoston nimi, johon tiedot ovat tallennettu
    :return: dict, tallennetut tiedot kerrotussa muodossa
    """
    try:
        tiedosto = open(tiedosto_nimi, mode = "r")

        rivi_numero = 1
        hakemisto = {}
        otsikot = []

        for rivi in tiedosto:
            rivi = rivi.rstrip()
            rivin_osat = rivi.split(";")
            if rivi_numero == 1:
                del rivin_osat[0]
                otsikot = rivin_osat
            else:
                key = rivin_osat.pop(0)
                tiedot = rivin_osat
                index = 0
                yhteystiedot = {}
                for tieto in tiedot:
                    yhteystiedot[otsikot[index]] = tieto
                    index += 1
                hakemisto[key] = yhteystiedot
            rivi_numero += 1

        tiedosto.close()

        return hakemisto

    except OSError:
        print("Virhe avatessa tiedostoa")
        return None


def main():
    read_file("contacts.csv")


if __name__ == "__main__":
    main()