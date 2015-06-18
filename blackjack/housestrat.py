__author__ = 'cwong_000'

import hand

class HouseStrat():

    def __init__(self):
        pass

    def hits(self, hand):
        if hand.score() > 17:
            return False
        else:
            return True