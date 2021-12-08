""" Image Converter Interface

This Script defines an abstract class used to implement
an interface for image converters

"""
from abc import ABC, abstractmethod


class Converter(ABC):
    """
    Interface to handle all posible ways of converting
    and image (pixel data) to some other representation
    as ascii characters, unicode characters,maybe sixels, etc

    """
    @abstractmethod
    def convert(self, img, mode):
        """
        Convert image to a given representation utilizing the specified mode
        """

        pass

    @abstractmethod
    def print(self):
        """
        Prints the result of convertion to the terminal
        """

        pass

    @abstractmethod
    def save(self):
        """
        Saves the result of convertion to a file
        """

        pass
