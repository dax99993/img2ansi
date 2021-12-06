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

    Methods
    -------
    convert(img, mode)
        Convert image to a given representation utilizing the specified mode
    print()
        Prints the result of convertion to the terminal
    save()
        Saves the result of convertion to a file
    """
    @abstractmethod
    def convert(self, img, mode):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def save(self):
        pass
