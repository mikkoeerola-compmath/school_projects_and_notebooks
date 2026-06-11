"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.4.1 Montako löytyy?
"""


def input_to_list(n):
    """
    Lukee käyttäjältä lukuja ja tallentaa ne listaksi

    :param n: int, montako lukua luetaan
    :return: list, lista käyttäjän antamista luvuista
    """
    print(f"Enter {n} numbers:")
    luku_lista = []
    for i in range(1, n + 1):
        luku = int(input())
        luku_lista.append(luku)
    return luku_lista


def main():
    n = int(input("How many numbers do you want to process: "))
    lista = input_to_list(n)
    haku = int(input("Enter the number to be searched: "))
    kerrat = lista.count(haku)
    if kerrat == 0:
        print(f"{haku} is not among the numbers you have entered.")
    else:
        print(f"{haku} shows up {kerrat} times among the numbers"
              f" you have entered.")


if __name__ == "__main__":
    main()
