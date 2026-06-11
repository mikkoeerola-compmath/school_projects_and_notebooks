"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.11 kokonaisen viestin ROT-13 salaus
"""


def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    if text.lower() in regular_chars:
        if text.isupper():
            text = text.lower()
            indeksi = regular_chars.index(text)
            return encrypted_chars[indeksi].upper()
        else:
            indeksi = regular_chars.index(text)
            return encrypted_chars[indeksi]
    else:
        return text


def row_encryption(text):
    """
    Tekee encrypt() funktion kuvaileman salauksen koko riville

    :param text: str, salattava rivi
    :return: str, salattu rivi
    """
    salaus = ""
    for i in range(len(text)):
        merkki = text[i]
        salattu_merkki = encrypt(merkki)
        salaus += salattu_merkki
    return salaus


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

    print("ROT13:")
    for i in range(len(msg)):
        msg[i] = row_encryption(msg[i])
        print(msg[i])


if __name__ == "__main__":
    main()
