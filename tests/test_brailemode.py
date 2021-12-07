from img2ansi.img2ansi import main
#from os import get_terminal_size
#from img2ansi.commands import Commands
import argparse

def test_braile_convertion():
    # Test keep original size, not print result
    print("""Braile mode -D,
            Keep original size -r 0 0,
            noecho (externally echoed to visual check) -n
            Threshold -t 150
            Bold -b
          """)
    res = main(['tests/test_pic3.jpg','-D', '-n', '-r', '0', '0', '-t', '150', '-b'])
    # Print externally to visually verify it
    print("".join(res))
    assert res != ""


def test_braile_resize_width():
    print("""Braile mode -D,
            Keep aspect ratio given WIDTH size -r 30 0,
            Color -c 255 150 150
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic2.webp','-D', '-r', '30', '0', '-c', '255', '150', '150'])
    assert res != ""

def test_braile_resize_height():
    print("""Braile mode -D,
            Keep aspect ratio given WIDTH size -r 0 40,
            Blink -k
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg','-D', '-r', '0', '40', '-k'])
    assert res != ""

