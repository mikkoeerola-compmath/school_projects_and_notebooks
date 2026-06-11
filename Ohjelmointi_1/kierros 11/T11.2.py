"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 11.2 Murtoluku
"""


class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Sieventää murtolukua
        """

        syt = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator // syt
        self.__denominator = self.__denominator // syt

    def reciprocal(self):
        """
        Muodostaa ja palauttaa murtoluvun käänteisluvun

        :return: Fraction, käänteisluku
        """

        re_numerator = self.__denominator
        re_denomerator = self.__numerator
        return Fraction(re_numerator, re_denomerator)

    def complement(self):
        """
        Muodostaa ja palauttaa murtoluvun vastaluvun

        :return: Fraction, vastaluku
        """

        comp_numerator = -self.__numerator
        return Fraction(comp_numerator, self.__denominator)

    def multiply(self, frac):
        """
        Kertoo kaksi kertolukua keskenään

        :param frac: Fraction, kertoja
        :return: Fraction, kertolaskun lopputulos
        """

        num = self.__numerator * frac.__numerator
        denum = self.__denominator * frac.__denominator
        return Fraction(num, denum)

    def divide(self, frac):
        """
        Jakaa kertoluvun toisella

        :param frac: Fraction, jakaja
        :return: Fraction, jakolaskun lopputulos murtolukuna
        """

        return self.multiply(frac.reciprocal())

    def add(self, frac):
        """
        Laskee kaksi murtolukua yhteen
        :param frac: Fraction, lisättävä luku
        :return: Fraction, Yhteenlaskun lopputulos
        """

        denom = self.__denominator * frac.__denominator
        num = self.__numerator * frac.__denominator + frac.__numerator * self.__denominator
        return Fraction(num, denom)

    def deduct(self, frac):
        """
        Vähentää murtoluvun annetusta murtoluvusta

        :param frac: Fraction, vähennettävä
        :return: Fraction, vähennyslaskun lopputulos
        """
        ded = self.multiply(Fraction(frac.__denominator, frac.__denominator))
        dedis = frac.multiply(Fraction(self.__denominator, self.__denominator))

        return Fraction(ded.__numerator - dedis.__numerator, ded.__denominator)

    def __lt__(self, frac):

        self_as_float = self.__numerator / self.__denominator
        frac_as_float = frac.__numerator / frac.__denominator

        return self_as_float < frac_as_float

    def __gt__(self, frac):
        self_as_float = self.__numerator / self.__denominator
        frac_as_float = frac.__numerator / frac.__denominator

        return self_as_float > frac_as_float

    def __str__(self):
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    lippu = True
    murtolista = []

    while lippu:
        rivi = input()
        if rivi == "":
            lippu = False
        else:
            luvut = rivi.split("/")
            frac = Fraction(int(luvut[0]), int(luvut[1]))
            murtolista.append(frac)

    print("The given fractions in their simplified form:")

    for frac in murtolista:
        print(frac, end=" = ")
        frac.simplify()
        print(frac)




if __name__ == "__main__":
    main()