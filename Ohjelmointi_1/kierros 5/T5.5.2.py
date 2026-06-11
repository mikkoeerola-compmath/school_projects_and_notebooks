"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.5.2 Funktio listan suuruusjärjestyksen tarkasteluun
"""


def is_the_list_in_order(lista):
    """
    Tarkistaa onko annettu lista suuruusjärjestyksessä

    :param lista: list, tutkittava lista
    :return: bool, True, jos on ja False, jos ei ole
    """
    if lista == sorted(lista):
        return True
    else:
        return False


def main():
    is_the_list_in_order([])


if __name__ == "__main__":
    main()
