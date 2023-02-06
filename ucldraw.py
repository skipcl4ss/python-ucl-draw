import random

print("Which draw would you like to simulate?")
while True:
    # Save the type of draw in a variable
    draw = input("1) Group stage\n2) Round of 16\n3) Finals (Quarter-finals and beyond)\n")
    # Code for group stage draw
    # TODO: complete the case
    if draw == '1':
        PotOne1, PotOne1N = input("Pot 1 teams & nations:\n").split(sep = " - ")
        PotOne2, PotOne2N = input().split(sep = " - ")
        PotOne3, PotOne3N = input().split(sep = " - ")
        PotOne4, PotOne4N = input().split(sep = " - ")
        PotOne5, PotOne5N = input().split(sep = " - ")
        PotOne6, PotOne6N = input().split(sep = " - ")
        PotOne7, PotOne7N = input().split(sep = " - ")
        PotOne8, PotOne8N = input().split(sep = " - ")
        PotTwo1, PotTwo1N = input("Pot 2 teams & nations:\n").split(sep = " - ")
        PotTwo2, PotTwo2N = input().split(sep = " - ")
        PotTwo3, PotTwo3N = input().split(sep = " - ")
        PotTwo4, PotTwo4N = input().split(sep = " - ")
        PotTwo5, PotTwo5N = input().split(sep = " - ")
        PotTwo6, PotTwo6N = input().split(sep = " - ")
        PotTwo7, PotTwo7N = input().split(sep = " - ")
        PotTwo8, PotTwo8N = input().split(sep = " - ")
        PotThree1, PotThree1N = input("Pot 3 teams & nations:\n").split(sep = " - ")
        PotThree2, PotThree2N = input().split(sep = " - ")
        PotThree3, PotThree3N = input().split(sep = " - ")
        PotThree4, PotThree4N = input().split(sep = " - ")
        PotThree5, PotThree5N = input().split(sep = " - ")
        PotThree6, PotThree6N = input().split(sep = " - ")
        PotThree7, PotThree7N = input().split(sep = " - ")
        PotThree8, PotThree8N = input().split(sep = " - ")
        PotFour1, PotFour1N = input("Pot 4 teams & nations:\n").split(sep = " - ")
        PotFour2, PotFour2N = input().split(sep = " - ")
        PotFour3, PotFour3N = input().split(sep = " - ")
        PotFour4, PotFour4N = input().split(sep = " - ")
        PotFour5, PotFour5N = input().split(sep = " - ")
        PotFour6, PotFour6N = input().split(sep = " - ")
        PotFour7, PotFour7N = input().split(sep = " - ")
        PotFour8, PotFour8N = input().split(sep = " - ")

        PotOne = {PotOne1: PotOne1N, PotOne2: PotOne2N, PotOne3: PotOne3N, PotOne4: PotOne4N, PotOne5: PotOne5N, PotOne6: PotOne6N, PotOne7: PotOne7N, PotOne8: PotOne8N}
        PotTwo = {PotTwo1: PotTwo1N, PotTwo2: PotTwo2N, PotTwo3: PotTwo3N, PotTwo4: PotTwo4N, PotTwo5: PotTwo5N, PotTwo6: PotTwo6N, PotTwo7: PotTwo7N, PotTwo8: PotTwo8N}
        PotThree = {PotThree1: PotThree1N, PotThree2: PotThree2N, PotThree3: PotThree3N, PotThree4: PotThree4N, PotThree5: PotThree5N, PotThree6: PotThree6N, PotThree7: PotThree7N, PotThree8: PotThree8N}
        PotFour = {PotFour1: PotFour1N, PotFour2: PotFour2N, PotFour3: PotFour3N, PotFour4: PotFour4N, PotFour5: PotFour5N, PotFour6: PotFour6N, PotFour7: PotFour7N, PotFour8: PotFour8N}

        groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        redGroups = groups[: 4]
        blueGroups = groups[4: ]

        name = 0
        nation = 1

        def firstEmptyGroup(grps):
            for group in grps:
                if len(group) == 1:
                    return group
        # TODO: there is a case where we may find that the red groups were filled, and we are left with two teams of the same nation in the blue teams
        # ! Cannot count the values of a dictionary
        def pairsCount(pot):
            testedNations = []
            for i in list(pot.values()):
                if testedNations.count(i) == 0:
                    print(list(pot.values()).count(i), i)
                    testedNations.append(i)

        def addToGroup(team):
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

        while len(PotOne) > 0:
            team = random.choice(list(PotOne.items()))
            print(team)
            addToGroup(team)
            print(groups)
            PotOne.pop(team[name])
            print(PotOne)

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
        # Input must be separated as follows: Team Name - Nation
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
        # Lists for group winners and runner ups, with nested lists of names and nations of each team
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
        # Input must be separated as follows: Team Name
        # Make a list of the teams, this list will decrease with each pairing
        teamPot = [input("Team 1, Team 2, etc:\n"), input(), input(), input(), input(), input(), input(), input()]
        # Choose randomly two pairs from the list, print the match with proper spacing and remove the teams from the teamPot list
        # This time, there are no rules. This is a completely random draw
        # This is why team nation is not necessary
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