"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 3.6.3  Neliön tulostus
"""

def print_box(leveys, korkeus, merkki):
    """ Tulostetaan haluttu suorakulmio

    :param leveys: int, suorakulmion leveys
    :param korkeus: int, suorakulmion korkeus
    :param merkki: string, merkki jolla suorakulmio tulostetaan"""
    korkeus = int(korkeus)
    for i in range (1, korkeus + 1):
        leveys = int(leveys)
        print(merkki * leveys)

def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
