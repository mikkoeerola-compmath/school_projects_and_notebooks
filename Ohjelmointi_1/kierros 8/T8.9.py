"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 8.9 Numeroitujen rivien kirjoittaminen tiedostoon
"""


def read_message():
    """
    Luetaan käyttäjältä viesti ja talletetaan se listaan

    :return: list, alkiot käyttäjän syötteitä merkkijonoina
    """
    jatka = True
    viesti_lista = []
    while jatka:
        viesti = input()
        if viesti == "":
            jatka = False
        else:
            viesti_lista.append(viesti)
    return viesti_lista


def main():
    tiedosto_nimi = input("Enter the name of the file: ")
    try:
        tiedosto = open(tiedosto_nimi, mode="w")
    except OSError:
        print(f"Writing the file {tiedosto_nimi} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    rivilista = read_message()
    rivinro = 1
    for rivi in rivilista:
        print(f"{rivinro} {rivi}", file=tiedosto)
        rivinro += 1
    tiedosto.close()
    print(f"File {tiedosto_nimi} has been written.")


if __name__ == "__main__":
    main()
