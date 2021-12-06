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
from img2ansi.convert.ascii.ascii import Ascii
from img2ansi.convert.braile.braile import Braile
from img2ansi.convert.block.block import Block


class Commands():
    """CLI commands handler
    This class handles all the CLI parameters
    and executes the corresponding action

    Attributes
    ----------
    img : Image
        Image object to convert
    ansimode : int
        Bitwised flags to specify which ansi sequences to perform
    colorRGB: bool
        True if output should be keep original image colors
    asciicharset: list
        List of ASCII characters to map light intensity
    ascii : bool
        True if convertion utilizes ascii characters
    block : bool
        True if convertion utilizes block unicode characters
    braile : bool
        True if convertion utilizes braile unicode characters
    invertPattern : bool
        True if convertion should use the character set inverted
    noecho : bool
        True if convertion not echoed to terminal when finished
    threshold : int
        Value to binarize image when performing braile convertion
    save : list
        If true saves convertion to a file with a given filename
        also contained in the list
    resizewidth : int
        Size to resize width image (-1) keeps original aspect ratio
        with respect to width
    resizeheight : int
        Size to resize height image (-1) keeps original aspect ratio
        with respect to height
    converter : Converter Class
        Converter class that performs the actual convertion

    Methods
    -------
    __init__(args)
        Sets all attributes with args content and calls methods
        _resizeImg method if necessary and _convert method
    resizeImg()
        Resize img attribute
    convert()
        Convert img to ascii, braile, blocks representation
        utilizing Converter interface
    """

    def resizeImg(self):
        """
        Resize img according to resizewidth, resizeheight and fullscreen
        To perform resampling the LANCZOS algorithm is used.

        """
        if(self.fullscreen):
            # Resize to fullscreen
            if(self.resizewidth == 0 and self.resizeheight == 0):
                w, h = get_terminal_size()
                if(self.braile):
                    self.img = self.img.resize((2 * w, 4 * h),
                                               Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize((w, 2 * h),
                                               Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize((w, h), Image.LANCZOS)
            # Resize keeping aspect ratio, height -> terminal height
            elif(self.resizewidth == 0 and self.resizeheight != 0):
                AspectRatio = self.img.width / self.img.height
                _, h = get_terminal_size()
                if(self.braile):
                    self.img = self.img.resize(
                        (int(2 * h * AspectRatio), 4 * h), Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize(
                        (int(1 * h * AspectRatio), 2 * h), Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize(
                        (int(h * AspectRatio), h), Image.LANCZOS)
            # Resize keeping aspect ratio, width -> terminal width
            elif(self.resizewidth != 0 and self.resizeheight == 0):
                AspectRatio = self.img.height / self.img.width
                w, _ = get_terminal_size()
                if(self.braile):
                    self.img = self.img.resize(
                        (2 * w, int(4 * w * AspectRatio)), Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize(
                        (1 * w, int(2 * w * AspectRatio)), Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize(
                        (w, int(w * AspectRatio)), Image.LANCZOS)
        else:
            # Resize to given size
            if(self.resizewidth != 0 and self.resizeheight != 0):
                if(self.braile):
                    self.img = self.img.resize(
                        (2 * self.resizewidth, 4 * self.resizeheight),
                        Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize(
                        (1 * self.resizewidth, 2 * self.resizeheight),
                        Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize(
                        (self.resizewidth, self.resizeheight),
                        Image.LANCZOS)
            # Resize keeping aspect ratio, height -> resizeheight
            elif(self.resizewidth == 0 and self.resizeheight != 0):
                AspectRatio = self.img.width / self.img.height
                if(self.braile):
                    self.img = self.img.resize(
                        (int(2 * self.resizeheight * AspectRatio),
                         4 * self.resizeheight), Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize(
                        (int(1 * self.resizeheight * AspectRatio),
                         2 * self.resizeheight), Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize(
                        (int(self.resizeheight * AspectRatio),
                         self.resizeheight), Image.LANCZOS)
            # Resize keeping aspect ratio, width -> resizewidth
            elif(self.resizewidth != 0 and self.resizeheight == 0):
                AspectRatio = self.img.height / self.img.width
                if(self.braile):
                    self.img = self.img.resize((2 * self.resizewidth,
                        int(4 * self.resizewidth * AspectRatio)),
                        Image.LANCZOS)
                elif(self.block):
                    self.img = self.img.resize((1 * self.resizewidth,
                        int(2 * self.resizewidth * AspectRatio)),
                        Image.LANCZOS)
                elif(self.ascii):
                    self.img = self.img.resize((self.resizewidth, int(
                        self.resizewidth * AspectRatio)), Image.LANCZOS)

    def convert(self):
        """
        Convert img to seleccted representation according to
        selected converter

        Utilizes imgConverter interface

        """

        if(self.braile):
            # Create instance of Braile converter
            self.converter = Braile()
            if(self.colorRGB != []):
                self.converter.convert(
                    self.img, self.ansimode, self.invertPattern,
                    self.threshold[0], self.colorRGB)
            else:
                self.converter.convert(
                    self.img, self.ansimode, self.invertPattern,
                    self.threshold[0])
        elif(self.block):
            # Create instance of Block converter
            self.converter = Block()
            self.converter.convert(self.img, self.ansimode)
        elif(self.ascii):
            # Create an instance of Ascii converter
            self.converter = Ascii(self.asciicharset)
            self.converter.convert(
                self.img, self.ansimode, self.invertPattern)

        if (self.noecho):
            self.converter.print()
        if (self.save):
            self.converter.save(self.save)
        else:
            self.converter.save()

    def __init__(self, args):
        """
        Set all the attributes and call _resize method if
        necessary, afterwards call _convert method
        """

        # Open the img
        self.img = Image.open(args.inputImage)
        #self.img = self.img.convert("RGB")
        # Get convertion mode
        self.ascii = args.ascii
        self.braile = args.braile
        self.block = args.block
        # Get Extra parameters
        self.colorRGB = args.color
        self.asciicharset = args.asciicharset
        self.invertPattern = args.invertPattern
        self.threshold = args.threshold
        self.noecho = args.noecho
        self.save = args.save
        # Get Ansi flags and
        # Setup ansimode
        self.ansimode = Ansi.NONE
        # Unset None if any ansi sequence is used
        if(args.bold or args.blink or args.foreground or (self.colorRGB != [])):
            self.ansimode &= ~Ansi.NONE
            if (args.bold):
                self.ansimode |= Ansi.BOLD
            if (args.blink):
                self.ansimode |= Ansi.BLINK
            #if (args.bkgd):
            #    self.ansimode |= Ansi.BKGD
            if (args.foreground or (self.colorRGB != [])):
                self.ansimode |= Ansi.FRGD
        # Get resize parameters
        self.fullscreen = args.fullscreen
        self.resizewidth, self.resizeheight = args.resize
        # Resize img
        self.resizeImg()
        # Create instance of img converters and perform convertion
        self.convert()
