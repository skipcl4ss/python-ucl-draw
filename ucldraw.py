import random

print("Which draw would you like to simulate?")
while True:
    # Save the type of draw in a variable
    draw = input("1) Group stage\n2) Round of 16\n3) Finals (Quarter-finals and beyond)\n")
    # Code for group stage draw
    # TODO: complete the case
    if draw == '1':
        Pot11, Pot11N = input("Pot 1 teams & nations:\n").split(sep = " - ")
        Pot12, Pot12N = input().split(sep = " - ")
        Pot13, Pot13N = input().split(sep = " - ")
        Pot14, Pot14N = input().split(sep = " - ")
        Pot15, Pot15N = input().split(sep = " - ")
        Pot16, Pot16N = input().split(sep = " - ")
        Pot17, Pot17N = input().split(sep = " - ")
        Pot18, Pot18N = input().split(sep = " - ")
        Pot21, Pot21N = input("Pot 2 teams & nations:\n").split(sep = " - ")
        Pot22, Pot22N = input().split(sep = " - ")
        Pot23, Pot23N = input().split(sep = " - ")
        Pot24, Pot24N = input().split(sep = " - ")
        Pot25, Pot25N = input().split(sep = " - ")
        Pot26, Pot26N = input().split(sep = " - ")
        Pot27, Pot27N = input().split(sep = " - ")
        Pot28, Pot28N = input().split(sep = " - ")
        Pot31, Pot31N = input("Pot 3 teams & nations:\n").split(sep = " - ")
        Pot32, Pot32N = input().split(sep = " - ")
        Pot33, Pot33N = input().split(sep = " - ")
        Pot34, Pot34N = input().split(sep = " - ")
        Pot35, Pot35N = input().split(sep = " - ")
        Pot36, Pot36N = input().split(sep = " - ")
        Pot37, Pot37N = input().split(sep = " - ")
        Pot38, Pot38N = input().split(sep = " - ")
        Pot41, Pot41N = input("Pot 4 teams & nations:\n").split(sep = " - ")
        Pot42, Pot42N = input().split(sep = " - ")
        Pot43, Pot43N = input().split(sep = " - ")
        Pot44, Pot44N = input().split(sep = " - ")
        Pot45, Pot45N = input().split(sep = " - ")
        Pot46, Pot46N = input().split(sep = " - ")
        Pot47, Pot47N = input().split(sep = " - ")
        Pot48, Pot48N = input().split(sep = " - ")

        Pot1 = {Pot11: Pot11N, Pot12: Pot12N, Pot13: Pot13N, Pot14: Pot14N, Pot15: Pot15N, Pot16: Pot16N, Pot17: Pot17N, Pot18: Pot18N}
        Pot2 = {Pot21: Pot21N, Pot22: Pot22N, Pot23: Pot23N, Pot24: Pot24N, Pot25: Pot25N, Pot26: Pot26N, Pot27: Pot27N, Pot28: Pot28N}
        Pot3 = {Pot31: Pot31N, Pot32: Pot32N, Pot33: Pot33N, Pot34: Pot34N, Pot35: Pot35N, Pot36: Pot36N, Pot37: Pot37N, Pot38: Pot38N}
        Pot4 = {Pot41: Pot41N, Pot42: Pot42N, Pot43: Pot43N, Pot44: Pot44N, Pot45: Pot45N, Pot46: Pot46N, Pot47: Pot47N, Pot48: Pot48N}

        groupA = ['A']; groupB = ['B']; groupC = ['C']; groupD = ['D']; groupE = ['E']; groupF = ['F']; groupG = ['G']; groupH = ['H']
        groups = [groupA, groupB, groupC, groupD, groupE, groupF, groupG, groupH]
        redGroups = [groupA, groupB, groupC, groupD]
        blueGroups = [groupE, groupF, groupG, groupH]

        name = 0
        nation = 1

        def firstEmptyGroup(grps):
            for group in grps:
                if len(group) == 1:
                    return group
        # TODO: there is a case where we may find that the red groups were filled, and we are left with two teams of the same nation in the blue teams
        def TVpairings(team):
            redCounter = 0
            for group in redGroups:
                for teams in group:
                    if group.index(teams) == 0:
                        continue
                    elif team[nation] == teams[nation]:
                        redCounter += 1

            blueCounter = 0
            for group in blueGroups:
                for teams in group:
                    if group.index(teams) == 0:
                        continue
                    elif team[nation] == teams[nation]:
                        blueCounter += 1

            if redCounter > blueCounter:
                firstEmptyGroup(blueGroups).append(team)
            elif blueCounter > redCounter:
                firstEmptyGroup(redGroups).append(team)
            else:
                firstEmptyGroup(groups).append(team)

        while len(Pot1) > 0:
            team = random.choice(list(Pot1.items()))
            print(team)
            TVpairings(team)
            print(groups)
            Pot1.pop(team[name])
            print(Pot1)

        for group in groups:
            for teams in group:
                if group.index(teams) == 0:
                    continue
                elif groups.index(group) != 3 and groups.index(group) != 7:
                    print(teams[name] + " (" + teams[nation] + ")" + " " * (28 - len(teams[name]) - len(teams[nation])), end = '')
                else:
                    print(teams[name] + " (" + teams[nation] + ")")
                    print()
        # print()
        # 2021-2022 UCL season group stage teams
        '''
Chelsea - England
Villarreal - Spain
Atlético Madrid - Spain
Manchester City - England
Bayern München - Germany
Inter Milan - Italy
Lille - France
Sporting CP - Portugal
Real Madrid - Spain
Barcelona - Spain
Juventus - Italy
Manchester United - England
Paris Saint-Germain - France
Liverpool - England
Sevilla - Spain
Borussia Dortmund - Germany
Porto - Portugal
Ajax - The Netherlands
Shakhtar Donetsk - Ukraine
RB Leipzig - Germany
Red Bull Salzburg - Austria
Benfica - Portugal
Atalanta - Italy
Zenit Saint Petersburg - Russia
Beşiktaş - Turkey
Dynamo Kyiv - Ukraine
Club Brugge - Belgium
Young Boys - Switzerland
Milan - Italy
Malmö FF - Sweden
VfL Wolfsburg - Germany
Sheriff Tiraspol - Moldova
        '''
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
        # Pots are lists of the teams that are yet to be paired
        winnerPot = winnerList.copy()
        runnerPot = runnerList.copy()
        # To ease the readability of the , we will save the index of the team names in a variable called name, and the same for the team nations
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
        print() # Make a new line
        # 2021-2022 UCL season group winners and runners
        '''
Manchester City - England
Paris Saint-Germain - France
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
    elif draw == '3':
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
        print() # Make a new line
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
        print() # Make a new line
        # Print the finals match, where names are anonymous. This is done for operational reasons
        home = random.randrange(1, 3)
        if home == 1:
            away = 2
            print("Final" + ": Semi-final #" + str(home) + " winner V " + "Semi-final #" + str(away) + " winner")
        else:
            away = 1
            print("Final" + ": Semi-final #" + str(home) + " winner V " + "Semi-final #" + str(away) + " winner")
        print() # Make a new line
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
        print("Please choose a number between 1 to 3")
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