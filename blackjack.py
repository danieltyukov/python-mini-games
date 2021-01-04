from random import random
from random import randrange

def printIntro():
    print("Playing blackjack to see the probability of dealer winning simulated")


def takeInput():
    n = int(input("How many games are we playing: "))
    return n


def simNgames(n):
    for i in range(n):
        dealerS, userS = simOnegame()
        if dealerS > 21:
            userS += 1
        else:
            dealerS += 1
    return dealerS, userS


def simOnegame():
    userS = dealerS = 0
    while dealerS < 21 and userS < 21:
        if dealerS >= 17:
            userS += 1
        else:
            dealerS += randrange(1, 12)
            userS += randrange(1, 12)
        if dealerS > 17:
            if randrange(1, 14) == 13:
                dealerS = dealerS - 10
        if userS > 17:
            if randrange(1, 14) == 13:
                userS = userS - 1
    return userS, dealerS


def getSummery(dealerS, userS, n):
    print("amount of games: ", n)
    print("how much user won: ", userS)
    print("how much dealer won: ", dealerS)
    if userS == 0:
        print("Dealer did not bust")
    elif userS / n == 1:
        print("Dealer did bust")
    else:
        print("the probability the dealer will bust is: ({0:0.1%})".format(userS / n))


def main():
    printIntro()
    n = takeInput()
    dealerS, userS = simNgames(n)
    getSummery(dealerS, userS, n)


main()