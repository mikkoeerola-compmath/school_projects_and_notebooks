"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.4  Vokaalien ja konsonanttien määrä
"""


def laske_vokaalit(sana):
    """
    laskee englannin kielisen sanan vokaalien lukumäärän

    :param sana: str, sana, josta vokaalit lasketaan
    :return: int, vokaalien lkm
    """
    vokaali_lkm = 0
    for i in range(len(sana)):
        if sana[i] in ["a", "e", "i", "o", "u", "y"]:
            vokaali_lkm += 1
    return vokaali_lkm



def main():
    sana = input("Enter a word: ")
    vokaalit = laske_vokaalit(sana)
    konsonantit = len(sana) - vokaalit
    print(f"The word \"{sana}\" contains {vokaalit} vowels"
          f" and {konsonantit} consonants.")


if __name__ == "__main__":
    main()
