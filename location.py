"""
created by Nagaj at 13/06/2021
"""
from logs import logger
from mixins import JsonMixin


class City(JsonMixin):
    """
    class for dealing with city
    """

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        logger.info("city '%s' was created", self.name)

    def __repr__(self):  # pylint:  disable=C0116
        return self.name

    def to_json(self):
        """
        return json obj for city
        :return: obj for city
        """
        return {
            "name": self.name,
            "lat": self.latitude,
            "lon": self.longitude,
        }


class Country(JsonMixin):
    """
        class for dealing with country
    """

    def __init__(self, name):
        self.name = name
        self.cities = []
        logger.info("country '%s' was created", self.name)

    def __repr__(self):  # pylint: disable=C0116
        return self.name

    def __getitem__(self, item):  # pylint:  disable=C0116
        return self.cities[item]

    def __contains__(self, item):  # pylint:  disable=C0116
        return item in self.cities

    def add_city(self, city: City):
        """
        add city to country
        :param city: city obj
        :return:
        """
        self.cities.append(city)

    def show_city_info(self, city: City):
        """
        show city if related to country
        :param city: City obj
        :return: json obj for city if it related to country
        """
        if city in self.cities:
            return city.to_json()
        return ""

    def to_json(self):
        """
         json obj for country
        :return: obj for country
        """
        return {"name": self.name, "cities": [city.to_json() for city in self.cities]}
