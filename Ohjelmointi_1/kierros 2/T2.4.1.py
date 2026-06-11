"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.4.1 Lukusarjapeli zip boing


def main():
    lapun_pituus = int(input("How many numbers would you like to have? "))
    kierros = 1
    while kierros <= lapun_pituus:
        if kierros % 3 == 0 and kierros % 7 == 0:
            print("zip boing")
        elif kierros % 3 == 0 and kierros % 7 != 0:
            print("zip")
        elif kierros % 3 != 0 and kierros % 7 == 0:
            print("boing")
        else:
            print(kierros)
        kierros += 1


if __name__ == "__main__":
    main()
