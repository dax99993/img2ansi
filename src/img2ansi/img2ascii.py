#!/usr/bin/env python3

import argparse
import sys
from img2ansi.asciicmd import AsciiCmd


def create_parser(args):
    """Creates an argument parser for the img2ascii CLI

    Returns
    -------
    argparse
        a set of args to perform specified convertion
    """

    # Setup parser
    parser = argparse.ArgumentParser(
        description="Convert img to Ascii representation",
        epilog="""By default uses parameters -r 0 0 -a " .~*:+zM#&@$" """
    )

    parser.add_argument('-a', '--asciicharset', metavar="Character Set",
                        type=str,
                        help="""ascii character set (default :
                        " .~*:+zM#&@$" )""",
                        default=" .~*:+zM#&@$")

    parser.add_argument('-F', '--frgdcolor', metavar=("R", "G", "B"),
                        nargs=3, type=int,
                        help="""All characters with RGB24 foreground color""",
                        default=[])

    parser.add_argument('-B', '--bkgdcolor', metavar=("R", "G", "B"),
                        nargs=3, type=int,
                        help="""All characters with RGB24 background color""",
                        default=[])

    parser.add_argument('-b', '--bold',
                        action='store_true', help='bold flag',
                        default=False)

    parser.add_argument('-c', '--color',
                        action='store_true', help='foreground text as img colors',
                        default=False)

    parser.add_argument('-f', '--fullscreen',
                        action='store_true', help='fullscreen flag',
                        default=False)

    parser.add_argument('-i', '--invertPattern',
                        action='store_true',
                        help=""""invert ascii character set""",
                        default=False)

    parser.add_argument('-k', '--blink',
                        action='store_true', help='blink flag',
                        default=False)

    parser.add_argument('-n', '--noecho',
                        action='store_false', help="no echo flag",
                        default=True)

    parser.add_argument('-r', '--resize', metavar=("Width", "Height"),
                        nargs=2, type=int,
                        help="""resize image (0 0 keeps original size),
                        if given -r 100 0 keeps aspectratio with
                        100px width""",
                        default=[0, 0])

    parser.add_argument('-o', '--save', metavar="output filename",
                        nargs='?', type=str,
                        help="""save file (if no output filename)
                        defaults to ascii.txt""",
                        default="ascii.txt")

    parser.add_argument('inputImage', type=str,
                        help='image to be converted'
                        )

    return parser.parse_args(args)

def main(argv=None):
    # Create parser
    if( argv is None ):
        args = create_parser(sys.argv[1:])
    else:
        args = create_parser(argv)
    # Create command instance and process commands
    commands = AsciiCmd(args)
    # Call convert method
    result = commands.convert()
    # return result of convertion
    return result

