from img2ansi.img2ansi import main
#from os import get_terminal_size
from img2ansi.commands import Commands
import argparse

def test_block_convertion():
    # Test keep original size, not print result
    print("""Block mode -B,
            Keep original size -r 0 0,
            noecho (externally echoed to visual check) -n
          """)
    res = main(['tests/test_pic1.png','-B', '-n', '-r', '0', '0' ])
    # Print externally to visually verify it
    print("".join(res))
    assert res != ""


def test_block_resize_width():
    print("""Block mode -B,
            Keep aspect ratio given WIDTH size -r 30 0,
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic2.webp','-B', '-r', '30', '0'])
    assert res != ""

def test_block_resize_height():
    print("""Block mode -B,
            Keep aspect ratio given WIDTH size -r 0 40,
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg','-B', '-r', '0', '40'])
    assert res != ""

#def test_block_fullscreen_resize_height():
#    print("""Block mode -B,
#            Fullscreen -F
#           Keep aspect ratio given WIDTH size -r 0 10,
#          """)
#    # Output should have square dimensions
#    res = main(['tests/test_pic3.jpg','-B', '-F', '-r', '0', '40'])
#    assert res != ""
