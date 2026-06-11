"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehtävä 2.7 Fibonaccin lukusarja


def main():
    haluttu_kierros = int(input("How many Fibonacci numbers do you want? "))
    kierrosluku = 1
    eka_luku = 1
    toka_luku = 1
    while kierrosluku <= haluttu_kierros:
        laskettu_fib = eka_luku + toka_luku
        if kierrosluku <= 2:
            print(kierrosluku, ".", " ", eka_luku, sep = "")
            toka_luku = eka_luku
            kierrosluku += 1
        else:
            print(kierrosluku, ".", " ", laskettu_fib, sep = "")
            eka_luku = toka_luku
            toka_luku = laskettu_fib
            kierrosluku += 1


if __name__ == "__main__":
    main()
