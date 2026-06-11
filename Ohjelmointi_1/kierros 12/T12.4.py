"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Mikko Eerola, 11518294

This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    def __init__(self, nimi, hitpoints):
        """
        rakentaa pelihahmon jolla on nimi, aluksi tyhjä reppu ja hitpoints
        (elämät)

        :param nimi: str, Pelihahmon nimi
        :param hitpoints: int, Pelaajan hitpoints
        """
        self.__nimi = nimi
        self.__reppu = {}
        self.__hitpoints = hitpoints

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
        print("Hitpoints:", self.__hitpoints)
        if self.__reppu != {}:
            for esine in sorted(self.__reppu):
                print(f"  {self.__reppu[esine]} {esine}")
        else:
            print("  --nothing--")

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if item in self.__reppu:
            target.give_item(item)
            self.remove_item(item)
            return True
        else:
            return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        if weapon not in WEAPONS:
            print(f"Attack fails: unknown weapon \"{weapon}\".")
            return False
        elif weapon not in self.__reppu:
            print(f"Attack fails: {self.__nimi} doesn't have \"{weapon}\".")
            return False
        elif self == target:
            print(f"Attack fails: {self.__nimi} can't attack him/herself.")
            return False
        else:
            attack_p = WEAPONS[weapon]
            print(f"{self.__nimi} attacks {target.__nimi}"
                  f" delivering {attack_p} damage.")
            target.__hitpoints -= attack_p

            if target.__hitpoints <= 0:
                print(f"{self.__nimi} successfully defeats {target.__nimi}.")

            return True


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
