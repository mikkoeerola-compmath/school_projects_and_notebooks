"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")


    print_box(width, height, mark)


if __name__ == "__main__":
    main()
