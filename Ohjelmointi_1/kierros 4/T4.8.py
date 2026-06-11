"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtövö 4.8 Geometrisen muodon pinta-ala ja piiri
"""


from math import pi


def kysy(kehote):
    """
    Kysytään käyttäjältä muodon dimensioita annetulla kehotteella

    :param kehote: string, kysymyksen kehote
    :return: float, haluttu mitta
    """
    string = input(f"Enter the {kehote}: ")
    luku = float(string)
    return luku


def tarkistus(sivu):
    """
    tarkistetaan onko annettu sivu järkevä

    :param sivu: float, muodon sivun pituus
    :return: bool, True jos hyväksytään ja False jos ei hyväksytä
    """
    if sivu <= 0:
        return False
    else:
        return True


def suorakulmio():
    """
    lasketaan ja tulostetaan suorakulmion piiri ja pinta-ala
    """
    ok_1 = False
    ok_2 = False
    sivu_1, sivu_2 = 0, 0
    while not ok_1:
        sivu_1 = kysy("length of the rectangle's side 1")
        ok_1 = tarkistus(sivu_1)
    while not ok_2:
        sivu_2 = kysy("length of the rectangle's side 2")
        ok_2 = tarkistus(sivu_2)
    piiri = sivu_1 * 2 + sivu_2 * 2
    pinta_ala = sivu_1 * sivu_2

    tulostus(piiri, pinta_ala)


def nelio():
    """
    lasketaan neliön pinta-ala sekä piiri ja tulostetaan ne
    """
    ok = False
    sivu = 0
    while not ok:
        sivu = kysy("length of the square's side")
        ok = tarkistus(sivu)
    piiri = sivu * 4
    pinta_ala = sivu * sivu

    tulostus(piiri, pinta_ala)


def ympyra():
    """
    Lasketaan ja tulostetaan ympyrän piiri ja pinta-ala
    """
    ok = False
    sade = 0
    while not ok:
        sade = kysy("circle's radius")
        ok = tarkistus(sade)
    piiri = 2 * pi * sade
    pinta_ala = sade ** 2 * pi

    tulostus(piiri, pinta_ala)


def tulostus(piiri, pinta_ala):
    """
    Tulostaa pyydetyssä muodossa annetut luvut

    :param piiri: float, muodon piiri
    :param pinta_ala: float, muodon pinta-ala
    """
    print(f"The circumference is {piiri:.2f}")
    print(f"The surface area is {pinta_ala:.2f}")


def menu():
    """
    Print a menu for user to select which
    geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            nelio()

        elif answer == "r":
            suorakulmio()

        elif answer == "c":
            ympyra()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
