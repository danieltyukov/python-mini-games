from random import random
from random import randrange

def printIntro():
    print("This program simulates a number of games of craps.")
    print("The rules are that a player wins if they roll a pair ")
    print("of die with a total of 7 and 11, or lose with 2, 3, 12.")
    print("If you roll anything else you roll again to gain points.")


def getInputs():
    n = eval(input("\nHow many games to simulate? "))

    return n


def simNGames(n):
    wins = losses = 0
    for i in range(int(n)):
        wins, losses = simOneGame(wins, losses)
        print(wins, losses)
    return wins, losses


def simOneGame(wins, losses):
    dieTotal = int(randrange(1, 7)) + int(randrange(1, 7))
    loop = True
    while loop:
        if dieTotal == 2 or dieTotal == 3 or dieTotal == 12:
            losses = losses + 1
            loop = False
        elif dieTotal == 7 or dieTotal == 11:
            wins = wins + 1
            loop = False
        else:
            dieTotal = randrange(1, 6)
        return wins, losses


def printSummary(wins, losses, n):
    print(wins, losses, n)
    print("wins are: {0} ({1:0.1%})".format(wins, wins / n))


def main():
    printIntro()
    n = getInputs()
    wins, losses = simNGames(n)
    printSummary(wins, losses, n)


main()