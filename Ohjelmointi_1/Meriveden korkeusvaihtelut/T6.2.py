"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Projekti 6.2: meriveden korkeusvaihtelut
"""


def lue_syotteet():
    """
    Luetaan mittaustulokset käyttäjältä ja palautetaan ne listana
    :return: list, mittaustulokset listana syötetyssä järjestyksessä
    """
    mittaukset = []
    suorita_kysely = True
    while suorita_kysely:  # luetaan syötteitä kunnes lippu muutetaan
        mittaus = input()
        if mittaus == "":
            suorita_kysely = False
        else:
            mittaukset.append(float(mittaus))
    return mittaukset


def laske_mediaani(mittaus_lista):
    """
    Lasketaan annetusta listasta siinä esiintyvien lukujen mediaani
    :param mittaus_lista: list, jossa kaikki alkiot reaalilukuja
    :return: float, alkioiden mediaani
    """
    # järjestetään lista suuruusjärjestykseen
    mittaus_lista = sorted(mittaus_lista)
    if len(mittaus_lista) % 2 == 1:  # mittauksia parillinen vai pariton määrä
        return mittaus_lista[len(mittaus_lista) // 2]
    else:
        indeksi = len(mittaus_lista) // 2
        keskiarvo = (mittaus_lista[indeksi - 1] + mittaus_lista[indeksi]) / 2
        return keskiarvo


def laske_keskiarvo(mittaus_lista):
    """
    Laskee listassa annettujen lukujen keskiarvon
    :param mittaus_lista: list, alkiot reaalilukuja
    :return: float, alkioiden keskiarvo
    """
    summa = 0  # lasketaan summa kaikista listan alkioista
    for i in range(len(mittaus_lista)):
        summa += mittaus_lista[i]
    return summa / len(mittaus_lista)


def laske_keskihajonta(mittaus_lista):
    """
    Laskee listassa annettujen lukujen keskihajonnan

    :param mittaus_lista: list, alkiot reaalilukuja
    :return: float, alkioiden keskihajonta
    """
    from math import sqrt
    # lasketaan listan alkioiden keskiarvo laske_keskiarvo funktiolla
    ka = laske_keskiarvo(mittaus_lista)
    virheneliosummat = 0  # lasketaan virheiden neliöistä summa
    for i in range(len(mittaus_lista)):
        virheneliosummat += (ka - mittaus_lista[i]) ** 2
    varianssi = virheneliosummat / (len(mittaus_lista) - 1)
    return sqrt(varianssi)


def main():
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")
    mittaus_tulokset = lue_syotteet()  # luetaan syötteet käyttäjältä
    if len(mittaus_tulokset) < 2:
        print("Error: At least two measurements must be entered!")
    else:
        # tallennetaan tunnusluvut muuttujiin
        minimum = min(mittaus_tulokset)
        maximum = max(mittaus_tulokset)
        mediaani = laske_mediaani(mittaus_tulokset)
        keskiarvo = laske_keskiarvo(mittaus_tulokset)
        keskihajonta = laske_keskihajonta(mittaus_tulokset)
        # tulostuksen muotoilun vuoksi tallennetaan tunnuslukujen nimet listaan
        nimet = ["Minimum:", "Maximum:", "Median:", "Mean:", "Deviation:"]
        # tulostetaan tunnusluvun nimet listasta ja tunnusluvut muuttujista
        print(f"{nimet[0]:<10} {minimum:.2f} cm")
        print(f"{nimet[1]:<10} {maximum:.2f} cm")
        print(f"{nimet[2]:<10} {mediaani:.2f} cm")
        print(f"{nimet[3]:<10} {keskiarvo:.2f} cm")
        print(f"{nimet[4]:<10} {keskihajonta:.2f} cm")


if __name__ == "__main__":
    main()
