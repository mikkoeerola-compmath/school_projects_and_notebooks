"""
COMP.CS.100 Ohjelmointi 1, syksy 2022, luento 5.
Tekijä: Jorma Laurikkala
Opiskelijanumero: ---------
Luetaan ja tulostetaan arvosana.
Versio 7: koodia on selvennetty globaaleilla vakioilla
ja funktiota lyhennetty listojen avulla.
"""
# Numeeriset arvosanat globaaleina vakioina.
VÄLTTÄVÄ = 1
TYYDYTTÄVÄ = 2
HYVÄ = 3
KIITETTÄVÄ = 4
ERINOMAINEN = 5

def anna_arvosana_sanana(arvosana):
    """Palauttaa numeerisen arvosanan sanallisen kuvauksen
    tai virhearvon None.

    :param arvosana: int, arvosana numeerisena.
    :return: string, arvosana tekstuaalisena. Pythonin
    None-vakio, jos parametrin arvo on virheellinen.
    """
    # Palautetaan sanallinen vastine listalta, jos numeerinen arvosana
    # on listalla.
    if arvosana in [VÄLTTÄVÄ, TYYDYTTÄVÄ, HYVÄ, KIITETTÄVÄ, ERINOMAINEN]:
        # Indeksointi alkaa nollasta.
        sanoina = ["välttävä", "tyydyttävä", "hyvä", "kiitettävä", "erinomainen"]
        return sanoina[arvosana - 1]
    else:
        return None

def main():
    # Alustetaan pääsilmukkaa ohjaava lippu siten,
    # että silmukka saadaan käyntiin.
    jatketaan = True

    # Kysellään arvosanoja kunnes käyttäjä kyllästyy.
    while jatketaan:
        # Luetaan syöte käyttäjältä.
        syöte = input("Anna arvosana tai kirjoita \"lopeta\": ")

        # Varsinainen arvosanan lausunta on ehdon takana,
        # koska lopettavaa syötettä ei voi muuntaa kokonaisluvuksi.
        if syöte != "lopeta":
            # Muunnetetaan syöte kokonaisluvuksi, jotta vertailu ja
            # aritmetiikka onnistuu.
            arvosana = int(syöte)

            # Tulostetaan arvosana näytölle hienommin huomioiden
            # virheelliset syötteet.
            sanana = anna_arvosana_sanana(arvosana)
            if sanana != None:
                print("Arvosanasi on ", sanana, ".", sep = "")
            else:
                print("Virheellinen arvosana!")

            # Pohditaan mitä arvosana olisi yhdellä korotettuna,
            # jos voidaan korottaa. Valintarakenne varmistaa,
            # että virheellistä tai kiitettävää arvosanaa ei
            # koroteta.
            if arvosana >= VÄLTTÄVÄ:
                if arvosana < ERINOMAINEN:
                    arvosana = arvosana + 1
                    # Tulostetaan korotettu arvosana näytölle hienommin.
                    sanana = anna_arvosana_sanana(arvosana)
                    print("Yhdellä korotettu arvosana on ", sanana, ".", sep = "")

        # Käännetään pääsilmukan lippu.
        else:
            jatketaan = False

if __name__ == "__main__":
    # Kutsutaan pääohjelmaa.
    main()
