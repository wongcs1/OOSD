__author__ = 'cwong_000'

import deck

class Hand:

    def __init__(self):
        self.cards = []

    def addcard(self, card):
        self.cards.append(card)

    def numofcards(self):
        return len(self.cards)

    def calcscore(self):
        # sorting the aces and normal card out of the hand
        regular_cards = [c for c in self.cards if c.value != "A"]
        aces = [c for c in self.cards if c.value == "A"]

        points = 0

        for c in regular_cards:
            if isinstance(c.value, basestring):
                points += 10
            else:
                points += c.value
        # Add ace values
        for c in aces:
            if points + 11 <= 21:
                points += 11
            else:
                points += 1

        return points

    def __repr__(self):
        hand_string = ""
        for c in self.cards:
            hand_string += str(c)
            hand_string += " "
        return hand_string
