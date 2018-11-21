"""
Dance moves generator. Run this to generate random dance moves.
Goals for this package:
  - Have it use multiple modules
  - Be able to run from the command line with flags
    - Flags : [-h] [-m [MOVE]]
  - Use virtual environment
  - Dance moves stored in separate file
  - It's gonna be kinda overengineered but that's ok
 """

import genfuncs
import random

MOVES = ['right-side pass', 'left-side pass', 'sugar-push',
         'sugar tuck', 'whip', 'inside turn', 'outside turn',]


def main():
    first = genfuncs.random_move(MOVES)
    second = genfuncs.random_move(MOVES)
    print('Combine {0} and {1}'.format(first, second))

if __name__ == "__main__":
    main()