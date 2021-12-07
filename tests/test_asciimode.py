from img2ansi.img2ansi import main
#from os import get_terminal_size
#from img2ansi.commands import Commands
import argparse

def test_ascii_convertion():
    # Test keep original size, not print result
    print("""Ascii mode -A,
            Keep original size -r 0 0,
            noecho (externally echoed to visual check) -n
            Threshold -t 150 (shouldn't do anything in this mode)
            Bold -b
          """)
    res = main(['tests/test_pic3.jpg','-A', '-n', '-r', '0', '0', '-t', '150', '-b'])
    # Print externally to visually verify it
    print("".join(res))
    assert res != ""


def test_ascii_resize_width():
    print("""Ascii mode -A,
            Keep aspect ratio given WIDTH size -r 30 0,
            Color -c 255 0 0 (shouldn't do anything in this mode)
            Blink -k
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic2.webp','-A', '-r', '30', '0', '-c', '255', '0', '0', '-k'])
    assert res != ""

def test_ascii_resize_height():
    print("""Ascii mode -A,
            Keep aspect ratio given WIDTH size -r 0 40,
            Foreground -f
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg','-A', '-r', '0', '40', '-f'])
    assert res != ""

