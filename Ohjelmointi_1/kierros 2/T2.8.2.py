"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.8.2 Vuoden päivämäärät


def main():
    for kuukausi in range(1, 13):
        if kuukausi == 2:
            for paiva in range(1,29):
                print(paiva, ".", kuukausi, ".", sep = "")
        elif ((kuukausi % 2 == 1 and kuukausi <= 7)
              or (kuukausi % 2 == 0 and kuukausi >= 8)):
            for paiva in range (1, 32):
                print(paiva, ".", kuukausi, ".", sep="")
        else:
            for paiva in range(1, 31):
                print(paiva, ".", kuukausi, ".", sep="")


if __name__ == "__main__":
    main()
