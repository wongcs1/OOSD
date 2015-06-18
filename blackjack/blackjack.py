__author__ = 'cwong_000'

import sys
import deck
import participant
import playerstrat
import housestrat


d = deck.Deck()
d.shuffle()
p = participant.Player(playerstrat.PlayerStrat())
h = participant.HousePlayer(housestrat.HouseStrat())
p.drawcard(d.next())
h.drawcard(d.next())
p.drawcard(d.next())
h.drawcard(d.next())

print("House: " + h.showcardfacedown())
print("You: " + p.showhand())

print("Your play")
while(p.hits()):
    p.drawcard(d.next())
    print("House: " + h.showcardfacedown())
    print("You: " + p.showhand())
    print("==========")
    if(p.score() > 21):
        print("Busted!")
        sys.exit()
    print("")

print("")
print("House plays")
print("House: " + h.showhand())
print("You: " + p.showhand())
print("==========")
print("")
while(h.hits()):
    h.drawcard(d.next())
    print("House: " + h.showhand())
    print("You: " + p.showhand())
    print("==========")
    if(h.score() > 21):
        print("Busted!")
        sys.exit()
    print("")

if(p.score() > h.score()):
    print("You win!")
else:
    print("House wins!")
