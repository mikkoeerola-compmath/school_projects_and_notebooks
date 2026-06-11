"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.3.2 kertotaulu, yli sadan

def main():
    satanen = True
    annettu_luku = int(input("Choose a number: "))
    kertoja = 1
    while satanen:
        tulos = kertoja * annettu_luku
        print(kertoja, "*", annettu_luku, "=", tulos)
        satanen = tulos <= 100
        kertoja += 1


if __name__ == "__main__":
    main()
