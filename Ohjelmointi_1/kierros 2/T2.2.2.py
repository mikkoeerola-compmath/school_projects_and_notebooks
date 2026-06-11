"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192
"""
# Tehvävä 2.2.2 Onko tylsää? (virhetarkastelu)

def main():
    vastaus = ""
    while vastaus != "y" and vastaus != "n"\
            and vastaus != "Y" and vastaus != "N":
        vastaus = input("Answer Y or N: ")
        if vastaus != "y" and vastaus != "n"\
                and vastaus != "Y" and vastaus != "N":
            print ("Incorrect entry.")
    print("You answered", vastaus)


if __name__ == "__main__":
    main()
