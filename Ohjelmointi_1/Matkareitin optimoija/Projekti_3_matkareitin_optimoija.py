"""
COMP.CS.100 Ohjelmointi 1
Student Id: 151184192
Nimi:       Mikko Eerola
Sähköposti:      mikko.eerola@tuni.fi

Projekti 3, Matkareitin optimoija:
Ohjelma auttaa käyttäjää löytämään lyhimmän reitin lähtökaupungista kohde-
kaupunkiin käyttäen tiedostosta saatavia etäisyyksiä. Näiden kaupunkien lisäk-
si ohjelmaan voi lisätä ja poistaa yhteyksiä kaupunkien välillä. Ohjelma kysyy
aluksi tiedoston nimeä, jossa yhteystiedot ovat. Käyttö kannattaa aloitta
syötteellä display.
"""


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dict, A data structure of an unspecified type (you decide)
           which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """

    # +--------------------------------------+
    # |                                      |
    # |     DO NOT MODIFY THIS FUNCTION!     |
    # |                                      |
    # +--------------------------------------+

    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """

    # yritetään avata ja lukea tiedosto, jos se ei onnistus palautetaan None.
    try:

        data = open(file_name, mode="r", encoding="utf-8")

        matka_datat = {}  # alustetaan ulompi sanakirja
        # luetaan tekstitiedostoa riveittäin
        for rivi in data:
            rivi = rivi.rstrip()
            rivi_lista = rivi.split(";")
            # nyt on muodostettu lista, jonka ensimmäinen alkio on lähtö-
            # kaupunki, toinen alkio kohdekaupunki ja kolmas niiden välinen
            # etäisyys. Muodostetaan näistä sisäkkäiset sanakirjat.

            kohde_matkat = {}  # alustetaan sisempi sanakirja

            try:
                if rivi_lista[0] not in matka_datat:
                    # jos kaupunkia ei vielä ole lähtökaupungeissa, lisätään
                    # se, kohde ja etäisyys sanakirjoihin
                    try:
                        kohde_matkat[rivi_lista[1]] = int(rivi_lista[2])

                    except ValueError:
                        return None

                else:
                    # jos kaupunki on jo ulommassa sanakirjassa lisätään uusi
                    # kohde sen avaimen takana olevaan sisempään sanakirjaan
                    try:
                        kohde_matkat = matka_datat[rivi_lista[0]]
                        kohde_matkat[rivi_lista[1]] = int(rivi_lista[2])

                    except ValueError:
                        return None

            except IndexError:
                return None

            matka_datat[rivi_lista[0]] = kohde_matkat

        data.close()

        return matka_datat

    except OSError:
        return None


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict[dict], A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    try:
        lista = list(data[city].keys())
        return lista
    except KeyError:
        return []


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict[dict], A data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    if departure in data:
        if destination in data[departure]:
            return data[departure][destination]
        else:
            return None
    else:
        return None


def tulosta_tiedot(data):
    """
    Tulostaa pyydetyssä muodossa kaikki etäisyystiedot kaupunkien välillä.
    tulostus tapahtuu aakkosjärjestyksessä.

    :param data: dict[dict], joissa data on.
    """

    for lahto in sorted(data):
        for kohde in sorted(data[lahto]):
            matka = data[lahto][kohde]
            print(f"{lahto:<14}{kohde:<14}"
                  f"{matka:>5}")


def lisaa_yhteys(data):
    """
    lisää yhteyden käyttäjän antamien kaupunkien välille

    :param data: dict[dict], joissa data on.
    """

    lahto = input("Enter departure city: ")
    kohde = input("Enter destination city: ")
    matka = input("Distance: ")

    try:
        matka = int(matka)
        #  lisätään yhteys dataan. Näin myös olemassa oleva yhteys päivittyy
        if lahto in data:
            data[lahto][kohde] = matka
        else:
            data[lahto] = {kohde: matka}

    except ValueError:
        print(f"Error: '{matka}' is not an integer.")
        pass


def poista_yhteys(data):
    """
    poistaa pyydetyn yhteyden ja hallitsee vastaan tulevat virhetilanteet

    :param data: dict[dict], joissa data on.
    """

    lahto = input("Enter departure city: ")

    # jos lahtokaupunkia ei löydy
    if lahto not in data:
        print(f"Error: '{lahto}' is unknown.")
        return None

    kohde = input("Enter destination city: ")

    # jos yhteyttä ei löydy
    if kohde not in data[lahto]:
        print(f"Error: missing road segment between '{lahto}' and '{kohde}'.")
        return None

    del data[lahto][kohde]


def naapurit(data):
    """
    tulostaa pyydetyn kaupungin naapurit eli kaupungit, joihin lähtö-
    kaupungista pääsee.

    :param data: dict[dict], joissa data on
    """

    # käytetään hyödyksi tulostatiedot funnktion pohjaa

    lahto = input("Enter departure city: ")
    # onko lahto lähtö- tai kohdekaupunki
    if lahto not in tunnetut_kaupungit(data):
        print(f"Error: '{lahto}' is unknown.")
        return None

    # poikkeus tulee esille kun kaupungista ei lähde yhteyksiä
    try:
        for kohde in sorted(data[lahto]):
            matka = data[lahto][kohde]
            print(f"{lahto:<14}{kohde:<14}"
                  f"{matka:>5}")
    except KeyError:
        pass


def reitti(data):
    """
    laskee find_route laskeman reitin pituuden ja tulostaa sen kysytyssä
    muodossa. Käsittelee ongelmatapaukset, kun lähtökaupunkia ei löydy tai
    reittiä ei löydy.

    :param data: dict(dict), joka sisältää datan yhteyksistä ja etäisyysksistä
    """

    lahto = input("Enter departure city: ")

    if lahto not in tunnetut_kaupungit(data):
        print(f"Error: '{lahto}' is unknown.")
        return None

    kohde = input("Enter destination city: ")
    # käytetään valmista funktiota
    reitti_lista = find_route(data, lahto, kohde)

    # käsitellään erikoistapaukset:

    if reitti_lista == []:
        print(f"No route found between '{lahto}' and '{kohde}'.")
        return None

    elif lahto == kohde:
        print(lahto, "-", kohde, " (0 km) ", sep="")

    else:
        matka = 0
        # lasketaan reitin pituus
        for i in range(len(reitti_lista) - 1):
            matka += distance_to_neighbour(data, reitti_lista[i], reitti_lista[i + 1])

        # tehdään oikean lainen tulostus
        print("-".join(reitti_lista), f"({matka} km)")


def tunnetut_kaupungit(data):
    """
    Määrittelee, mitä kaupunkeja tunnetaan, jotta vertailu heloppuu.

    :param data: dict[dict], rakenne, jossa tiedot kaupungeista ovat
    :return: list, tunnettut kaupungit
    """

    kaupungit = []

    # saman tyyppinen läpikäynti kuin display toiminnossa.

    for lahto in data:
        if lahto not in kaupungit:
            kaupungit.append(lahto)
        for kohde in data[lahto]:
            if kohde not in kaupungit:
                kaupungit.append(kohde)

    return kaupungit


def main():
    input_file = input("Enter input file name: ")

    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return

        elif "display".startswith(action):

            tulosta_tiedot(distance_data)

        elif "add".startswith(action):

            lisaa_yhteys(distance_data)

        elif "remove".startswith(action):

            poista_yhteys(distance_data)

        elif "neighbours".startswith(action):

            naapurit(distance_data)

        elif "route".startswith(action):

            reitti(distance_data)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
