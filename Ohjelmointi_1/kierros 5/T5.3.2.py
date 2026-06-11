"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.3.2 Listan indeksien läpikäyminen
"""


def main():
    print("Give 5 numbers:")
    numerot = []
    for i in range(1, 6):
        numero = int(input("Next number: "))
        numerot.append(numero)
    print("The numbers you entered, in reverse order:")
    for ind in range(0, 5):
        print(numerot[4 - ind])

if __name__ == "__main__":
    main()
