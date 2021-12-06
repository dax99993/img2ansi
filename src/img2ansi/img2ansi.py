#!/usr/bin/env python3

import argparse
from img2ansi.commands import Commands


def createParser():
    """Creates an argument parser for the imgtoansi CLI

    By default uses parameters -t 127

    Returns
    -------
    argparse
        a set of args to perform specified convertion
    """

    # Setup parser
    parser = argparse.ArgumentParser(
        description="Convert img to Ascii or Braile representation",
        epilog="""By default utilizes Ascii representation with no
        Ansi and original Size""",
    )

    parser.add_argument('-a', '--asciicharset', metavar="Character Set",
                        type=str,
                        help="""Ascii custom character set (default :
                        " .~*:+zM#&@$" )""",
                        default=" .~*:+zM#&@$")

    parser.add_argument('-A', '--ascii',
                        action='store_true',
                        help='Ascii Representation flag',
                        default=True)

    parser.add_argument('-b', '--bold',
                        action='store_true', help='Bold flag',
                        default=False)

    parser.add_argument('-B', '--block',
                        action='store_true', help='Background flag',
                        default=False)

    parser.add_argument('-c', '--color', metavar=("R", "G", "B"),
                        nargs=3, type=int,
                        help="""Set Ansi RGB24 color of Braile
                        representation, each channel is 8bits""",
                        default=[])

    parser.add_argument('-D', '--braile',
                        action='store_true',
                        help='Dot/Braile Representation flag',
                        default=False)

    parser.add_argument('-f', '--foreground',
                        action='store_true', help='Ascii Foreground flag',
                        default=False)

    parser.add_argument('-F', '--fullscreen',
                        action='store_true', help='Fullscreen flag',
                        default=False)

    parser.add_argument('-i', '--invertPattern',
                        action='store_true',
                        help=""""Invert ascii character set or
                        Braile characters flag""",
                        default=False)

    parser.add_argument('-k', '--blink',
                        action='store_true', help='Blink flag',
                        default=False)

    parser.add_argument('-n', '--noecho',
                        action='store_false', help="No echo flag",
                        default=True)

    parser.add_argument('-r', '--resize', metavar=("Width", "Height"),
                        nargs=2, type=int,
                        help="""Resize image (0 0 keeps original size),
                        if given -r 100 0 keeps aspectratio with
                        100px width""",
                        default=[0, 0])

    parser.add_argument('-s', '--save', metavar="output filename",
                        nargs='?', type=str,
                        help="""Save file (if no output filename)
                        defaults to imgAscii.txt or
                        imgBraile.txt or imgBlock.txt""",
                        default="")

    parser.add_argument('-t', '--threshold', metavar=("Threshold"),
                        nargs=1, type=int,
                        help="""Set threshold to binarize img in
                        braile convertion (0-255)""",
                        default=[0x7f])

    parser.add_argument('inputImage', type=str,
                        help='image to be converted'
                        )

    return parser.parse_args()


if __name__ == '__main__':
    # Create parser
    args = createParser()
    # Create command instance and process commands
    commands = Commands(args)
