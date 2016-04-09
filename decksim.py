import random
import sys

def hitLand(numlands, numcards):
    deck = []
    for i in range(numlands):
        deck.append(1)
    for i in range (numcards - numlands):
        deck.append(0)

    hand = []
    for i in range(7):
        x = random.choice(deck)
        hand.append(x)
        if x == 0:
            deck.pop()
        if x == 1:
            deck.pop(0)
    return hand


def deckSim(numlands, trials):
    trial = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(trials):
        x = hitLand(numlands, 99)
        trial[sum(x)] += 1

    for i in range(len(trial)):
        trial[i] = trial[i] * 100 // trials
        
        
    return trial


if __name__ == '__main__':
    print(deckSim(int(sys.argv[1]), int(sys.argv[2])))
