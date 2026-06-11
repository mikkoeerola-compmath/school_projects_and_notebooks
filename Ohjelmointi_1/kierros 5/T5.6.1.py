"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 5.6.1 Arvosanojen korvaus
"""


def convert_grades(arvosanalista):
    """
    Korvaa nollasta poikkeavat arvosanat arvosanaksi 6

    :param arvosanalista: list, arvosanat sisältävä lista
    """
    index = 0
    for i in arvosanalista:
        if i > 0:
            arvosanalista[index] = 6
        index += 1


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
