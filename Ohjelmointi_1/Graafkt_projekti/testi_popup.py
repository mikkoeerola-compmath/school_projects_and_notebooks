"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""

from tkinter import *

class Käyttöliittymä:
    def __init__(self):
        self.__kt = Tk()
        self.__luku = Entry(self.__kt)
        self.__luku.pack()
        self.__näyttö = Label(self.__kt, relief=GROOVE)
        self.__näyttö.pack()
        self.__nappi = Button(self.__kt, text="muunna", command=self.muutos)
        self.__nappi.pack()
        self.__lopeta_nappi = Button(self.__kt, text="lopeta", command=self.lopetam)
        self.__lopeta_nappi.pack()

        self.__kt.mainloop()

    def muutos(self):
        try:
            luku = int(self.__luku.get())
            self.__näyttö.configure(text=luku)
        except ValueError:
            self.popup()

    def popup(self):
        self.__virheikkuna = Toplevel(self.__kt)
        self.__virheikkuna.geometry("240x120")
        self.__virheikkuna.title("Virhe tapahtui")
        self.__lopeta = Button(self.__virheikkuna, text="Palaa", command=self.lopetap)
        self.__virhe_ilmo = Label(self.__virheikkuna,
                                  text="Ei voitu muuttaa luvuksi",
                                  font='Helvetica 14 bold')
        self.__virhe_ilmo.pack()
        self.__lopeta.pack()
        self.reset_fields()

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__luku.delete(0, END)
        self.__näyttö.configure(text="")
        self.__nappi.configure(state=DISABLED)


    def lopetap(self):
        self.__virheikkuna.destroy()
        self.__nappi.configure(state=NORMAL)

    def lopetam(self):
        self.__kt.destroy()


def main():
    Käyttöliittymä()

if __name__ == "__main__":
    main()

# tutkitaan loppiuko kierros
if self.loppuiko_kier():
    if self.__vuoro == PELAAJA_1:
        self.__erät_p1 += 1
        self.popup(f"{PELAAJA_1} voitti kierroksen")
    else:
        self.__erät_p2 += 1
        self.popup(f"{PELAAJA_1} voitti kierroksen")
    self.uusi_kierros()

# tutkitaan loppuiko peli
if self.lopeta_peli():
    if self.__vuoro == PELAAJA_1:
        self.popup(f"{PELAAJA_1} voitti ottelun! JIPPIII!")
    else:
        self.popup(f"{PELAAJA_2} voitti ottelun! JIPPIII!")