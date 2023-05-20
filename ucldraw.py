import random
from xml.dom.minidom import Notation

print("Which draw would you like to simulate?")
while True:
    # Save the type of draw in a variable
    draw = input("1) Round of 16\n2) Finals (Quarter-finals and beyond)\n")
    # Code for round of 16 draw
    if draw == '1':
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
        # Pots are lists of the teams that are yet to be paired
        winnerPot = winnerList.copy()
        runnerPot = runnerList.copy()
        # To ease the readability of the , we will save the index of the team names in a variable called name, and the same for the team nations
        # TODO: make a variable for group name
        name = 0
        nation = 1

        def eligibleWinners(runner):
            '''
            A function for making a list of eligible opponents for a certain runner from the winnersPot list,and append them in a pot of eligible winners, called eligibleWinnersPot.
            Each eligible opponent must be:
                1. A winner team (seeded teams V unseeded teams rule)
                2. Of a different nation from the runner (country protection rule)
                3. From a different group from the runner (group protection rule)

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
                        print("Match #" + str(match) + ": " + runner[name] + " " * (20 - len(runner[name])) + "(" + runner[nation] + ")" + " " * (16 - len(runner[nation])) + "(Group " + chr(65 + runnerList.index(runner)) + ") V " + winner[name] + " " * (20 - len(winner[name])) + "(" + winner[nation] + ")" + " " * (16 - len(winner[nation])) + "(Group " + chr(65 + winnerList.index(winner)) + ")")
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
            print("Match #" + str(match) + ": " + runner[name] + " " * (20 - len(runner[name])) + "(" + runner[nation] + ")" + " " * (16 - len(runner[nation])) + "(Group " + chr(65 + runnerList.index(runner)) + ") V " + winner[name] + " " * (20 - len(winner[name])) + "(" + winner[nation] + ")" + " " * (16 - len(winner[nation])) + "(Group " + chr(65 + winnerList.index(winner)) + ")")
            runnerPot.remove(runner)
            winnerPot.remove(winner)
            match += 1

        # 2021-2022 UCL season group winners and runners
        '''
Manchester City - England
Paris Saint Germain - France
Liverpool - England
Atlético Madrid - Spain
Ajax - The Netherlands
Sporting CP - Portugal
Real Madrid - Spain
Inter Milan - Italy
Bayern München - Germany
Benfica - Portugal
Manchester United - England
Villarreal - Spain
Lille - France
Red Bull Salzburg - Austria
Juventus - Italy
Chelsea - England
        '''
    # Code for finals draw
    elif draw == '2':
        # Input must be separated as follows: Team Name - Nationality
        T1 = input("Team 1, Team 2, etc:\n")
        T2 = input()
        T3 = input()
        T4 = input()
        T5 = input()
        T6 = input()
        T7 = input()
        T8 = input()
        # Make a list of the teams, this list will decrease with each pairing
        teamPot = [T1, T2, T3, T4, T5, T6, T7, T8]
        # Choose randomly two pairs from the list, print the match with proper spacing and remove the teams from the teamPot list
        # This time, there are no rules. This is completely random draw
        match = 1
        while len(teamPot) > 0:
            home = random.choice(teamPot)
            teamPot.remove(home)
            away = random.choice(teamPot)
            teamPot.remove(away)
            print("Quarter-final #" + str(match) + ": " + home + " " * (20 - len(home)) + "V" + " " * (20 - len(away)) + away)
            match += 1
        # Print the semi-finals matches, where names are anonymous
        semisPot = [1, 2, 3, 4]
        match = 1
        while len(semisPot) > 0:
            home = random.choice(semisPot)
            semisPot.remove(home)
            away = random.choice(semisPot)
            semisPot.remove(away)
            print("Semi-final #" + str(match) + ": Quarter-final #" + str(home) + " winner V " + "Quarter-final #" + str(away) + " winner")
            match += 1
        # Print the finals match, where names are anonymous. This is done for operational reasons
        home = random.randrange(1, 3)
        if home == 1:
            away = 2
            print("Final" + ": Semi-final #" + str(home) + " winner V " + "Semi-final #" + str(away) + " winner")
        else:
            away = 1
            print("Final" + ": Semi-final #" + str(home) + " winner V " + "Semi-final #" + str(away) + " winner")
        # 2021-2022 UCL season Quarter-finals qualifiers
        '''
Manchester City
Liverpool
Atlético Madrid
Real Madrid
Bayern München
Benfica
Villarreal
Chelsea
        '''
    # If the user inputs a letter, or inputs a number other than 1, 2 or 3
    else:
        print("Please choose either 1 or 2")
        continue
    # A way to exit the program
    print("Do you want to continue the program?")
    while True:
        answer = input("[c]ontinue\n[q]uit\n")
        if answer == 'c':
            print("Which draw would you like to simulate?")
            break
        elif answer == 'q':
            quit = True
            break
        else:
            print("Please choose a valid answer")
    if quit == True:
        break