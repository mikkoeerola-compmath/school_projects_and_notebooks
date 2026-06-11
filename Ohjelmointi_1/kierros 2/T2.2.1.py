"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.2.1 Onko tylsää?


def main():
    vastaus = "n"
    while vastaus == "n":
        vastaus = input("Bored? (y/n) ")
    print("Well, let's stop this, then.")


if __name__ == "__main__":
    main()
