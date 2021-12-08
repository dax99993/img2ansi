"""Ascii Image Converter

This script implements a class to perform image to ascii convertion

"""

from img2ansi.convert.converter import Converter
from img2ansi.convert.ansi.ansi import *


class Ascii(Converter):
    """
    Convert a PIL (img) to a ascii representation
    class implements the Converter interface and
    converts and image to it's representation using ascii
    characters.


    Aditionally supports partially ANSI escape codes to add expressivity
    to the representation, in particular supports truecolor characters,
    blink, bold.

    Attributes
    ----------
    asciiRepr : str
        A str containing the result of convertion
    asciiCode : str
        A str containing the ascii character set to map light intensity
    asciiCodeLen : int
        Lenght of asciiCode

    """

    def __init__(self, ascii_charset):
        """
        Initialize attributes
        """

        self.asciiRepr = ""
        self.asciiCode = ascii_charset
        self.asciiCodeLen = len(self.asciiCode) - 1

    def print(self):
        """
        Print the result of convertion to terminal
        """

        print(self.asciiRepr)

    def save(self, filename):
        """
        Save the result of convertion to a file with given filename
        """

        with open(filename, 'w') as f:
            f.write(self.asciiRepr)

    def setAsciiCharacterSet(self, ascii_charset):
        """
        Change the current ascii character set
        """

        self.asciiCode = ascii_charset
        self.asciiCodeLen. len(self.asciiCode) - 1

    def convert(self, img, ansimode=Ansi.NONE, invertPattern=False,
                frgdfix=False, frgdcolor=(0xff, 0xff, 0xff),
                bkgdfix=False, bkgdcolor=(0x00, 0x00, 0x00)
                ):
        """
        Converts a PIL (img) to the ascii representation
        """

        # Convert to RGB
        RGBimg = img.convert("RGB")
        # Convert to Luma
        Limg = img.convert("L")
        # Get img dimensions
        width = img.width
        height = img.height
        # Iterate through all pixels
        for y in range(height):
            # Add optional ansimode (blink, bold, etc)
            self.asciiRepr += get_ansi_seq(ansimode & ~
                                           Ansi.BKGD & ~
                                           Ansi.FRGD)
            for x in range(width):
                # Get Luma pixel
                Lpixel = Limg.getpixel((x, y))
                # Here might add subpixel analysis to get better contrast
                # Linear map from Luma to ascii character set
                if(invertPattern):
                    index = (self.asciiCodeLen - 1 - Lpixel) * \
                            self.asciiCodeLen // 0xff
                else:
                    index = Lpixel * self.asciiCodeLen // 0xff
                # Add Color
                # Fixed bkgdcolor
                if(bkgdfix):
                    self.asciiRepr += get_ansi_seq(Ansi.BKGD,
                                                   bkgdcolor)
                # Fixd frgdcolor has priority over img color
                if(frgdfix):
                    self.asciiRepr += get_ansi_seq(Ansi.FRGD,
                                                   frgdcolor)
                elif(Ansi.FRGD & ansimode):
                    # Get RGB component of pixel
                    rgbpixel = RGBimg.getpixel((x, y))
                    self.asciiRepr += get_ansi_seq(Ansi.FRGD,
                                                   rgbpixel)
                # Add the character
                self.asciiRepr += self.asciiCode[index]
            # Add newline at the end of row
            if((ansimode & Ansi.NONE) and
               not(frgdfix) and not(bkgdcolor)):
                self.asciiRepr += "\n"
            else:
                # Reset Ansi for next row
                self.asciiRepr += get_ansi_seq(Ansi.RESET)
                self.asciiRepr += "\n"

        return self.asciiRepr
