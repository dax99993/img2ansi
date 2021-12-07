"""
This script defines a class to convert an image to
a unicode block representation, which allows to
preview an approximation of the image on the terminal

"""

from img2ansi.convert.converter import Converter
from img2ansi.convert.ansi.ansi import *

class Block(Converter):
    """
    Convert a PIL (img) to a block representation
    basically show the actual image with a lower
    resolution to fit in terminal screen

    Attributes
    ----------
    blockRepr : list
        A list with all the convertion data
    blockChar : str
        Unicode str of upper square solid block

    Methods
    -------
    __init__()
        Set the attributes to default values
    print()
        Print result of convertion to terminal
    save(filename)
        Save result of convertion to a file with given filename
    convert()
        Convert the img to the block representation
    """

    def __init__(self):
        """
        Initialize all attributes
        """

        self.blockRepr = []
        # Upper half block
        self.blockChar = "\u2580"
        # Lower half block
        #self.blockChar = "\u2584"

    def print(self):
        """
        Print representation to terminal
        """

        print("".join(self.blockRepr))

    def save(self, filename="imgBlock.txt"):
        """
        Save representation to a file
        """

        with open(filename, "w") as f:
            f.write("".join(self.blockRepr))

    def convert(self, img, ansimode=Ansi.NONE):
        """
        Convert PIL (img) to unicode block representation
        """

        # Convert img to RGB
        rgbimg = img.convert("RGB")
        # Get img dimensions
        width = img.width
        height = img.height
        # Iterate through image in 1x2 window
        # Ignore at most 1 row
        for y in range(0, height - (height % 2), 2):
            # Add optional ansi
            # This convertion mode doesn't support custom
            # background or foreground color since are already used
            # to color the blocks themselves
            self.blockRepr.append( get_ansi_seq(ansimode & ~
                                            Ansi.BKGD & ~
                                            Ansi.FRGD))
            for x in range(0, width):
                # Get RGB pixel values
                RGBupper = rgbimg.getpixel((x, y))
                RGBlower = rgbimg.getpixel((x, y + 1))
                # Set foreground to actual block char (upper block)
                self.blockRepr.append(
                    get_ansi_seq( Ansi.FRGD, RGBupper )
                )
                # Set background to simulate block
                self.blockRepr.append(
                    get_ansi_seq( Ansi.BKGD, RGBlower )
                )
                self.blockRepr.append(self.blockChar)
            # Add newline char at each row end
            self.blockRepr.append(get_ansi_seq(Ansi.RESET))
            self.blockRepr.append("\n")

        return self.blockRepr
