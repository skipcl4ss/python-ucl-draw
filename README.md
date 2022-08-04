# python-ucl-draw
#### A simulation of the UEFA Champions League different stages' draws using python

This program can simulate the draws of three stages in the Champions League:
* Group stage ***-not finished yet-***.
* Round of 16.
* Finals **(Quarter finals and beyond)**.

It also asks the user whether they want to repeat the process by hitting the letter c, or quit the program using the letter q.

## Packages used
### random
It is the only package needed, it is needed for two methods:
#### random.choice(list)
Chooses an item from the list randomly.
#### random.randrange(start, end, [step])
Makes a list of numbers from the start to right before the end, with the step taken into consideration. Then chooses a number from the list randomly.

## Group Stage Draw
### How the draw works
#### **Rules**
#### **Pairing Process**


### How the program works
#### **Input**
#### **Pairing Process**

## Round of 16 Draw
### How the draw works
#### **Rules**
Each two teams are paired together, where the following rules should apply:
* The first team which will play the first leg at home must be a group runner ***(unseeded team)***.
* The second team which will play the second leg at home must be a group winner ***(seeded team)***.
* The two teams should be of different nations ***(country protection rule)***.
* The two teams should be of different groups ***(group protection rule)***.
#### **Pairing Process**
The draw is performed by getting a pot of the runners and randomly choosing a runner form the pot.
Then a pot of the eligible winners that specific runner is made and winner is chosen also randomly.
If a runner in the *pot* has only one eligible winner, they are paired immediately.

*The max number of teams from the same nation is five.*

**The winner is written last in the pair as they host the second leg at home.**

### How the program works
#### **Input**
The program asks the user for the winner of the UCL group followed directly by its nation, then asks for the runner of the same group followed directly by its nation.
This is repeated for every group respectively.
Since the eight groups are named from A to H, the winners are of the 1st place, and the runners are of the second place, then the input will be as follows:
```
A1 - A1N
A2 - A2N
B1 - B1N
B2 - B2N
...
```
**Note that teams and nations are separated by hyphens and spaces " - ", while team and nation pairs are separated by newlines**
Which means that a pair such as Manchester United of England must be written as **Manchester United - England** or **MU - ENG** for example.
While two pairs such as Real Madrid of Spain and Inter Milan of Italy must be written as<br>**Real Madrid - Spain<br>Inter Milan - Italy**<br>or<br>**RMA - SPA<br>IM - ITA**<br>for example.

We take inputs from user using input function, for multiple inputs we use the split method, with **sep** argument of value " - ".
Then we make a list of winners, with nested lists of names and nations of each team, we do the same for runners.
Then we copy the two lists of items into editable lists of winners and runners called pots, where both will  decrease with every pairing.
#### **eligibleWinners(runner)**
A function for making a list of eligible opponents for a certain runner from the ***winnersPot*** list,and append them in a pot of eligible winners, called ***eligibleWinnersPot***.
As mentioned above, each eligible opponent must be:
    * A winner team ***(seeded teams V unseeded teams rule)***.
    * Of a different nation from the runner ***(country protection rule)***.
    * From a different group from the runner ***(group protection rule)***.

    Parameters:
        runner (list): A list of of two elements, the first being the name of the runner, the second being its nation. Represents the runner in question.

    Returns:
        eligibleWinnersPot (list): a list of lists, each nested list contains two elements, winner name and nation.
#### **Special Case**
Since that the max number of teams from the same nation is five, there is a special case where there are six winners, a runner team would find that four of the six winners are of the same of that runner's nation, and the fifth winner is of the same group oof the runner, then the sixth winner is paired automatically with that runner.
This can also happen with less than six winners, eg. five winners with four of them of the same nation of the spicific runner, or three of the same nation and one of the same group of the runner.
#### **Pairing Process**
If the special case happens, pair the two teams, remove them from their respective pots and repeat the pairing process.
If the special case does not happen, we choose the runner randomly, make a list of the eligible winners and choose a winner from that list, pair the two teams, remove them from their respective pots and repeat the pairing process.
The process ends when the runners Pot is empty.

**A counter called *match* is used in the process, to give each match done a proper number.**

## Finals Draw
### How the draw works
#### **Rules**
This draw is totally random, no seeding, no country protection, no special rules.
Semi-finals and final draws are made in advance with the quarter-finals draw, which means the teams will be anonymous.
In the semi-finals draw the teams are named as the winners of the numbered quarter-finals matches, where the first team to be drawn in a pair will have the first leg at home.
The same will happen for the final draw, while the difference is that the final will be a single match in a predetermined neutral venue.

**The final draw is done for *operational reasons*.**
#### **Pairing Process**
All the teams are put in one pot, every two consecutive chosen teams pair a match.
### How the program works
#### **Input**
Since there is no country protection, the user is not asked for the teams countries, as they are not needed.
The program asks for eight teams, each separated by a newline, where the input will be as follows:
```
T1
T2
T3
T4
...
```
#### **Pairing Process**
**A counter called *match* is used in the process, to give each match done a proper number.**

*The team written first in a pair will have the first leg played at home, except in the final match, where they will have the **home** title only. This is, as mentioned above, for operational reasons*

##### ***Quarter-finals-draw***
All the inputs are saved in a list called **teamPot**, where each two teams are paired, have their match printed with the proper number, and are removed from the list.

##### ***Semi-finals-draw***
Since the teams are anonymous, we use the number of quarter-final matches winners to make the draw.
Therefore, we make a list of the number of quarter-final matches, which is 4, then we choose two numbers randomly to pair them and print the match with a proper number for that semi-final match.

##### ***Final draw***
Again, the teams are anonymous, and this time we use the number of semi-final matches winners instead to make the draw.
Since this time there are two semi-final matches, the program chooses a random number from 1 and 2.
If the chosen number is 1, print the match with the semi-final match #1 winner is at home. If else, print it with the semi-final match #2 winner is at home this time.