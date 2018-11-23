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

import random
from itertools import combinations

import genfuncs

MOVES = ['right-side pass', 'left-side pass', 'sugar-push',
		 'sugar tuck', 'whip', 'inside turn', 'outside turn', ]

OPERATORS = ['Rock and Go!']


def main():
	print("\nm : random move\n" + "c : random two moves\n" + "q : quit\n")
	mv = MOVES.copy()
	mvs = genfuncs.random_comb(MOVES.copy())

	while True:

		f = input()
		
		if f == 'm':
			op = random.choice([0, 1])
			print(mv.pop())
			if op:
				print(random.choice(OPERATORS))
			if not mv:
				mv = MOVES.copy()


		elif f == 'c':
			op = random.choice([0, 1])
			print(mvs.pop())
			if op:
				print(random.choice(OPERATORS))
			if not mvs:
				mvs = genfuncs.random_comb(MOVES.copy())

		elif f == 'q':
			break

if __name__ == '__main__':
	main()
