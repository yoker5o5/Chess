import sys
from sah import *

def main(*args):
    tabla()
    ucitajfigure()

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)