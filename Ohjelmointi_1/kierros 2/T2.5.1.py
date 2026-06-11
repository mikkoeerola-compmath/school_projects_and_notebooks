"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.5.1 Lukusarjapeli zip boing for-silmukalla


def main():
    lapun_pituus = int(input("How many numbers would you like to have? "))
    for kierros in range(1, lapun_pituus + 1):
        if kierros % 3 == 0 and kierros % 7 == 0:
            print("zip boing")
        elif kierros % 3 == 0 and kierros % 7 != 0:
            print("zip")
        elif kierros % 3 != 0 and kierros % 7 == 0:
            print("boing")
        else:
            print(kierros)


if __name__ == "__main__":
    main()
