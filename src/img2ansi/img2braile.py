#!/usr/bin/env python3

import argparse
import sys
from img2ansi.brailecmd import BraileCmd


def create_parser(args):
    """Creates an argument parser for the imgtoansi CLI

    Returns
    -------
    argparse
        a set of args to perform specified convertion
    """

    # Setup parser
    parser = argparse.ArgumentParser(
        description="Convert img to Braile representation",
        epilog="""By default -r 0 0 -t 127""",
    )

    parser.add_argument('-b', '--bold',
                        action='store_true', help='bold flag',
                        default=False)

    parser.add_argument('-F', '--frgdcolor', metavar=("R", "G", "B"),
                        nargs=3, type=lambda x: int(x,0),
                        help="""All characters with RGB24 foreground color""",
                        default=[])

    parser.add_argument('-B', '--bkgdcolor', metavar=("R", "G", "B"),
                        nargs=3, type=lambda x: int(x,0),
                        help="""All characters with RGB24 background color""",
                        default=[])

    parser.add_argument('-f', '--fullscreen',
                        action='store_true', help='fullscreen flag',
                        default=False)

    parser.add_argument('-i', '--invertPattern',
                        action='store_true',
                        help=""""invert
                        Braile characters flag""",
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
                        help="""save file""",
                        default="")

    parser.add_argument('-t', '--threshold', metavar=("Threshold"),
                        nargs=1, type=int,
                        help="""set threshold to binarize img in
                        braile convertion (0-255)""",
                        default=[0x7f])

    parser.add_argument('inputImage', type=str,
                        help='image to be converted'
                        )

    return parser.parse_args(args)

def main(argv=None):
    """
    Handles all the program parameters and
    calls to perform the convertion

    Parameter
    ---------
    argv : list
        A list of parameters

    Returns
    -------
    str
        The result of convertion
    """

    # Create parser
    if( argv is None ):
        args = create_parser(sys.argv[1:])
    else:
        args = create_parser(argv)
    # Create command instance and process commands
    commands = BraileCmd(args)
    # Call convert method
    result = commands.convert()
    # should i return result of convertion ?
    # return result

