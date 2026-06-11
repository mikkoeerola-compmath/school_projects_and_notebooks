"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 7.5 Sanakirja turistille
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}
    for word in english_spanish.keys():
        spanish_english[english_spanish[word]] = word

    print("Dictionary contents:")
    sanakirjan_tila = ", ".join(sorted(english_spanish))
    print(sanakirjan_tila)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
             print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ")
            spa_word = input("Give the word to be added in Spanish: ")
            update_1 = {eng_word: spa_word}
            english_spanish.update(update_1)
            update_2 = {spa_word: eng_word}
            spanish_english.update(update_2)

            print("Dictionary contents:")
            sanakirjan_tila = ", ".join(sorted(english_spanish))
            print(sanakirjan_tila)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word hey could not be found from the dictionary.")

        elif command == "P":

            print("")
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(f"{word} {english_spanish[word]}")
            print("")

            print("Spanish-English")
            for word in sorted(spanish_english):
                print(f"{word} {spanish_english[word]}")
            print("")

        elif command == "T":
            lause = input("Enter the text to be translated into Spanish: ")
            lause_lista = lause.split(" ")
            print("The text, translated by the dictionary:")
            for sana in lause_lista:
                if sana in english_spanish:
                    print(english_spanish[sana], end=" ")
                else:
                    print(sana, end=" ")
            print("")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
