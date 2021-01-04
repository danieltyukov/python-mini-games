from random import random
from random import randrange

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def printIntro():
    print("This program simulates a game of racquetball between two")
    print("Players called A and B. The ability of each player is ")
    print("indicated by a probability (the number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def getInputs():
    # Returns the three simulation parameters
    a = float(input("Input the probability for player A "))
    b = float(input("Input the probability for play B "))
    n = int(input("How many games to simulate: "))
    return a, b, n


def simNGames(n, probA, probB):
    # Simulates n games of requetball between players whose
    # abilities are represented by the probability of winning a serve
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB + 2:
            winsA = winsA + 1
        elif scoreB > scoreA + 2:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    # simulates a single game of requetball between players whose
    # abilities are represented by the probability of winning a serve
    # Returns final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB


def gameOver(a, b):
    # a and b represent scores for a requetball game
    # Returns True if the game is over, False otherwise
    return a == 25 or b == 25


def printSummary(winsA, winsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print("\nGames simulated: ", n)
    print("wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))


if __name__ == "__main__":
    main()