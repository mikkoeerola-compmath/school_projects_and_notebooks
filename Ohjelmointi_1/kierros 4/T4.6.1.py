"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtövö 4.6.1 Liukulukujen vertailua
"""

EPSILON = 0.00001

def compare_floats(luku_1, luku_2, EPSILON):
    """Vertaillaan liukulukujen yhtäsuuruutta

    :param luku_1: float, ensimmäinen luku
    :param luku_2: float, toinen luku
    :param epsilon: float, vertailun kynnystarkkuus
    """
    vertailu  = abs(luku_1 - luku_2) < EPSILON
    return vertailu

def main():
    luku_1  = float(input())
    luku_2 = float(input())
    compare_floats(luku_1, luku_2, EPSILON)

if __name__ == "__main__":
    main()
