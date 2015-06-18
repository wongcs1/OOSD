__author__ = 'cwong_000'
import card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in "CDHS":
            for val in range(2, 11):
                self.cards.append(card.Card(val, suit))
            for val in "AKQJ":
                self.cards.append(card.Card(val, suit))


    def next(self):
        return self.cards.pop()

def shuffle(d):
    random.shuffle(d.cards)

def manual_swap(d, pos1, pos2):
        ctemp = d[pos1]
        d[pos1] = d[pos2]
        d[pos2] = ctemp

def odd_even_shuffle(d):
    for _ in xrange(52):
        c1 = random.randrange(1,52,2)
        c2 = random.randrange(0,52,2)
        manual_swap(d, c1, c2)
