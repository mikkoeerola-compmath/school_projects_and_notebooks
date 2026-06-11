"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 4.11.1 Print_box parempi versio
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """ Tulostetaan haluttu suorakulmio

    :param leveys: int, suorakulmion leveys
    :param korkeus: int, suorakulmion korkeus
    :param merkki: string, merkki jolla suorakulmio tulostetaan"""
    for i in range(1, height + 1):
        if i == 1 or i == height:
            print(border_mark * width)
        else:
            print(border_mark, end="")
            print(inner_mark * (width - 2), end="")
            print(border_mark)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
