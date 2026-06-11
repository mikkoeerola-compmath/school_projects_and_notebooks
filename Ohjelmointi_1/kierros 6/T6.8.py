"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.8 Isot kirjaimet oikelle paikoilleen
"""


def capitalize_initial_letters(sana):
    """
    Muttaa sana muotoon, jossa jokaisen sanan
    ensimmäinen kirjain on isolla ja muut pienellä

    :param sana: str, muokkauksen kohteena oleva sana, voi olla tyhjä
    :return: str, muokattu versio
    """
    sana_lista = sana.split(" ")
    for i in range(len(sana_lista)):
        sana_lista[i] = sana_lista[i].capitalize()
    return " ".join(sana_lista)


def main():
    print(capitalize_initial_letters("dddd"))


if __name__ == "__main__":
    main()
