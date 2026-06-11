"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.8.1 Onko tylsää? paranneltu versio


def main():
    vastaus = ""
    while vastaus != "y" and vastaus != "Y":
        vastaus = input("Bored? (y/n) ")
        while (vastaus != "y" and vastaus != "n"
                and vastaus != "Y" and vastaus != "N"):
            if (vastaus != "y" and vastaus != "n"
                    and vastaus != "Y" and vastaus != "N"):
                print("Incorrect entry.")
            vastaus = input("Bored? (y/n) ")
    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
