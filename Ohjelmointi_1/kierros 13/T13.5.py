"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 13.5 Kappaletavaralaskuri. Graafisenkäyttöliittymän avulla käyttäjä
voi lisätä, vähentää ja nollata laskurin.
"""


from tkinter import *


class Counter:
    def __init__(self):
        """
        rakentaja, joka luo laskija-olion graafisenkäyttöliittymänä
        """
        self.__pääikkuna = Tk()

        self.__laskuri = 0
        self.__current_value_label = Label(self.__pääikkuna,
                                           text=f"{self.__laskuri}")
        self.__current_value_label.pack(side=TOP)

        self.__reset_button = Button(self.__pääikkuna, text="Reset",
                                     command=self.nollaa)
        self.__reset_button.pack(side=LEFT)

        self.__increase_button = Button(self.__pääikkuna, text="Increase",
                                        command=self.kasvata)
        self.__increase_button.pack(side=LEFT)

        self.__decrease_button = Button(self.__pääikkuna, text="Decrease",
                                        command=self.vähennä)
        self.__decrease_button.pack(side=LEFT)

        self.__quit_button = Button(self.__pääikkuna, text="quit",
                                    command=self.lopeta)
        self.__quit_button.pack(side=LEFT)

        self.__pääikkuna.mainloop()

    def nollaa(self):
        """
        nollaa laskurin
        """
        self.__laskuri = 0
        self.__current_value_label.configure(text=self.__laskuri)

    def kasvata(self):
        """
        Kasvattaa laskuria yhdellä
        """
        self.__laskuri += 1
        self.__current_value_label.configure(text=self.__laskuri)

    def vähennä(self):
        """
        vähentää laskuria yhdellä
        """
        self.__laskuri -= 1
        self.__current_value_label.configure(text=self.__laskuri)

    def lopeta(self):
        self.__pääikkuna.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
