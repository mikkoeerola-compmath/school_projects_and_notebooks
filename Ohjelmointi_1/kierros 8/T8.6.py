"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 8.6 Tiedoston rivien numerointi
"""


def main():
    tiedosto_nimi = input("Enter the name of the file: ")
    try:
        tiedosto = open(tiedosto_nimi, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return
    rivi_nro = 1
    for rivi in tiedosto:
        rivi = rivi.rstrip()
        print(f"{rivi_nro} {rivi}")
        rivi_nro += 1
    tiedosto.close()


if __name__ == "__main__":
    main()
