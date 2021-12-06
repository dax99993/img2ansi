"""Ascii Image Converter

This script implements a class to perform image to ascii convertion

"""

from img2ansi.convert import Converter
from img2ansi.convert.ansi import *


class Ascii(Converter):
    """
    This class implements the ImgConverter Interface and
    converts and image to it's representation using ascii
    characters.


    Aditionally supports partially ANSI escape codes to add expressivity
    to the representation, in particular supports truecolor characters,
    blink, bold.

    Attributes
    ----------
    asciiRepr : list
        A list containing the result of convertion
    asciiCode : str
        A str containing the ascii character set to map light intensity
    asciiCodeLen : int
        Lenght of asciiCode

    Methods
    -------
    __init__(ascii_charset)
        Initialize attributes
    setAsciiCharacterSet(ascii_charset)
        Change the current ascii character set
    print()
        Print the result of convertion to terminal
    save(filename)
        Save the result of convertion to a file with given filename
    convert(img, ansimode, invertPattern, color)
        Convert the 
    """

    def __init__(self, ascii_charset):
        self.asciiRepr = []
        self.asciiCode = ascii_charset
        self.asciiCodeLen = len(self.asciiCode) - 1

    def print(self):
        print("".join(self.asciiRepr))

    def save(self, filename="imgAscii.txt"):
        with open(filename, 'w') as f:
            f.write(''.join(self.asciiRepr))

    def setAsciiCharacterSet(self, ascii_charset):
        self.asciiCode = ascii_charset
        self.asciiCodeLen. len(self.asciiCode) - 1

    def convert(self, img, ansimode=Ansi.NONE, invertPattern=False,
                color=(0xff, 0xff, 0xff)):
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
        # Add optional ansimode (blink, bold, etc)
        self.asciiRepr.append(get_ansi_seq(
            ansimode & ~ Ansi.BKGD & ~ Ansi.FRGD))
        # Iterate through all pixels
        for y in range(height):
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
                if(Ansi.FRGD & ansimode):
                    # Get RGB component of pixel
                    rgbpixel = RGBimg.getpixel((x, y))
                    self.asciiRepr.append(
                        get_ansi_seq(Ansi.FRGD, rgbpixel))
                # Add the character
                self.asciiRepr.append( self.asciiCode[index] )
            # Add newline at the end of row
            if(ansimode & Ansi.NONE)):
                self.asciiRepr.append("\n")
            else:
                # Reset Ansi for next row
                self.asciiRepr.append(get_ansi_seq(Ansi.RESET))
                self.asciiRepr.append("\n")
                # Add Ansi attributes to next row
                if(y != height - 1):
                self.asciiRepr.append(get_ansi_seq(
                    ansimode & ~ Ansi.BKGD & ~ Ansi.FRGD))
