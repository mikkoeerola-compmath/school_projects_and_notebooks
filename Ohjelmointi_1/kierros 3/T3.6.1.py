"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 3.6.1 Old McDonald -laulu
"""


def print_verse(animal, noise):
    """Tulostaa säkeistön

    :param animal: string, säkeistön eläin
    :param noise: string, eläimen ääni
    """
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print("And on his farm he had a", animal)
    print("E-I-E-I-O")
    print(f"With a {noise} {noise} here")
    print(f"And a {noise} {noise} there")
    print(f"Here a {noise}, there a {noise}")
    print (f"Everywhere a {noise} {noise}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
