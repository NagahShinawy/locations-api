"""
created by Nagaj at 13/06/2021
"""
from pprint import pprint
from data import cities
from location import City, Country


def main():
    """
    entry point
    :return:
    """
    cities_ = [City(**city) for city in cities]
    print(cities_)
    saudi_arabia = Country("Saudi Arabia")
    for city in cities_:
        saudi_arabia.add_city(city)

    pprint(saudi_arabia.to_json())
    pprint(cities_[0].to_json())

    print("#" * 100)
    for city in saudi_arabia:  # happens because of using __getitem__
        print(city)

    print("#" * 100)
    alex = City("Alex", 34.5, 95.65)
    print(alex in saudi_arabia)  # happens because of using __contains__
    print(cities_[1] in saudi_arabia)

    print("#" * 100)
    print(saudi_arabia.show_city_info(alex))
    print(saudi_arabia.show_city_info(cities_[-1]))


if __name__ == "__main__":
    main()
