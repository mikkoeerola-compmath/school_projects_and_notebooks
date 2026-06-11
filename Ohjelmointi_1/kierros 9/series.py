"""
COMP.CS.100 Programming 1

Mikko Eerola, 151184192, Tehtävä 9.5

Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: str, name of the file which contains the data
    :return: dict, keys being the genres and payload being the series belonging
    to the genre.
    """

    genre_dict = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # If the input row was correct, it contained two parts:
            # · the show name before semicolon (;) and
            # · comma separated list of genres after the semicolon.
            # If we know that a function (method split in this case)
            # returns a list containing two elements, we can assign
            # names for those elements as follows:
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            for i in range(0, len(genres)):
                if genres[i] not in genre_dict:
                    genre_dict[genres[i]] = []
                genre_dict[genres[i]].append(name)

        file.close()
        return genre_dict

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    genre_names = ", ".join(sorted(genre_data.keys()))
    print("Available genres are:", genre_names)

    while True:
        genre = input("> ")

        if genre == "exit":
            return
        try:
            for series in sorted(genre_data[genre]):
                print(series)
        except KeyError:
            pass


if __name__ == "__main__":
    main()
