"""Commands for converter

This script handles all the previous transformations for the image,
as resize, crop (still not implemented)

This script require the 'PIL' package in specific the Image module,
as it offers the required Interface for IO image.

To perform the according actions it utilizes internal modules, which
satisfy an internal interface for img convertion

"""
from PIL import Image
from os import get_terminal_size
from img2ansi.convert.ansi.ansi import Ansi
from img2ansi.convert.block.block import Block


class BlockCmd():
    """CLI commands handler
    This class handles all the CLI parameters
    and executes the corresponding action

    Attributes
    ----------
    img : Image
        Image object to convert
    ansimode : int
        Bitwised flags to specify which ansi sequences to perform
    noecho : bool
        True if convertion not echoed to terminal when finished
    wholeblock : bool
        True if convertion utilizes Whole block mode
    save : list
        If true saves convertion to a file with a given filename
        also contained in the list
    resizewidth : int
        Size to resize width image (0) keeps original aspect ratio
        with respect to width
    resizeheight : int
        Size to resize height image (0) keeps original aspect ratio
        with respect to height
    converter : Converter Class
        Converter class that performs the actual convertion

    """

    def resizeImg(self):
        """
        Resize img according to resizewidth, resizeheight and fullscreen
        To perform resampling the LANCZOS algorithm is used.

        """
        if(self.fullscreen):
            # Resize to fullscreen -Fr 0 0
            if(self.resizewidth == 0 and self.resizeheight == 0):
                w, h = get_terminal_size()
                if(self.wholeblock):
                    self.img = self.img.resize((w, h),
                                            Image.LANCZOS)
                else:
                    self.img = self.img.resize((w, 2 * h),
                                            Image.LANCZOS)
            # Keep aspect ratio, height -> terminal height -F -r 0 y
            elif(self.resizewidth == 0 and self.resizeheight != 0):
                AspectRatio = self.img.width / self.img.height
                _, h = get_terminal_size()
                if(self.wholeblock):
                    self.img = self.img.resize(
                        (int(h * AspectRatio), h), Image.LANCZOS)
                else:
                    self.img = self.img.resize(
                        (int(1 * h * AspectRatio), 2 * h), Image.LANCZOS)
            # Keep aspect ratio, width -> terminal width -Fr x 0
            elif(self.resizewidth != 0 and self.resizeheight == 0):
                AspectRatio = self.img.height / self.img.width
                w, _ = get_terminal_size()
                if(self.wholeblock):
                    self.img = self.img.resize(
                        (w, int(w * AspectRatio)), Image.LANCZOS)
                else:
                    self.img = self.img.resize(
                        (1 * w, int(2 * w * AspectRatio)), Image.LANCZOS)
            # Resize to given size -Fr x y.
            elif(self.resizewidth != 0 and self.resizeheight != 0):
                if(self.wholeblock):
                    self.img = self.img.resize(
                        (self.resizewidth, self.resizeheight),
                        Image.LANCZOS)
                else:
                    self.img = self.img.resize(
                        (1 * self.resizewidth, 2 * self.resizeheight),
                        Image.LANCZOS)
        else:
            # Resize to given size -r x y
            if(self.resizewidth != 0 and self.resizeheight != 0):
                if(self.wholeblock):
                    self.img = self.img.resize(
                        (2 * self.resizewidth, self.resizeheight),
                        Image.LANCZOS)
                else:
                    self.img = self.img.resize(
                        (1 * self.resizewidth, 2 * self.resizeheight),
                        Image.LANCZOS)
            # Keep aspect ratio, height -> resizeheight -r 0 y
            elif(self.resizewidth == 0 and self.resizeheight != 0):
                AspectRatio = self.img.width / self.img.height
                if(self.wholeblock):
                    self.img = self.img.resize(
                        (int(2 * self.resizeheight * AspectRatio),
                         self.resizeheight), Image.LANCZOS)
                else:
                    self.img = self.img.resize(
                        (int(2 * self.resizeheight * AspectRatio),
                         2 * self.resizeheight), Image.LANCZOS)
            # Keep aspect ratio, width -> resizewidth -r x 0
            elif(self.resizewidth != 0 and self.resizeheight == 0):
                AspectRatio = self.img.height / self.img.width
                if(self.wholeblock):
                    self.img = self.img.resize((self.resizewidth,
                        int(2 * self.resizewidth * AspectRatio)),
                        Image.LANCZOS)
                else:
                    self.img = self.img.resize((2 * self.resizewidth,
                        int(2 * self.resizewidth * AspectRatio)),
                        Image.LANCZOS)

    def convert(self):
        """
        Convert img to block representation according to
        selected parameters

        """

        # Create instance of Block converter
        self.converter = Block()
        result = self.converter.convert(self.img, self.ansimode, self.wholeblock)
        if (self.noecho):
            self.converter.print()
        if (self.save):
            self.converter.save(self.save)

        return result


    def __init__(self, args):
        """
        Set all the attributes and call resize method if
        necessary
        """

        # Open the img
        self.img = Image.open(args.inputImage)
        # Get Extra parameters
        self.wholeblock = args.wholeblock
        self.noecho = args.noecho
        self.save = args.save
        # Get Ansi flags and
        # Setup ansimode
        self.ansimode = Ansi.NONE
        # Unset None if any ansi sequence is used
        if(args.blink):
            self.ansimode &= ~Ansi.NONE
            self.ansimode |= Ansi.BLINK
        # Get resize parameters
        self.fullscreen = args.fullscreen
        self.resizewidth, self.resizeheight = args.resize
        # Resize img
        self.resizeImg()
