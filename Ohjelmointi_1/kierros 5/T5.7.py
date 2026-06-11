"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.7. tulostaa seuraavien kolmen bussin lähtöajat
"""

AIKATAULU = [630, 1015, 1415, 1620, 1720, 2000]


def seuraavat_bussit(kellonaika):
    """
    Tutkii mitkä ovat seuraavat kulkevat kolme bussia annetusta kellonajasta

    :param kellonaika: int, kellonaika kokonaislukuna
    :return: list, listana kolmem seuraavan bussin lähtöajat
    """
    i = 0
    while i < len(AIKATAULU):
        if kellonaika <= AIKATAULU[i]:
            indeksi = i
            break
        i += 1
    bussi_kpl = 0
    vrk_bussit = AIKATAULU[i:]
    if len(vrk_bussit) >= 3:
        return vrk_bussit[:3]
    else:
        bussi_kpl = len(vrk_bussit)
        seuraava_vrk = 3 - bussi_kpl
        return vrk_bussit + AIKATAULU[:seuraava_vrk]


def tulosta_aikataulu(aikataulu):
    """
    Tulostaa annetun listan

    :param aikataulu: list, aikataulu listana
    """
    i = 0
    while i < len(aikataulu):
        print(aikataulu[i])
        i = i + 1

def main():
    kellonaika = int(input("Enter the time (as an integer): "))
    seuraavat = seuraavat_bussit(kellonaika)
    print("The next buses leave:")
    tulosta_aikataulu(seuraavat)


if __name__ == "__main__":
    main()
