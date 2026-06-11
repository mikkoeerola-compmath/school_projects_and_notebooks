"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.5.3 Rubikin kuutio -kilpailut
"""


def kilpailutulos(lista):
    """
    Palauttaa kilpailijan kilpailutuloksen annetun tuloslistan pohjalta

    :param lista: list, kilpailijan tulokset listassa
    :return: float, kilpailutulos
    """
    lista.remove(min(lista))
    lista.remove(max(lista))
    return keskiarvo(lista)


def keskiarvo(lista):
    """
    laskee annetun listan alkioiden keskiarvon

    :param lista: list, tutkittava lista alkiot float tai int, ei tyhjä!!!
    :return: float, alkioiden keskiarvo
    """
    summa = 0
    for i in lista:
        summa = summa + i
    ka = summa / len(lista)
    return ka


def main():
    kaikki_tulokset = []
    for i in range(1, 6):
        tulos = float(input(f"Enter the time for performance {i}: "))
        kaikki_tulokset.append(tulos)
    lopputulos = kilpailutulos(kaikki_tulokset)
    print(f"The official competition score is {lopputulos:.2f} seconds.")


if __name__ == "__main__":
    main()
