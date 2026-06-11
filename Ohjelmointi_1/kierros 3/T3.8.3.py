"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 3.8.3 Parasetamolin annostelu
"""


def calculate_dose(wheigt, time, total_dose_24):
    """Lasketaan, minkä kokoinen annos tulisi antaa

    :param wheigt: int, potilaan paino
    :param time: int, kokonaistunnit viimeannoksesta
    :param total_dose_24: int, viimeisesen 24 h kokonaisannosmäärä
    :return: potilaalle annettava annos määrä"""
    if time < 6 or total_dose_24 >= 4000:
        return 0
    dose = wheigt * 15
    if total_dose_24 + dose < 4000:
        return dose
    else:
        return 4000 - total_dose_24


def main():
    paino = int(input("Patient's weight (kg): "))
    viime_annos = int(input("How much time has passed from the previous"
                            " dose (full hours): "))
    pv_kokonais = int(input("The total dose for the last 24 hours (mg): "))
    annos = calculate_dose(paino, viime_annos, pv_kokonais)
    print(f"The amount of Parasetamol to give to the patient: {annos}")


if __name__ == "__main__":
    main()
