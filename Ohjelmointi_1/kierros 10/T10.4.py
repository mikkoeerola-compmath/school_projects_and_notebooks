"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 10.4 Tuote luokka
"""


class Product:
    """ Luokka Product määrittelee kaupassa myytävän yksinkertaisen
    tuotteen.
    """
    def __init__(self, nimi, hinta, alennus=0):
        """
        rakentaja

        :param nimi: str, tuotteen nimi
        :param hinta: float, tuotteen hinta
        :param alennus: float, tuotteen alennus prosentteina,
            alkuarvo 0.00
        """

        self.__nimi = nimi
        self.__hinta = hinta
        self.__alennus = alennus

    def printout(self):
        """
        Tulostaa tuotteen tiedot näytölle
        """

        print(self.__nimi)
        print(" ", f"{self.__hinta:.2f}")
        print(" ", f"{self.__alennus:.2f}")

    def get_price(self):
        """
        hakee tuotteen hinnan

        :return: float, tuotteen hinta
        """

        return self.__hinta * (1 - self.__alennus / 100)

    def set_sale_percentage(self, uusi_alennus):
        """
        asettaa tuotteelle alennusprosentin

        :param uusi_alennus: float, haluttu alennus
        """
        if uusi_alennus >= 0:
            self.__alennus = uusi_alennus
        else:
            raise ValueError("Alennusksen pitää olla positiivinen")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
