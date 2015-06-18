__author__ = 'cwong_000'

import hand

class PlayerStrat():

    def __init__(self):
        pass

    def hits(self, hand):
        return raw_input("(h)it or (s)tand: ") == "h"