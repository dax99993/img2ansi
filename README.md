<div align="center">
  <h3>
imgtoANSI is a simple CLI to convert an image to an ASCI or BRAILE/DOT representation with support for <a href ="https://en.wikipedia.org/wiki/ANSI_escape_code" > ANSI escape code sequence </a>
  </h3>
</div>

<div align="center">
  <a href="https://github.com/dax99993/imgtoANSI/blob/main/demo/demo.md">Demo</a>
  <br/><br/>
  <a href="https://github.com/dax99993/imgtoANSI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="MIT" />
  </a>
  <a href="https://pypi.org/project/PIL/">
    <img src="https://img.shields.io/badge/Dependencies-PIL-blue.svg?style=flat-square" alt="dependencies" />
  </a>
</div>

## Installation

```bash
$ pip install img2ansi
```

## Features
- ASCII convertion
- BRAILE/DOT convertion
- Block convertion
- Custom ASCII character set
- Invert character set
- No echo **/** echo to terminal
- Resize of image convertion
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
- [ ] Save as HTML
- [ ] Multiple file handling
- [ ] Simple animation

## Usage
imgtoAnsi asumes default flags such that
the next uses are equal
```
usage: img2ansi [-h] [-a Character Set] [-A] [-b] [-B] [-c R G B] [-D] [-f]
                [-F] [-i] [-k] [-n] [-r Width Height] [-s [output filename]]
                [-t Threshold]
                inputImage

Convert img to Ascii or Braile representation

positional arguments:
  inputImage            image to be converted

optional arguments:
  -h, --help            show this help message and exit
  -a Character Set, --asciicharset Character Set
                        Ascii custom character set (default : " .~*:+zM#&@$" )
  -A, --ascii           Ascii Representation flag
  -b, --bold            Bold flag
  -B, --block           Block Representation flag
  -c R G B, --color R G B
                        Set Ansi RGB24 color of Braile representation, each
                        channel is 8bits
  -D, --braile          Dot/Braile Representation flag
  -f, --foreground      Ascii Foreground flag
  -F, --fullscreen      Fullscreen flag
  -i, --invertPattern   "Invert ascii character set or Braile characters flag
  -k, --blink           Blink flag
  -n, --noecho          No echo flag
  -r Width Height, --resize Width Height
                        Resize image (0 0 keeps original size), if given -r
                        100 0 keeps aspectratio with 100px width
  -s [output filename], --save [output filename]
                        Save file (if no output filename) defaults to
                        imgAscii.txt or imgBraile.txt or imgBlock.txt
  -t Threshold, --threshold Threshold
                        Set threshold to binarize img in braile convertion
                        (0-255)

By default utilizes -A -r 0 0

```

## License 
[MIT](https://github.com/dax99993/imgtoANSI/blob/main/LICENSE)
