"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 7.3 Hintalista
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    lippu = True
    while lippu:
        tuotenimi = input("Enter product name: ")
        if tuotenimi.lstrip(" ") == "":
            print("Bye!")
            lippu = False
        elif tuotenimi.strip() not in PRICES:
            print(f"Error: {tuotenimi.strip()} is unknown.")
        elif tuotenimi.strip() in PRICES:
            print(f"The price of {tuotenimi.strip()} is {PRICES[tuotenimi.strip()]:0.2f} e")


if __name__ == "__main__":
    main()
