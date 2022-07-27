import random
# Input must be separated as follows: Team-Name Nationality
A1, A1N = input("A1 & nation, A2 & nation, B1 & nation, etc :\n").split()
A2, A2N = input().split()
B1, B1N = input().split()
B2, B2N = input().split()
C1, C1N = input().split()
C2, C2N = input().split()
D1, D1N = input().split()
D2, D2N = input().split()
E1, E1N = input().split()
E2, E2N = input().split()
F1, F1N = input().split()
F2, F2N = input().split()
G1, G1N = input().split()
G2, G2N = input().split()
H1, H1N = input().split()
H2, H2N = input().split()
# Dictionaries for group winners and runner ups, with names as keys and nationalities as values
winnerDict = {A1: A1N, B1: B1N, C1: C1N, D1: D1N, E1: E1N, F1: F1N, G1: G1N, H1: H1N}
runnerDict = {A2: A2N, B2: B2N, C2: C2N, D2: D2N, E2: E2N, F2: F2N, G2: G2N, H2: H2N}

print("group winners:" + "\n" + str(winnerDict))
print("group runners:" + "\n" + str(runnerDict))
# Turning the dictionaries into lists for indexing while retaining both keys and values
# Notice that I needed to alter list of runnerDict twice so I declared two variables
winnerList = list(winnerDict.items())
runnerList = list(runnerDict.items())
winnerPot = winnerList.copy()
runnerPot = runnerList.copy()
# Since each item in the lists is a list of team names and nations respectively, we save the index of the name in name variable, and index of the nation in nation variable, to ease the readability of the code
name = 0
nation = 1
# A function for making a list of eligible winners for a certain runner and append them in a pot of eligible winners
def eligibleWinners(runner, winners):
    for winner in winners:
        # The rule for an eligible winner are
            # 1. Has a different nation from the runner
            # 2. Is from a different group from the runner
        if runner[nation] != winner[nation] and runnerList.index(runner) != winnerList.index(winner):
            eligibleWinnersPot.append(winner)

match = 1
while len(runnerPot) > 0:
    # Initialize the pot of eligible winners every loop iteration, as we are yet to choose a runner
    eligibleWinnersPot = []
    # The max number of teams from the same nation is five
    # There is a special case where there are six winners, a runner team would find that four of the six winners are of the same of that runner's nation, and the fifth winner is of the same group oof the runner, then the sixth winner is paired automatically with that runner
    # This can also happen with less than six winners, eg. five winners with four of them of the same nation of the spicific runner, or three of the same nation and one of the same group of the runner
    if len(winnerPot) <= 6:
        # That special case is saved in the specialCase variable
        specialCase = False
        for runner in runnerPot:
            # Initialize the pot of eligible winners every loop iteration, as we change the runner every iteration
            eligibleWinnersPot = []
            eligibleWinners(runner, winnerPot)
            # If the special case happens, print the match, remove the teams from their respective pots and break out of the inner loop
            if len(eligibleWinnersPot) == 1:
                winner = eligibleWinnersPot[0]
                print("Match #" + str(match) +": " + runner[name] +" (" + runner[nation] + ") V " + winner[name] +" (" + winner[nation] + ")")
                runnerPot.remove(runner)
                winnerPot.remove(winner)
                match += 1
                specialCase = True
                break
        # If the special case happens, skip the outer loop iteration
        if specialCase == True:
            continue
    # If the special case does not happen, choose the runner randomly, make a list of the eligible winners and choose a winner from that list
    runner = random.choice(runnerPot)
    eligibleWinners(runner, winnerPot)
    winner = random.choice(eligibleWinnersPot)
    # Print the match, remove the teams from their respective pots and break out of the inner loop
    print("Match #" + str(match) +": " + runner[name] +" (" + runner[nation] + ") V " + winner[name] +" (" + winner[nation] + ")")
    runnerPot.remove(runner)
    winnerPot.remove(winner)
    match += 1

'''
2021-2022 UCL season winners and runners
Manchester-City England
Paris-Saint-Germain France
Liverpool England
Atlético-Madrid Spain
Ajax Holland
Sporting-CP Portugal
Real-Madrid Spain
Inter-Milan Italy
Bayern-Munich Germany
Benfica Portugal
Manchester-United England
Villarreal Spain
Lille France
Red-Bull-Salzburg Austria
Juventus Italy
Chelsea England
'''