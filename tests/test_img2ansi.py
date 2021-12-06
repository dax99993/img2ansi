from img2ansi.commands import Commands
import argparse
import sys

if __name__ == "__main__":
    #parser = argparse.ArgumentParser()
    #args = parse_args(['-B' '-r 30 0' '-c 255 0 255'] )
    commands = Commands(['inputImage tora.jpeg', '-B', '-r 30 0', '-c 255 0 255'])
