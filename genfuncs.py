""" 
Dance moves:
    - right-side pass
    - left-side pass
      - inside-turn
    - sugar-push
    - sugar-tuck
    - whip
      - outside-turn
      - inside-turn 
"""

import random

def random_move(mvs) -> str:
    """ Return a random element of mvs, pop it out of mvs. """
    random.shuffle(mvs)
    return mvs.pop()

