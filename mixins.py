"""
created by Nagaj at 13/06/2021
"""
from abc import ABC, abstractmethod


class JsonMixin(ABC):  # pylint: disable=R0903
    """
    abstract class to handle json
    """

    @abstractmethod
    def to_json(self):
        """
        convert obj to json response
        :return:
        """
