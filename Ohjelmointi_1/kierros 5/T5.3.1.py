"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.3.1 Listan alkioiden läpikäyminen
"""


def main():
    print("Give 5 numbers:")
    numerot = []
    for i in range(1, 6):
        numero = int(input("Next number: "))
        numerot.append(numero)
    print("The numbers you entered that were greater than zero were:")
    for num in numerot:
        if num > 0:
            print(num)


if __name__ == "__main__":
    main()
