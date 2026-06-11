"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.10 Viestien tallentaminen listaan
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
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    for i in range(len(msg)):
        print(msg[i].upper())


if __name__ == "__main__":
    main()
