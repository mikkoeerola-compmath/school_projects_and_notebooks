"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

Tehtävä 7.9 sanatiheyslaskuri
"""


def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    lippu = True
    sanalaskuri = {}
    while lippu:
        sanat = input()
        if sanat == "":
            lippu = False
        else:
            sanat_listana = sanat.split(" ")
            for i in range(len(sanat_listana)):
                sanat_listana[i] = sanat_listana[i].lower()
            for word in sanat_listana:
                if word in sanalaskuri:
                    sanalaskuri[word] += 1
                else:
                    sanalaskuri[word] = 1
    #tulostus
    for sana in sorted(sanalaskuri):
        print(f"{sana} : {sanalaskuri[sana]} times")


if __name__ == "__main__":
    main()
