import random

cards = ["A", 2, 3, 4, 5, 6, 7,8,9,10, "J", "Q", "K"]

myCards = []
dealerCards = []
total = 0

def deal():
    myCards.append(cards[random.randint(0,len(cards) - 1)])
    myCards.append(cards[random.randint(0,len(cards) - 1)])
    dealerCards.append(cards[random.randint(0,len(cards) - 1)])
    dealerCards.append(cards[random.randint(0,len(cards) - 1)])
    print("Your cards: ")
    print(myCards)
    print("Dealer cards: ")
    firstDealerCard = str(dealerCards[0])
    print("[" + firstDealerCard + ", _ ]")

def hitme():
    myCards.append(cards[random.randint(0,len(cards) - 1)])
    if(sumCards(myCards) > 21):
        print("Game Over! You Lose!")
        print(myCards)
        print(dealerCards)

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
    dealerTotal = sumCards(dealerCards)
    while(dealerTotal < 16):
        dealerCards.append(cards[random.randint(0,len(cards) - 1)])
        dealerTotal = sumCards(dealerCards)
    return dealerTotal


deal()
print(myCards)
print(dealerCards)
hitme()
print(myCards)
print(sumCards(myCards))
dealer()
print(sumCards(dealerCards))