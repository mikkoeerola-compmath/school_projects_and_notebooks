"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 10.10 Mölkyn pisteiden laskenta
"""


class Player:
    """
    Luokka, joka käsittelee mölkyn pelaajia.
    """

    def __init__(self, nimi, pisteet=0, heittojen_lkm=0, heitetyt_pisteet=0,
                onnistuneet_heitot=0):
        """
        Rakennetaan luokan pelaajan oliot

        :param nimi: str, pelaajan nimi
        :param pisteet: int, pelaajan pisteet
        :param heittojen_lkm: pelaajan heittojen lukumäärä
        """

        self.__nimi = nimi
        self.__pisteet = pisteet
        self.__heitot = heittojen_lkm
        self.__heitetyt_pisteet = heitetyt_pisteet
        self.__onn_heitot = onnistuneet_heitot

    def get_name(self):
        """
        Hakee pelaajan nimen, johon metodia käytetään

        :return: str, pelaajan nimi
        """
        return self.__nimi

    def add_points(self, lisa_pisteet):
        """
        lisää pelaajalle pisteitä

        :param lisa_pisteet: int, pelaajalle lisättävät pisteet, suurempaa
            kuin nolla
        :raises: Valueerror, jos pisteet ovat negatiivisia
        """

        if lisa_pisteet >= 0:
            self.__heitetyt_pisteet += lisa_pisteet
            self.__heitot += 1
            if lisa_pisteet > 0:
                self.__onn_heitot += 1
            if self.__pisteet + lisa_pisteet > 50:
                self.__pisteet = 25
                print("Matti gets penalty points!")
            else:
                self.__pisteet += lisa_pisteet
                if self.__pisteet >= 40 and self.__pisteet <= 49:
                    print(f"{self.__nimi} needs only {50 - self.__pisteet}"
                          f" points. It's better to avoid knocking down the "
                          f"pins with higher points.")
        else:
            raise ValueError("lisättävät pisteet on oltava ei-negatiivien")

    def get_points(self):
        """
        Hakee pelaajalle pisteet

        :return: int, pelaajan pisteet
        """
        return self.__pisteet

    def has_won(self):
        """
        tarkistaa onko vuorossa oleva pelaaja voittanut

        :return: True, pelaaja voittanut kierroksen jälkeen, False muuten
        """

        if self.__pisteet == 50:
            return True
        else:
            return False

    def throw_average(self):
        """
        laskee ja palauttaa pelaajan heittojen keskiarvon

        :return: float, pelaajan heittojen keskiarvo
        """

        return self.__heitetyt_pisteet / self.__heitot

    def throw_percentage(self):
        """
        laskee ja palauttaa pelaajan osumatarkkuuden. onnistuneeksi heitoksi
        lasketaan kierros, jossa pelaaja on heittänyt yhden tai useamman
        pisteen.

        :return: float, percentage
        """
        if self.__heitot != 0:
            return self.__onn_heitot / self.__heitot * 100
        else:
            return 0


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.throw_average() < pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")

        print(player1.get_name() + ":", player1.get_points(), "p, ", end="")
        print(f"hit percentage {player1.throw_percentage():0.1f}")

        print(player2.get_name() + ":", player2.get_points(), "p, ", end="")
        print(f"hit percentage {player2.throw_percentage():0.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()