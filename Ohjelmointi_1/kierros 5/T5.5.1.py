"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtövö 5.5.1 Funktio listan alkioiden yhtäsuuruusvertailuun
"""


def are_all_members_same(lista):
    """
    Tutkii ovatko kaikki listan alkiot samoja.

    :param lista: list, tutkittava lista
    :return: bool, True, jos kaikki arvot samoja, False, jos ei.
    """
    lista_2 = sorted(lista)
    lista_3 = sorted(2 * lista_2)
    if lista_3 == 2 * lista:
        return True
    else:
        return False

def main():
    are_all_members_same([2, 3, 4 ,5])


if __name__ == "__main__":
    main()
