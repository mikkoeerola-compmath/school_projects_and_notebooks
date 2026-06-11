"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 6.6 Käännä nimet oikein päin
"""


def reverse_name(nimi):
    """
    kääntää nimen oikein päin
    :param nimi: str, nimi annettu muodossa sukunimi, etunimi tms
    :return: str, nimi muodossa etunimi sukunimi
    """
    if "," in nimi:
        nimet_lista = nimi.split(",")
        nimet_lista[0] = nimet_lista[0].strip()
        nimet_lista[1] = nimet_lista[1].strip()
        nimet_lista.reverse()
        if "" in nimet_lista:
            return "".join(nimet_lista)
        else:
            return " ".join(nimet_lista)
    else:
        return nimi


def main():
    nimi = input("anna nimesi nurinkurin: ")
    print(f"nimesi oikein päin {reverse_name(nimi)}.")


if __name__ == "__main__":
    main()
