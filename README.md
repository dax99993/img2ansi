<div align="center">
  <h3>
img2ansi is a simple package containing three CLI to convert an image to an ASCII, BRAILE/DOT, BLOCK representation with support for <a href ="https://en.wikipedia.org/wiki/ANSI_escape_code" > ANSI escape code sequence </a>
  </h3>
</div>

<div align="center">
  <a href="https://github.com/dax99993/img2ansi/blob/main/demo/demo.md">Demo</a>
  <br/><br/>
  <a href="https://github.com/dax99993/img2ansi/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL2-greee.svg?style=flat-square" alt="license" />
  </a>
  <a href="https://pypi.org/project/PIL/">
    <img src="https://img.shields.io/badge/Dependencies-PIL-blue.svg?style=flat-square" alt="dependencies" />
  </a>
  <a href="https://pypi.org/project/img2ansi/">
    <img src="https://img.shields.io/badge/Package-img2ansi-red.svg?style=flat-square" alt="dependencies" />
  </a>
</div>

## Installation

```bash
$ Python3 -m pip install img2ansi
```

## Features
- ASCII convertion
- BRAILE/DOT convertion
- Block convertion
- Custom ASCII character set
- Invert character set
- No echo **/** echo to terminal
- Resize of image
- Save to a file
- True color

## ANSI support
- Bold
- Blink
- True color Foreground
- True color Background 

## Todo
- [x] Simple Ascii convertion
- [x] Color support
- [ ] Multiple file handling
- [ ] Simple animation

## Usage
img2ansi contains three modules to perform different kind of convertion
-img2ascii
-img2braile
-img2block
```
usage: img2ascii [-h] [-a Character Set] [-F R G B] [-B R G B] [-b] [-c] [-f]
                 [-i] [-k] [-n] [-r Width Height] [-o [output filename]]
                 inputImage

Convert img to Ascii representation

positional arguments:
  inputImage            image to be converted

optional arguments:
  -h, --help            show this help message and exit
  -a Character Set, --asciicharset Character Set
                        ascii character set (default : " .~*:+zM#&@$" )
  -F R G B, --frgdcolor R G B
                        All characters with RGB24 foreground color
  -B R G B, --bkgdcolor R G B
                        All characters with RGB24 background color
  -b, --bold            bold flag
  -c, --color           foreground text as img colors
  -f, --fullscreen      fullscreen flag
  -i, --invertPattern   "invert ascii character set
  -k, --blink           blink flag
  -n, --noecho          no echo flag
  -r Width Height, --resize Width Height
                        resize image (0 0 keeps original size), if given -r
                        100 0 keeps aspectratio with 100px width
  -o [output filename], --save [output filename]
                        save file (if no output filename) defaults to
                        ascii.txt

By default uses parameters -r 0 0 -a " .~*:+zM#&@$"

```

```
usage: img2braile [-h] [-b] [-F R G B] [-B R G B] [-f] [-i] [-k] [-n]
                  [-r Width Height] [-o [output filename]] [-t Threshold]
                  inputImage

Convert img to Braile representation

positional arguments:
  inputImage            image to be converted

optional arguments:
  -h, --help            show this help message and exit
  -b, --bold            bold flag
  -F R G B, --frgdcolor R G B
                        All characters with RGB24 foreground color
  -B R G B, --bkgdcolor R G B
                        All characters with RGB24 background color
  -f, --fullscreen      fullscreen flag
  -i, --invertPattern   "invert Braile characters flag
  -k, --blink           blink flag
  -n, --noecho          no echo flag
  -r Width Height, --resize Width Height
                        resize image (0 0 keeps original size), if given -r
                        100 0 keeps aspectratio with 100px width
  -o [output filename], --save [output filename]
                        save file (if no output filename) defaults to
                        braile.txt
  -t Threshold, --threshold Threshold
                        set threshold to binarize img in braile convertion
                        (0-255)

By default -r 0 0 -t 127

```

```
usage: img2block [-h] [-f] [-W] [-k] [-n] [-r Width Height]
                 [-o [output filename]]
                 inputImage

Convert img to Block representation

positional arguments:
  inputImage            image to be converted

optional arguments:
  -h, --help            show this help message and exit
  -f, --fullscreen      fullscreen flag
  -W, --wholeblock      "Use one block per terminal cell
  -k, --blink           blink flag
  -n, --noecho          no echo flag
  -r Width Height, --resize Width Height
                        resize image (0 0 keeps original size), if given -r
                        100 0 keeps aspectratio with 100px width
  -o [output filename], --save [output filename]
                        save file (if no output filename) defaults to
                        block.txt

By default uses 2 blocks per terminal cell and -r 0 0

```

## License
[GPL2](https://github.com/dax99993/img2ansi/blob/main/LICENSE)
