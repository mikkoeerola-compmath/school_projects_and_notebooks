"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 3.8.1 Kolmion pinta-ala
"""


from math import sqrt


def area(sivu_a, sivu_b, sivu_c):
    """Laskee kolmion pinta-alan

    :param sivu_a: float, sivu a
    :param sivu_b: float, sivu b
    :param sivu_c: float, sivu c
    :return: float, kolmion pinta-ala"""
    piiri = (sivu_a + sivu_b + sivu_c) / 2
    testi = piiri * (piiri - sivu_a) * (piiri - sivu_b) * (piiri - sivu_c)
    print(testi)
    ala = sqrt(piiri * (piiri - sivu_a) * (piiri - sivu_b) * (piiri - sivu_c))
    return ala


def main():
    line_a = float(input("Enter the length of the first side: "))
    line_b = float(input("Enter the length of the second side: "))
    line_c = float(input("Enter the length of the third side: "))
    pinta_ala = area(line_a, line_b, line_c)

    print(f"The triangle's area is{pinta_ala: .1f}")


if __name__ == "__main__":
    main()
