import random

cards = ["A", 2, 3, 4, 5, 6, 7,8,9,10, "J", "Q", "K"]

myCards = []
dealerCards = []
total = 0

def yourCards():
    myCards.append(cards[randomint(0,len(cards) - 1)])
    myCards.append(cards[randomint(0,len(cards) - 1)])

def hitme():
    myCards.append(cards[randomint(0,len(cards) - 1)])

def sumCards(cards):
    total = 0
    for card in cards:
        if(card == "J" or card == "Q" or card == "K"):
            total += 10
        elif(card == "A"):
            total += 11
        else:
            total += card
    if(total > 21):
        if("A" in cards):
            total -= 10

    return total


def dealer():
