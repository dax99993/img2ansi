"""
This script defines a class that performs a convertion from an image
to a braile unicode character representation, in order to perform it
a windowing technique is used, as a consequence the result has the
width reduced in half and height being a quarter of the original.
"""

from img2ansi.convert.converter import Converter
from img2ansi.convert.ansi.ansi import *
from img2ansi.convert.braile.characters import BRAILE
from img2ansi.convert.braile.utilFunctions import *


class Braile(Converter):
    """
    Convert a PIL (img) to a block representation
    class implements the Converter interface and
    converts an image to it's representation using braile 8 dot unicode
    characters.

    Aditionally supports partially ANSI escape codes to add expressivity to
    the representation, in particular supports truecolor characters, blink,
    bold.

    Attributes
    ----------
    braileRepr : list
        A list containing the result of convertion
    braileCode : list
        A list containing all the braile characters used in convertion

    """

    def __init__(self):
        """
        Initialize attributes
        """

        self.braileRepr = ""
        self.braileCode = BRAILE

    def print(self):
        """
        Prints the content of braileRepr as a text file
        """

        print(self.braileRepr)

    def save(self, filename):
        """
        Save content of braileRepr to an output file with given filename
        """

        with open(filename, 'w') as f:
            f.write(self.braileRepr)

    def convert(self, img, ansimode=Ansi.NONE, invertPattern=False,
                threshold=0x7f,
                frgdcolor=(0xff, 0xff, 0xff),
                bkgdcolor=(0x00, 0x00, 0x00)):
        """
        Converts an img ( PIL ) to the braile unicode representation,
        the optional parameters allow to change the convertion of the img,
        moreover allow the representation unicode with ANSI ESCAPE SEQUENCE
        """

        # Convert to Luma
        Limg = img.convert("L")
        # Get img dimensions
        width = Limg.width
        height = Limg.height
        # Ignores last column if width is odd
        # Ignores at most last 3 rows if height is not multiple of 4
        # Iterate through all image one window at a time
        for winy in range(0, height - (height % 4), 4):
            # Add optional ansimode 
            self.braileRepr += get_ansi_seq(ansimode & ~
                                            Ansi.BKGD & ~
                                            Ansi.FRGD)
            # Add foreground
            if(ansimode & Ansi.FRGD):
                self.braileRepr += get_ansi_seq(Ansi.FRGD,
                                                frgdcolor)
            # Add background
            if(ansimode & Ansi.BKGD):
                self.braileRepr += get_ansi_seq(Ansi.BKGD,
                                                bkgdcolor)
            for winx in range(0, width - (width % 2), 2):
                # Get window pixels
                win = windowing(Limg, winx, winy)
                # Apply Filter
                filteredwin = filter_window(win, "Binarize", threshold)
                # Get braile code representation and add to representation
                self.braileRepr += self.get_braile_char(filteredwin,
                                                        invertPattern)
            # Add a newline at the end of row
            if (ansimode & Ansi.NONE):
                self.braileRepr += "\n"
            else:
                self.braileRepr += get_ansi_seq(Ansi.RESET)
                self.braileRepr += "\n"

        return self.braileRepr

    def get_braile_char(self, pdata, invertPattern=False):
        '''
        Analyzes a list of pixel data which is either 0 or 1
        and converts to best fitting Unicode Braile 8 dot code
        The BRAILE list has the braile codes ordered with respect to the
        binary combination of the points stating from top to bottom and
        left to right column
        Ex. ⢗ is the binary combination A = 7, B = 10
        and would correspond to the simbol BRAILE[7][10]

        Retuns the best fitting Braile code
        '''
        A = (pdata[0] << 0) + (pdata[2] << 1) + \
            (pdata[4] << 2) + (pdata[6] << 3)
        B = (pdata[1] << 0) + (pdata[3] << 1) + \
            (pdata[5] << 2) + (pdata[7] << 3)

        if (invertPattern):
            # To invert the pattern just invert bitwise A and B
            return self.braileCode[~A][~B]

        return self.braileCode[A][B]
