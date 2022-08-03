# python-ucl-draw
#### A simulation of the UEFA Champions League different stages' draws using python

This program can simulate the draws of three stages in the Champions League:
* Group stage ***-not finished yet-***
* Round of 16
* Finals **(Quarter finals and beyond)** ***-not finished yet-***

It also asks the user whether they want to repeat the process by hitting enter.

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
Each group winner is paired with a group runner, where the following rules should apply:
* The two teams should be of different nationality
* The two teams should be of different groups
#### **Pairing Process**
The draw is performed by getting a pot of the runners and randomly choosing a runner form the pot.
Then a pot of the eligible winners that specific runner is made and winner is chosen also randomly.
If a runner in the pot has only one eligible winner, they are paired immediately.

*The max number of teams from the same nation is five*
**The winner is written last in the pair as they host the 2nd leg at home**

### How the program works
#### **Input**
The program asks the user for the winner of the UCL group followed directly by its nationality, then asks for the runner of the same group followed directly by its nationality.
This is repeated for every group respectively.
Since the eight groups are named from A to H, the winners are of the 1st place, and the runners are of the second place, then the input will be as follows:
```
A1 - A1N
A2 - A2N
B1 - B1N
B2 - B2N
...
```
**Note that the inputs are separated by hypens and spaces " - "**
Which means that names such as Manchester United of England must be written as **Manchester United - England** or **MU - ENG** for example.
We take inputs from user using input function, for multiple inputs we use the split method, with sep argument of value " - ".
Then we make a list of winners, with nested lists of names and nations of each team, we do the same for runners.
Then we copy the two lists of items into editable lists of winners and runners called pots, where both will  decrease with every pairing.
#### **eligibleWinners(runner)**
A function for making a list of winners from ***winnerPot*** list, which are eligible for a certain runner and append them in a pot of eligible winners, taking the rules mentioned above into consideration.

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

## Finals Draw
### How the draw works
#### **Rules**
#### **Pairing Process**


### How the program works
#### **Input**
#### **Pairing Process**