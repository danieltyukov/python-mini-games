from random import random
from random import randrange

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, RwinsA, RwinsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, RwinsA, RwinsB)
    
def printIntro():
    print("This program simulates two games of volleyball")
    print('with two separate scoring systems for investigation.')
    print("Rally scoring score points anytime while the other ")
    print("method scores only when team team scores when serving.")
    print("Game ends when a score of 25 is reached..\n")

def getInputs():
    # Returns the three simulation parameters
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    oddN = False
    while not oddN:
      n = eval(input("How many games to simulate? "))
      if n%2 != 0:
        oddN = True
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
    #while winsA < n/2 and winsB < n/2: # best of option
        scoreA, scoreB, rallyA, rallyB = simOneGame(n, probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
        RwinsA = 0
        RwinsB = 0
        if rallyA > rallyB:
            RwinsA = RwinsA + 1
        else:
            RwinsB = RwinsB + 1
    return winsA, winsB, rallyA, rallyB

def simOneGame(n, probA, probB):
    # Simulates a single game or volleyball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    if n%2 == 0:
        serving = "B"
    else:
        serving = "A"
        
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
                scoreB = scoreB + 1
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
                scoreA += 1
    rallyA = 0
    rallyB = 0
    while not gameOver(rallyA, rallyB):
        if serving == "A":
            if random() < probA:
                rallyA = rallyA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                rallyB += 1
            else:
                serving = "A"

    return scoreA, scoreB, rallyA, rallyB

def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return (a==25 or b==25)

def printSummary(winsA, winsB, RwinsA, RwinsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("\nServe based wins")
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print("\nRally wins")
    print("Wins for A: {0} ({1:0.1%})".format(RwinsA, RwinsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(RwinsB, RwinsB/n))
if __name__ == '__main__': main()