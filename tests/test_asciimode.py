from img2ansi.img2ascii import main
import argparse

def test_ascii_convertion():
    # Test keep original size, not print result
    print("""Ascii,
            Keep original size -r 0 0,
            noecho (externally echoed to visual check) -n
            Bold -b
          """)
    res = main(['tests/test_pic3.jpg','-n', '-r', '0', '0', '-b'])
    # Print externally to visually verify it
    print("".join(res))
    assert res != ""


def test_ascii_resize_width():
    print("""Ascii,
            Keep aspect ratio given WIDTH size -r 30 0,
            Blink -k
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic2.webp', '-r', '30', '0', '-k'])
    assert res != ""

def test_ascii_resize_height():
    print("""Ascii,
            Keep aspect ratio given WIDTH size -r 0 40,
            Foreground -f
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg', '-r', '0', '40', '-f'])
    assert res != ""

