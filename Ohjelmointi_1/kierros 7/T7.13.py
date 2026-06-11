"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 7.13 Lajittelu hinnan mukaan
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def hinta(tuote):
    """
    Palauttaa kyseisen tuotteen hinnan

    :param tuote: str, tuote, jonka hinta halutaan tietää
    :return: float, tuotteen hinta
    """
    return PRICES[tuote]

def main():
    for tuote in sorted(PRICES, key=hinta):
        print(f"{tuote} {PRICES[tuote]:.2f}")



if __name__ == "__main__":
    main()
