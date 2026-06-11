"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 4.10.1 Kolmion kulman suuruus
"""


def calculate_angle(kulma_1, kulma_2 = 90.0):
    """
    Laskee kolmion kolmannen kulman, kun kaksi kulmaa annetaan

    :param kulma_1: float, kolmion ensimmäinen kulma
    :param kulma_2: float, kolmion toinen kulma, oletusarvona 90
    :return: float, kolmannen kulman suuruus
    """
    kulma_3 = 180 - kulma_1 - kulma_2
    return kulma_3


def main():
    yks = float(input("anna ensimmäinen kulma: "))
    kaks = input("anna toinen kulma (vapaaehtoinen, oletus 90): ")
    if kaks != "":
        kaks = float(kaks)
        kulma = calculate_angle(yks, kaks)
    else:
        kulma = calculate_angle(yks)
    print(f"{kulma:.2f}")

if __name__ == "__main__":
    main()
