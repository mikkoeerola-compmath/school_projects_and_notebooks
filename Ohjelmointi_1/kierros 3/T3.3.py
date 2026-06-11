"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Projekti inflaatiolaskin
"""


def main():
    #annetaan sopivia alkuarvoja muuttujille
    poistu = True #toistorakenteen lippumuuttuja
    kuukausi = 1
    suurin = 0 #tähän voidaan myöhemmin tallentaa suurin muutos
    inf_viime = 0 #varmistetaan, että muut. on joku arvo jo enne if-lausetta
    while poistu: #toistaa niin kauan kun lippu käännetään
        string = input(f"Enter inflation rate for month {kuukausi}: ")
        if string == "": #käännetään lippu kun käyttäjä lyö enteriä
            poistu = False
        else: #muussa tapauksessa suoritetaan vertailua edelliseen kuukauteen
            inf_nyt = float(string)
            if kuukausi == 1: #edellistä arvoa ei ole, joten tehdään muutok-
                inf_viime = inf_nyt #sesta vökisin nolla
            ero = inf_nyt - inf_viime
            if ero > suurin or kuukausi == 2: #vertaillaan eroa suurimpaan arvoon
                suurin = ero #jos ero on suurempi tallennetaan se suurin muut.
            inf_viime = inf_nyt #lopuksi muutetaan tarvittavat arvot seuraavaa
        kuukausi += 1 #toistoa varten
    if kuukausi <= 3: #Tulostetaan virhe jos toisto loppuu liian aikaisin
        print("Error: at least 2 monthly inflation rates must be entered.")
    else: #muuten tulostetaan suurimmaksi tallennettu ero
        print(f"Maximum inflation rate change was {suurin:0.1f} points.")


if __name__ == "__main__":
    main()
