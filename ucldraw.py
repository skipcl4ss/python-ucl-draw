import random
from xml.dom.minidom import Notation

print("Which draw would you like to simulate?")
while True:
    # Save the type of draw in a variable
    draw = input("1) Group stage\n2) Round of 16\n3) Finals (Quarter finals and beyond)\n")
    # Code for group stage draw
    # TODO: complete the case
    if draw == '1':
        pass
    # Code for round of 16 draw
    elif draw == '2':
        # Input must be separated as follows: Team Name - Nationality
        A1, A1N = input("A1 & nation, A2 & nation, B1 & nation, etc :\n").split(sep = " - ")
        A2, A2N = input().split(sep = " - ")
        B1, B1N = input().split(sep = " - ")
        B2, B2N = input().split(sep = " - ")
        C1, C1N = input().split(sep = " - ")
        C2, C2N = input().split(sep = " - ")
        D1, D1N = input().split(sep = " - ")
        D2, D2N = input().split(sep = " - ")
        E1, E1N = input().split(sep = " - ")
        E2, E2N = input().split(sep = " - ")
        F1, F1N = input().split(sep = " - ")
        F2, F2N = input().split(sep = " - ")
        G1, G1N = input().split(sep = " - ")
        G2, G2N = input().split(sep = " - ")
        H1, H1N = input().split(sep = " - ")
        H2, H2N = input().split(sep = " - ")
        # Lists for group winners and runner ups, with nested lists of names and nationalities of each team
        winnerList = [[A1, A1N], [B1, B1N], [C1, C1N], [D1, D1N], [E1, E1N], [F1, F1N], [G1, G1N], [H1, H1N]]
        runnerList = [[A2, A2N], [B2, B2N], [C2, C2N], [D2, D2N], [E2, E2N], [F2, F2N], [G2, G2N], [H2, H2N]]

        print("group winners:" + "\n" + str(winnerList))
        print("group runners:" + "\n" + str(runnerList))
        # Pots are lists of the teams that are yet to be paired
        winnerPot = winnerList.copy()
        runnerPot = runnerList.copy()
        # To ease the readability of the , we will save the index of the team names in a variable called name, and the same for the team nations
        # TODO: make a variable for group name
        name = 0
        nation = 1

        def eligibleWinners(runner):
            '''
            A function for making a list of winners from winnerPot list, which are eligible for a certain runner and append them in a pot of eligible winners, where each eligible winner must be:
                1. Of a different nation from the runner
                2. From a different group from the runner

                Parameters:
                    runner (list): A list of of two elements, the first being the name of the runner, the second being its nation. Represents the runner in question.

                Returns:
                    eligibleWinnersPot (list): a list of lists, each nested list contains two elements, winner name and nation.
            '''
            eligibleWinnersPot = []
            for winner in winnerPot:
                if runner[nation] != winner[nation] and runnerList.index(runner) != winnerList.index(winner):
                    eligibleWinnersPot.append(winner)
            return eligibleWinnersPot

        match = 1
        while len(runnerPot) > 0:
            # The max number of teams from the same nation is five
            # There is a special case where there are six winners, a runner team would find that four of the six winners are of the same of that runner's nation, and the fifth winner is of the same group oof the runner, then the sixth winner is paired automatically with that runner
            # This can also happen with less than six winners, eg. five winners with four of them of the same nation of the spicific runner, or three of the same nation and one of the same group of the runner
            if len(winnerPot) <= 6:
                # That special case is saved in the specialCase variable
                specialCase = False
                for runner in runnerPot:
                    eligibleWinners(runner)
                    # If the special case happens, print the match (team name, nation and group) with proper spacing, remove the teams from their respective pots and break out of the inner loop
                    if len(eligibleWinners(runner)) == 1:
                        winner = eligibleWinners(runner)[0]
                        print("Match #" + str(match) +": " + runner[name] + " " * (20 - len(runner[name])) + "(" + runner[nation] + ")" + " " * (16 - len(runner[nation])) + "(Group " + chr(65 + runnerList.index(runner)) + ") V " + winner[name] + " " * (20 - len(winner[name])) + "(" + winner[nation] + ")" + " " * (16 - len(winner[nation])) + "(Group " + chr(65 + winnerList.index(winner)) + ")")
                        runnerPot.remove(runner)
                        winnerPot.remove(winner)
                        match += 1
                        specialCase = True
                        break
                # If the special case happens, skip the outer loop iteration
                if specialCase == True:
                    continue
            # If the special case does not happen, choose the runner randomly, pair it with a random winner from the eligible winners
            runner = random.choice(runnerPot)
            winner = random.choice(eligibleWinners(runner))
            # Print the match (team name, nation and group) with proper spacing and remove the teams from their respective pots
            print("Match #" + str(match) +": " + runner[name] + " " * (20 - len(runner[name])) + "(" + runner[nation] + ")" + " " * (16 - len(runner[nation])) + "(Group " + chr(65 + runnerList.index(runner)) + ") V " + winner[name] + " " * (20 - len(winner[name])) + "(" + winner[nation] + ")" + " " * (16 - len(winner[nation])) + "(Group " + chr(65 + winnerList.index(winner)) + ")")
            runnerPot.remove(runner)
            winnerPot.remove(winner)
            match += 1

        # 2021-2022 UCL season winners and runners
        '''
Manchester City - England
Paris Saint Germain - France
Liverpool - England
Atlético Madrid - Spain
Ajax - The Netherlands
Sporting CP - Portugal
Real Madrid - Spain
Inter Milan - Italy
Bayern Munich - Germany
Benfica - Portugal
Manchester United - England
Villarreal - Spain
Lille - France
Red Bull Salzburg - Austria
Juventus - Italy
Chelsea - England
        '''
    # Code for finals draw
    # TODO: complete the case
    elif draw == '3':
        # Input must be separated as follows: Team-Name Nationality
        team1 = input("Team 1 & nation, Team 2 & nation, etc:")
        print(team1)
    # If the user inputs a letter, or inputs a number other than 1, 2 or 3
    else:
        print("Please choose a number between 1 to 3")
        continue
    # A way to exit the program
    if input("Press enter to repeat the program, or anywhere else to exit\n") != '':
        break
    else:
        print("Which draw would you like to simulate?")