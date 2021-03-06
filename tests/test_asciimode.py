from img2ansi.img2ascii import main
import argparse

def test_ascii_convertion():
    # Test keep original size, not print result
    print("""Ascii,
            Keep original size -r 0 0,
            noecho (externally echoed to visual check) -n
            Bold -b
            Foreground -F
          """)
    res = main(['tests/test_pic3.jpg',
                '-n', '-r', '0', '0', '-b',
                '-F', '0', '255', '0'])
    assert res == ""


def test_ascii_resize_width():
    print("""Ascii,
            Keep aspect ratio given WIDTH size -r 30 0,
            Blink -k
            Background -B
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic2.webp',
                '-r', '30', '0', '-k',
                '-B', '0', '255', '255'])
    print("Externally printing result for check!")
    print(res)
    assert res != ""

def test_ascii_resize_height():
    print("""Ascii,
            Keep aspect ratio given WIDTH size -r 0 40,
            Color -c
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg', '-r', '0', '40', '-c'])
    print("Externally printing result for check!")
    print(res)
    assert res != ""

def test_ascii_charset():
    print("""Ascii,
            Keep aspect ratio given WIDTH size -r 0 40,
            Color -c
            Charset -a "abcd"
          """)
    # Output should have square dimensions
    res = main(['tests/test_pic4.jpeg', '-r', '0', '40', '-c', '-a', 'abcd'])
    print("Externally printing result for check!")
    print(res)
    assert res != ""
