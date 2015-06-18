__author__ = 'cwong_000'

import re
import hand
import playerstrat
import housestrat

class Player:

    def __init__(self, strategy):
        self.hand = hand.Hand()
        self.strategy = strategy

    def addcard(self, newcard):
        self.hand.addcard(newcard)

    def showhand(self):
        return str(self.hand) + " Score: " + str(self.hand.calcscore())

    def hits(self):
        return self.strategy.hits(self.hand)

    def score(self):
        return self.hand.calcscore()


class HousePlayer(Player):

    def hits(self):
        return self.strategy.hits(self.hand)

    def showcardfacedown(self):
        cards = str(self.hand)
        #replace first card with '**'
        card_to_hide = re.compile("(^\w+)\s")
        return card_to_hide.sub("** ", cards)