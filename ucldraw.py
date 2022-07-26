import random
#input must be separated as follows: Team-Name Nationality
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
#dictionaries for group winners and runner ups, with names as keys and nationalities as values
winnerDict = {A1: A1N, B1: B1N, C1: C1N, D1: D1N, E1: E1N, F1: F1N, G1: G1N, H1: H1N}
runnerDict = {A2: A2N, B2: B2N, C2: C2N, D2: D2N, E2: E2N, F2: F2N, G2: G2N, H2: H2N}

print("group winners:" + "\n" + str(winnerDict))
print("group runners:" + "\n" + str(runnerDict))
#turning the dictionaries into lists for indexing while retaining both keys and values
#notice that I needed to alter list of runnerDict twice so I declared two variables
winnerList = list(winnerDict.items())
runnerList = list(runnerDict.items())
winnerListEditable = winnerList.copy()
runnerPot = runnerList.copy()
#turning the dictionaries into lists for indexing while retaining only the keys (team names)
winnerNames = list(winnerDict.keys())
runnerNames = list(runnerDict.keys())