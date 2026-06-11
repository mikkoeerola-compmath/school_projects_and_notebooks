"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Darts tuloslaskuri:
Ohjelma on apuväline darts peliin. Käyttäjä voi valita mistä luvusta erä
alkaa ja montako erävoittoa vaaditaan ottelun voittoon (oletuksena 501 ja
11). Käyttöliittymässä on painikkeet 1-20 sekä tupla- ja triplapainike. Näitä
yhdistelemällä kirjataan vuorossa olevan pelaajan kierroksen pisteet ylös.
Pisteet voi antaa myös manuaalisesti näppäimistöltä. Ohjelmassa on toteutettu
myös ponnahdusikkuna, joka ilmoittaa virheistä, mahdollistaa uuden pelin aloit-
tamisen sekä ilmoittaa uuden erän ja pelin loppumisesta.
"""

from tkinter import *

# Luodaan globaaleja muuttijia kierrospisteitä, pelin pituutta sekä vuorojen
# vaihtelua auttamaan.

KIERROSPISTEET = 301
ERÄVOITOT = 3
PELAAJA_1 = 1
PELAAJA_2 = 2

class DartsLaskuri:
    """
    Graafinen käyttöliittymä, jolla lasketaan darts pisteitä
    """
    def __init__(self):
        # tehdään ikkuna ja sinne tarvittavat komponentit
        self.__darts_kt = Tk()
        self.__darts_kt.title("Darts tuloslaskuri")

        self.__pelaaja_1 = Label(self.__darts_kt,
                                 text="Pelaaja 1", font='Helvetica 12 bold')
        self.__pelaaja_2 = Label(self.__darts_kt,
                                 text="Pelaaja 2", font='Helvetica 12 bold')
        self.__erät_1 = Label(self.__darts_kt, text="erät:",
                              font='Helvetica 12')
        self.__erät_2 = Label(self.__darts_kt, text="erät:",
                              font='Helvetica 12')
        self.__pisteet_1 = Label(self.__darts_kt, text="kier. pisteet:",
                                 font='Helvetica 12')
        self.__pisteet_2 = Label(self.__darts_kt, text="kier. pisteet:",
                                 font='Helvetica 12')
        self.__ka_pisteet_1 = Label(self.__darts_kt, text="ka pisteet:")
        self.__ka_pisteet_2 = Label(self.__darts_kt, text="ka pisteet:")
        self.__kierros_pisteet = Entry(self.__darts_kt)
        self.__tallenna_pisteet = Button(self.__darts_kt, text="Tallenna",
                                         command=self.tallenna)
        self.__nollaa_pisteet = Button(self.__darts_kt, text="Nollaa",
                                       command=self.nollaa)

        #Laitetaan nämä paikalleen
        self.__pelaaja_1.grid(row=0, column=0, columnspan=3, sticky=E + W)
        self.__pelaaja_2.grid(row=0, column=4, columnspan=3, sticky=E + W)
        self.__erät_1.grid(row=1, column=0, columnspan=3, sticky=W)
        self.__erät_2.grid(row=1, column=4, columnspan=3, sticky=W)
        self.__pisteet_1.grid(row=2, column=0, columnspan=3, sticky=W)
        self.__pisteet_2.grid(row=2, column=4, columnspan=3, sticky=W)
        self.__ka_pisteet_1.grid(row=3, column=0, columnspan=3, sticky=W)
        self.__ka_pisteet_2.grid(row=3, column=4, columnspan=3, sticky=W)
        self.__kierros_pisteet.grid(row=5, column=0, columnspan=2, sticky=E + W, pady=10)
        self.__tallenna_pisteet.grid(row=5, column=3, columnspan=2, sticky=E + W, padx=10)
        self.__nollaa_pisteet.grid(row=5, column=5, sticky=E + W)

        # tehdään erikoissyöttöpainikkeet
        self.__bust_nappi = Button(self.__darts_kt, text="Bust", command=self.bust)
        self.__tupla_nappi = Button(self.__darts_kt, text="tupla", command=self.tupla)
        self.__tripla_nappi = Button(self.__darts_kt, text="tripla", command=self.tripla)

        # tehdään syöttöpainikkeet
        self.__p1 = Button(self.__darts_kt, text="1", command=self.p1)
        self.__p2 = Button(self.__darts_kt, text="2", command=self.p2)
        self.__p3 = Button(self.__darts_kt, text="3", command=self.p3)
        self.__p4 = Button(self.__darts_kt, text="4", command=self.p4)
        self.__p5 = Button(self.__darts_kt, text="5", command=self.p5)
        self.__p6 = Button(self.__darts_kt, text="6", command=self.p6)
        self.__p7 = Button(self.__darts_kt, text="7", command=self.p7)
        self.__p8 = Button(self.__darts_kt, text="8", command=self.p8)
        self.__p9 = Button(self.__darts_kt, text="9", command=self.p9)
        self.__p10 = Button(self.__darts_kt, text="10", command=self.p10)
        self.__p11 = Button(self.__darts_kt, text="11", command=self.p11)
        self.__p12 = Button(self.__darts_kt, text="12", command=self.p12)
        self.__p13 = Button(self.__darts_kt, text="13", command=self.p13)
        self.__p14 = Button(self.__darts_kt, text="14", command=self.p14)
        self.__p15 = Button(self.__darts_kt, text="15", command=self.p15)
        self.__p16 = Button(self.__darts_kt, text="16", command=self.p16)
        self.__p17 = Button(self.__darts_kt, text="17", command=self.p17)
        self.__p18 = Button(self.__darts_kt, text="18", command=self.p18)
        self.__p19 = Button(self.__darts_kt, text="19", command=self.p19)
        self.__p20 = Button(self.__darts_kt, text="20", command=self.p20)
        self.__bull = Button(self.__darts_kt, text="BULL", command=self.bull)

        # laitetaan paikalleen syöttöpainikkeet. Manipuloin ipady/x ja padx/y
        # parametreilla nappeja ilman oikeaa tietoa näistä parametreistä,
        # joten tämä kohta voi olla hieman epälooginen.
        self.__tripla_nappi.grid(row=7, column=0, sticky=W + E)
        self.__tupla_nappi.grid(row=8, column=0, sticky=W+ E)
        self.__bust_nappi.grid(row=9, column=0, sticky=W + E)
        self.__p1.grid(row=6, column=1, sticky= E, pady=1, ipadx=10)
        self.__p2.grid(row=6, column=2, sticky=W + E, ipadx=7)
        self.__p3.grid(row=6, column=3, sticky=W + E, ipadx=7)
        self.__p4.grid(row=6, column=4, sticky=W + E, ipadx=7)
        self.__p5.grid(row=6, column=5, sticky=W, ipadx=10)
        self.__p6.grid(row=7, column=1, sticky=E, pady=1, ipadx=10)
        self.__p7.grid(row=7, column=2, sticky=W + E, ipadx=7)
        self.__p8.grid(row=7, column=3, sticky=W + E, ipadx=7)
        self.__p9.grid(row=7, column=4, sticky=W + E, ipadx=7)
        self.__p10.grid(row=7, column=5, sticky=W, ipadx=7)
        self.__p11.grid(row=8, column=1, sticky=E, pady=1, ipadx=7)
        self.__p12.grid(row=8, column=2, sticky=W + E, ipadx=7)
        self.__p13.grid(row=8, column=3, sticky=W + E, ipadx=7)
        self.__p14.grid(row=8, column=4, sticky=W + E, ipadx=7)
        self.__p15.grid(row=8, column=5, sticky=W, ipadx=7)
        self.__p16.grid(row=9, column=1, sticky=E, pady=1, ipadx=7)
        self.__p17.grid(row=9, column=2, sticky=W + E, ipadx=7)
        self.__p18.grid(row=9, column=3, sticky=W + E, ipadx=7)
        self.__p19.grid(row=9, column=4, sticky=W + E, ipadx=7)
        self.__p20.grid(row=9, column=5, sticky=W, ipadx=7)
        self.__bull.grid(row=6, column=6, sticky=W)

        # lisätään lopuksi vielä lopetus nappi
        self.__lopetusnappi = Button(self.__darts_kt, text="Lopeta pelaaminen",
                                     command=self.lopeta_peli)
        self.__lopetusnappi.grid(row=9, column=6, padx=2)

        #aloitetaan uusipeli alustamalla erät ja aloittamalla uusikierros
        self.__erät_p1 = 0
        self.__erät_p2 = 0
        self.uusi_kierros()

        self.__darts_kt.mainloop()

    def uusi_kierros(self):
        """
        Aloittaa uuden kierroksen pelissä. p numeron edessä erottaa nämä
        samannimisistä Label olioista.
        """
        self.__pisteet_p1 = KIERROSPISTEET
        self.__pisteet_p2 = KIERROSPISTEET
        self.__ka_pisteet_p1 = 0
        self.__ka_pisteet_p2 = 0
        self.__vuoro = (self.__erät_p1 + self.__erät_p2) % 2 + 1
        self.__kierroslaskuri = 1
        self.päivitä()

    def päivitä(self):
        """
        Tärkeä metodi, jolla päivitietään pelin tilanne tietoalueille
        """
        self.__erät_1.configure(text=f"erät: {self.__erät_p1}")
        self.__erät_2.configure(text=f"erät: {self.__erät_p2}")
        self.__pisteet_1.configure(text=f"kier. pisteet: {self.__pisteet_p1}")
        self.__pisteet_2.configure(text=f"kier. pisteet: {self.__pisteet_p2}")
        self.__ka_pisteet_1.configure(text=f"ka pisteet: {self.__ka_pisteet_p1:.1f}")
        self.__ka_pisteet_2.configure(text=f"ka pisteet: {self.__ka_pisteet_p2:.1f}")

        # väri koodaus, jotta voi nähdä kumpi pelaaja on vuorossa.
        if self.__vuoro == PELAAJA_1:
            self.__pelaaja_1.configure(background='red')
            self.__pelaaja_2.configure(background='white')
        else:
            self.__pelaaja_2.configure(background='red')
            self.__pelaaja_1.configure(background='white')


    def erä_ka(self):
        """
        Laskee erän pistekeskiarvon ja tallentaa sen atribuuttiin
        """
        if (self.__erät_p1 + self.__erät_p2) % 2 == 0:
            if self.__vuoro == PELAAJA_2:
                self.__ka_pisteet_p1 = (KIERROSPISTEET - self.__pisteet_p1) / ((self.__kierroslaskuri + 1) / 2)
            else:
                self.__ka_pisteet_p2 = (KIERROSPISTEET - self.__pisteet_p2) / (self.__kierroslaskuri / 2)
        else:
            if self.__vuoro == PELAAJA_1:
                self.__ka_pisteet_p2 = (KIERROSPISTEET - self.__pisteet_p2) / ((self.__kierroslaskuri + 1) / 2)
            else:
                self.__ka_pisteet_p1 = (KIERROSPISTEET - self.__pisteet_p1) / (self.__kierroslaskuri / 2)

    def tallenna(self):
        """
        tallentaa tuloksen,joka on ruudussa self.kierros_pisteet,
        vuorossa olevalle pelaajalle. Tarkistaa myös loppuiko erä/peli ja
        jatkaa tilanteen tarvitsemalla tavalla.
        """
        try:
            pisteet = self.__kierros_pisteet.get()
            pisteet = pisteet.rstrip()
            piste_lista = pisteet.split()
            kok_pisteet = 0
            for i in range(len(piste_lista)):
                kok_pisteet += int(piste_lista[i])
        except ValueError:
            self.popup1("Ei voitu muuttaa luvuksi")
            return

        # Tehdään oikeista pisteistä vähennykset, jos pisteet ei menisi pienemmäksi kuin nolla.
        if self.__vuoro == PELAAJA_1:
            if self.__pisteet_p1 - kok_pisteet >= 0:
                self.__pisteet_p1 -= kok_pisteet
            self.__vuoro = PELAAJA_2
        else:
            if self.__pisteet_p2 - kok_pisteet >= 0:
                self.__pisteet_p2 -= kok_pisteet
            self.__vuoro = PELAAJA_1
        self.erä_ka()

        # tutkitaan loppiuko kierros
        # Tässä on turhaa toistoa, joka päitisi toteuttaa jollain muulla tavalla
        if self.loppuiko_kier():
            if (self.__erät_p1 + self.__erät_p2) % 2 == 0:
                if self.__vuoro == PELAAJA_2:
                    self.__erät_p1 += 1
                    self.popup1(f"pelaaja {PELAAJA_1} voitti kierroksen"
                               f" {(self.__kierroslaskuri + 1) // 2}. kierroksella. "
                               f"heittojen keskiarvo oli {self.__ka_pisteet_p1:.1f}.")
                else:
                    self.__erät_p2 += 1
                    self.popup1(f"pelaaja {PELAAJA_2} voitti kierroksen"
                               f" {self.__kierroslaskuri  // 2}. kierroksella "
                               f"heittojen keskiarvo oli {self.__ka_pisteet_p2:.1f}.")
                self.uusi_kierros()
            else:
                if self.__vuoro == PELAAJA_1:
                    self.__erät_p2 += 1
                    self.popup1(f"pelaaja {PELAAJA_2} voitti kierroksen"
                               f" {(self.__kierroslaskuri + 1) // 2}. kierroksella. "
                               f"heittojen keskiarvo oli {self.__ka_pisteet_p2:.1f}.")
                else:
                    self.__erät_p1 += 1
                    self.popup1(f"pelaaja {PELAAJA_1} voitti kierroksen"
                               f" {self.__kierroslaskuri  // 2}. kierroksella "
                               f"heittojen keskiarvo oli {self.__ka_pisteet_p1:.1f}.")
                self.uusi_kierros()
        else:
            self.__kierroslaskuri += 1

        # tutkitaan loppuiko peli
        if self.loppuiko_peli():
            if self.__vuoro == PELAAJA_2:
                self.popup2(f"pelaaja {PELAAJA_1} voitti ottelun! JIPPIII!")
            else:
                self.popup2(f"pelaaja {PELAAJA_2} voitti ottelun! JIPPIII!")
            self.__tallenna_pisteet.configure(state=DISABLED)

        # Tehdään tarvittavat toimenpiteet, jotta uusi vuoro voi alkaa.
        self.päivitä()
        self.nollaa()

    def nollaa(self):
        self.__kierros_pisteet.delete(0, END)

    def loppuiko_kier(self):
        """
        Tarkistaa loppuiko kierros. HUOM! ei ota huomioon lopettiinko tuplan.
        Tämön voisi toteuttaa pienellä tuoplanapin toteutuksen muutoksella
        ja pienellä lisä tiedolla Button-oliosta.

        :return: True, jos kierros loppui ja False, jos kierros ei loppunut
        """
        if self.__pisteet_p1 == 0 or self.__pisteet_p2 == 0:
            return True
        else:
            return False

    def loppuiko_peli(self):
        """
        Tarkistaa loppuiko peli.

        :return: True, jos peli loppui, False muuten
        """
        if self.__erät_p1 == ERÄVOITOT or self.__erät_p2 == ERÄVOITOT:
            return True
        else:
            return False


    # muodostetaan pistenapeille komennot.
    def p1(self):
        self.__kierros_pisteet.insert(END, "1 ")

    def p2(self):
        self.__kierros_pisteet.insert(END, "2 ")

    def p3(self):
        self.__kierros_pisteet.insert(END, "3 ")

    def p4(self):
        self.__kierros_pisteet.insert(END, "4 ")

    def p5(self):
        self.__kierros_pisteet.insert(END, "5 ")

    def p6(self):
        self.__kierros_pisteet.insert(END, "6 ")

    def p7(self):
        self.__kierros_pisteet.insert(END, "7 ")

    def p8(self):
        self.__kierros_pisteet.insert(END, "8 ")

    def p9(self):
        self.__kierros_pisteet.insert(END, "9 ")

    def p10(self):
        self.__kierros_pisteet.insert(END, "10 ")

    def p11(self):
        self.__kierros_pisteet.insert(END, "11 ")

    def p12(self):
        self.__kierros_pisteet.insert(END, "12 ")

    def p13(self):
        self.__kierros_pisteet.insert(END, "13 ")

    def p14(self):
        self.__kierros_pisteet.insert(END, "14 ")

    def p15(self):
        self.__kierros_pisteet.insert(END, "15 ")

    def p16(self):
        self.__kierros_pisteet.insert(END, "16 ")

    def p17(self):
        self.__kierros_pisteet.insert(END, "17 ")

    def p18(self):
        self.__kierros_pisteet.insert(END, "18 ")

    def p19(self):
        self.__kierros_pisteet.insert(END, "19 ")

    def p20(self):
        self.__kierros_pisteet.insert(END, "20 ")

    def bull(self):
        self.__kierros_pisteet.insert(END, "25 ")

    def bust(self):
        self.nollaa()
        self.__kierros_pisteet.insert(0, "0")
        self.tallenna()

    def tupla(self):
        piste_str = self.__kierros_pisteet.get()
        piste_str = piste_str.rstrip()
        piste_lista = piste_str.split()
        try:
           lisä_pisteet = " " + piste_lista[-1] + " "
           self.__kierros_pisteet.insert(END, lisä_pisteet)
        except IndexError:
            self.popup1("Syötä tuplaa ennen mikä tupla oli kyseessä.")

    def tripla(self):
        piste_str = self.__kierros_pisteet.get()
        piste_str = piste_str.rstrip()
        piste_lista = piste_str.split()
        try:
           lisä_pisteet = (" " + piste_lista[-1] + " ") * 2
           self.__kierros_pisteet.insert(END, lisä_pisteet)
        except IndexError:
            self.popup1("Syötä triplaa ennen mikä tripla oli kyseessä.")

    # Halusin toteuttaa hieman erilaisen virheilmoituksen, koska käyttöliittymässä
    # ei mielestäni ollut hyvää paikkaa tekstille. Plussaa en, että tätä on
    # mahdollista käyttää myös muun asian ilmoittamiseen.
    def popup1(self, teksti):
        """
        Ilmoitus ikkuna. Toimii oikeastaan oikein vain, jos painaa lopeta
        painiketta.

        :param teksti: str, teksti, joka näytettään ilmoituksessa
        """
        self.__ponnistusikkuna = Toplevel(self.__darts_kt)
        self.__ponnistusikkuna.geometry("480x120")
        self.__lopeta = Button(self.__ponnistusikkuna, text="Palaa", command=self.lopetapop)
        self.__ilmo_1 = Label(self.__ponnistusikkuna,
                                  text=teksti,
                                  font='Helvetica 10 bold')
        self.__ilmo_1.pack()
        self.__lopeta.pack()

    def popup2(self, teksti):
        """
        Toteuteaan samaan ikkunaan vielä ikään kuin toinen versio, joka tulee
        näkyviin pelin loppuessa.

        :param teksti:  str, näytettävä teksti
        """
        self.__nappi = Button(self.__ponnistusikkuna, text="Uusi peli",
                               command=self.uusi_peli)
        self.__ilmo_2 = Label(self.__ponnistusikkuna,
                                  text=teksti,
                                  font='Helvetica 12 bold')
        # Jos painaa X:ää, peliä ei voi jaktaa "yli" erien.
        self.__lopeta.configure(state=DISABLED)
        self.__ilmo_2.pack()
        self.__nappi.pack()

    def lopetapop(self):
        self.__ponnistusikkuna.destroy()

    def lopeta_peli(self):
        self.__darts_kt.destroy()

    def uusi_peli(self):
        """
        aloittaa uuden pelin, jotta ohjelmaa ei tarvitse aloitta alusta.
        """
        self.__pisteet_p1 = KIERROSPISTEET
        self.__pisteet_p2 = KIERROSPISTEET
        self.__ka_pisteet_p1 = 0
        self.__ka_pisteet_p2 = 0
        self.__vuoro = (self.__erät_p1 + self.__erät_p2) % 2 + 1
        self.__kierroslaskuri = 1
        self.__erät_p1 = 0
        self.__erät_p2 = 0
        self.lopetapop()
        self.__tallenna_pisteet.configure(state=NORMAL)
        self.päivitä()


def main():
    darts = DartsLaskuri()


if __name__ == "__main__":
    main()
