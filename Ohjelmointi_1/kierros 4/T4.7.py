"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 4.7 Lottopelejä
"""

def onko_oikein(pallo_lkm, arvotut_lkm):
    """
    Tutkii ovatko käyttöjön syötteet kelvolliset

    :param pallo_lkm: int, loton pallojen kokonaismäärä
    :param arvotut_lkm: int, arvottavien pallojen lukumäärä
    :return: bool, menikö testi läpi vai ei
    """
    onko = True
    if pallo_lkm < 0:
        print("The number of balls must be a positive number.")
        onko = False
    elif not pallo_lkm < 0 and pallo_lkm < arvotut_lkm:
        print("At most the total number of balls can be drawn.")
        onko = False
    return onko

def loton_tod(pallot, arpa_lkm):
    """
    Laskee annetun loton päävoiton todennäköisyyden murtolukumuodossa

    :param pallot: int, loton pallojen kokonaismäärä
    :param arpa_lkm: int, arvottavien pallojen lukumäärä
    :return: string, todennäköisyys murtolukumuodossa.
    """
    o = kertoma(pallot) / (kertoma(arpa_lkm) * kertoma(pallot - arpa_lkm))
    return int(o)

def kertoma(kokonaisluku):
    """
    laskee kokonaisluvun kertoman

    :param kokonaisluku: int, käsiteltävä luku
    :return: int, luvun kertoma
    """
    tulos = 1
    for i in range(1, kokonaisluku + 1):
        tulos = i * tulos
    return int(tulos)

def main():
    pallot = int(input("Enter the total number of lottery balls: "))
    arpa = int(input("Enter the number of the drawn balls: "))
    tarkistus = onko_oikein(pallot, arpa)
    if tarkistus:
        tod = loton_tod(pallot, arpa)
        print(f"The probability of guessing all {arpa} balls"
              f" correctly is 1/{loton_tod(pallot, arpa)}")


if __name__ == "__main__":
    main()
