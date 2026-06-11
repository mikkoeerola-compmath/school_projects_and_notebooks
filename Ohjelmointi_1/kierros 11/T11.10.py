"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 11.10 Murtolukulaskin, komentotulkki
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
    lippu = True
    varasto = {}

    while lippu:
        komento = input("> ")

        if komento == "quit":
            print("Bye bye!")
            return

        elif komento == "add":

            murto = input("Enter a fraction in the form integer/integer: ")
            nimi = input("Enter a name: ")

            murto = murto.split("/")
            nim = int(murto[0])
            os = int(murto[1])
            murto = Fraction(nim, os)

            varasto[nimi] = murto

        elif komento == "print":

            nimi = input("Enter a name: ")
            try:
                print(f"{nimi} = {varasto[nimi]}")
            except KeyError:
                print(f"Name {nimi} was not found")
                pass

        elif komento == "list":

            if len(varasto) != 0:
                for luku in sorted(varasto):
                    print(f"{luku} = {varasto[luku]}")
            else:
                pass

        elif komento == "*":

            eka = input("1st operand: ")
            if eka not in varasto:
                print(f"Name {eka} was not found")
            else:
                toka = input("2nd operand: ")
                if toka not in varasto:
                    print(f"Name {toka} was not found")
                else:
                    tulos = varasto[eka].multiply(varasto[toka])
                    print(f"{varasto[eka]} * {varasto[toka]} = {tulos}")

                    tulos.simplify()
                    print(f"simplified {tulos}")

        elif komento == "file":

            tied_nimi = input("Enter the name of the file: ")
            try:
                murto_tied = open(tied_nimi, mode="r")

                try:

                    for rivi in murto_tied:
                        rivi = rivi.rstrip()
                        osat = rivi.split("=")
                        luvut = osat[1].split("/")

                        try:
                            luku_1 = int(luvut[0])
                            luku_2 = int(luvut[1])
                            murtoluku = Fraction(luku_1, luku_2)

                            varasto[osat[0]] = murtoluku

                        except ValueError:
                            print("Error: the file cannot be read.")
                            break

                except IndexError:
                    print("Error: the file cannot be read.")

            except OSError:
                print("Error: the file cannot be read.")

        else:
            print("Unknown command!")


if __name__ == "__main__":
    main()
