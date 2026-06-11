"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.9 yhden rivin ROT13-salaus
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


def main():
    text = input("salattava teksti: ")
    print(row_encryption(text))


if __name__ == "__main__":
    main()
