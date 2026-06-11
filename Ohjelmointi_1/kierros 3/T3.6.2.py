"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 3.6.2  Yogi bear -laulu
"""

def repeat_name(nimi, toisto):
    """Tulostaa karhun nimeä toiston antaman määrän

    :param nimi: string, karhun nimi
    :param toisto: int, nimen toistojen määrä"""
    toisto = int(toisto)
    for i in range(1, toisto + 1):
        print(nimi, ", ", nimi, " ", end="", sep="")
        print("Bear")

def verse(avaus,nimi):
    """Tulostaa halutun säkeistön

    :param avaus: string, säkeistön aloitus
    :param nimi: string, säkeistössä karhun nimi
    """
    print(avaus)
    print(nimi, nimi, sep=", ")
    print(avaus)
    repeat_name(nimi, 3)
    print(avaus)
    repeat_name(nimi, 1)


def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
