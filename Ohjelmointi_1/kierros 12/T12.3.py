"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Mikko Eerola, 11518294

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    """
    Kuvailee pelihahmoa, joka voi kerätä tavaroitaan reppuun
    """

    def __init__(self, nimi):
        """
        rakentaa pelihahmon jolla on nimi ja aluksi tyhjä reppu

        :param nimi: str, Pelihahmon nimi
        :param reppu: dict, pelaajan reppu, avaimina asiat ja hyötykuormana
            määrä
        """
        self.__nimi = nimi
        self.__reppu = {}

    def has_item(self, esine):
        """
        tutkii onko hahmolla kyseinen esine

        :param esine: str
        :return: Bool, True jos on, False jos ei ole
        """

        if esine in self.__reppu:
            return True
        else:
            return False


    def give_item(self, esine):
        """
        pelihahmo löytää esineen ja laittaa sen reppuunsa

        :param esine: str, esineen nimi
        """

        if self.has_item(esine):
            self.__reppu[esine] += 1
        else:
            self.__reppu[esine] = 1

    def remove_item(self, esine):
        """
        poistaa hahmon repusta esineen

        :param esine: str, poistettava esine
        """

        if esine in self.__reppu:
            if self.__reppu[esine] == 1:
                del self.__reppu[esine]
            else:
                self.__reppu[esine] -= 1


    def get_name(self):
        """
        kertoo hahmon nimen käyttäjälle

        :return: str, hahmon nimi
        """

        return self.__nimi

    def how_many(self, esine):
        """
        kertoo käyttäjälle montako kappaletta kyseistä esinettä löytyy
        hahmon repusta

        :param esine: str, haluttu esine
        :return: int, esineiden kpl
        """

        if esine in self.__reppu:
            return self.__reppu[esine]
        else:
            return 0

    def printout(self):
        """
        tulostaa hahmon nimen ja repun tiedot
        """
        print("Name:", self.__nimi)
        if self.__reppu != {}:
            for esine in sorted(self.__reppu):
                print(f"  {self.__reppu[esine]} {esine}")
        else:
            print("  --nothing--")


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
