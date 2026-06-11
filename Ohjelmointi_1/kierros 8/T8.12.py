"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 8.12 Pisteiden laskentaa
"""


def laske_pisteet(tiedoston_nimi):
    """
    Laskee tekstimuotoisesta tiedostosta löytyvät pisteet pelaajittain
    ja tallentaa ne sanakirjana. Oletuksena, että tiedostossa on aina yhdellä
    rivillä pelaajan nimi ja pisteet välilyönnillä erotettuna.

    :param tiedoston_nimi: str, tiedoston nimi, jossa pisteet on
    :return: dict, avaimina pelaajan nimi ja arvona kokonaispisteet
    """
    try:
        tiedosto = open(tiedoston_nimi, mode="r")
        piste_dict = {}
        for rivi in tiedosto:
            rivi = rivi.rstrip()
            rivi_eroteltuna = rivi.split()
            try:
                try:
                    pisteet = int(rivi_eroteltuna[1])
                except ValueError:
                    print("There was an erroneous score in the file:")
                    print(rivi_eroteltuna[1])
                    return None
                if rivi_eroteltuna[0] in piste_dict:
                    piste_dict[rivi_eroteltuna[0]] += pisteet
                else:
                    piste_dict[rivi_eroteltuna[0]] = pisteet
            except IndexError:
                print("There was an erroneous line in the file:")
                print(rivi)
                return None
        tiedosto.close()
    except OSError:
        print("There was an error in reading the file.")
        return None
    return piste_dict


def main():
    tiedoston_nimi = input("Enter the name of the score file: ")
    piste_dict = laske_pisteet(tiedoston_nimi)
    if piste_dict == None:
        return
    else:
        print("Contestant score:")
        for i in sorted(piste_dict.keys()):
            print(i, piste_dict[i])


if __name__ == "__main__":
    main()
