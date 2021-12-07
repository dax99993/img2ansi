#!/usr/bin/env python3

import argparse
import sys
from img2ansi.blockcmd import BlockCmd


def create_parser(args):
    """Creates an argument parser for the img2block CLI

    Returns
    -------
    argparse
        a set of args to perform specified convertion
    """

    # Setup parser
    parser = argparse.ArgumentParser(
        description="Convert img to Block representation",
        epilog="""By default -r 0 0 """,
    )

    parser.add_argument('-F', '--fullscreen',
                        action='store_true', help='fullscreen flag',
                        default=False)

    #add flag for hald block or full block
    #parser.add_argument('-', '--invertPattern',
    #                    action='store_true',
    #                    help=""""Invert ascii character set or
    #                    Braile characters flag""",
    #                    default=False)

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
                        defaults to block.txt""",
                        default="block.txt")

    parser.add_argument('inputImage', type=str,
                        help='image to be converted'
                        )

    return parser.parse_args(args)

def main(argv=None):
    #if __name__ == '__main__':
    # Create parser
    if( argv is None ):
        args = create_parser(sys.argv[1:])
    else:
        args = create_parser(argv)
    # Create command instance and process commands
    commands = BlockCmd(args)
    # Call convert method
    result = commands.convert()
    # return result of convertion
    return result

