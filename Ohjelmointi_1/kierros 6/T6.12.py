"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.12 Montako abbaa?
"""


def count_abbas(teksti):
    """
    Laskee montako abbaa (rinnakkaisia tai erillisiä) abba tekstejä löytyy

    :param teksti: str, tutkittava teksti
    :return: int, abbojen lukumäärä
    """
    count = 0
    if len(teksti) < 4:
        return count
    else:
        for i in range(len(teksti)):
            if teksti[i:].startswith("abba"):
                count += 1
        return count

def main():
    count_abbas("abba")


if __name__ == "__main__":
    main()
