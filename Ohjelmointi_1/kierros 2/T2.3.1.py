"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.3.1 Kertotaulu, kouluversio

def main():
    tulos = 0
    kertoja = 1
    annettu_luku = int(input("Choose a number: "))
    while kertoja <= 10:
        tulos = kertoja * annettu_luku
        print(kertoja, "*", annettu_luku, "=", tulos)
        kertoja += 1


if __name__ == "__main__":
    main()
