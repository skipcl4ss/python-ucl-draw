# python-ucl-draw
### A simulation of the UEFA Champions League Round of 16 draw using python

This program asks the user for the winner of the UCL group followed directly by its nationality, then asks for the runner of the same group followed directly by its nationality.
This is repeated for every group respectively.
Since the eight groups are named from A to H, the winners are of the 1st place, and the runners are of the second place, then the input will be as follows:
***A1 A1N A2 A2N B1 B1N B2 B2N C1 ...***
#### **Note that the inputs are separated by spaces**
Which means that names such as Manchester United must be written as **Manchester-United** or **MU** for example.

## How the draw works
Each winner is paired with a runner, where the following rules should apply:
* The two teams should be of different nationality
* The two teams should be of different groups
The draw is performed by getting a pot of the runners and randomly choosing a runner form the pot.
Then a pot of the eligible winners that specific runner is made and winner is chosen also randomly.
If a runner in the pot has only one eligible winner, they are paired immediately.
###### **The winner is written last in the pair as they host the 2nd leg at home**

## How the program works
We take inputs from user using input function, for multiple inputs we use the split function.
Then we make a dictionary of winners, where the names are keys and the nations as values, we do the same for runners.
We then make two list of **items** of the two dictionaries respectively, we also make another two lists of **keys**, where there is a list for winners and another for runners.
Then we copy the the two lists of items into an editable list of winners and a pot of runners, where both will  decrease with every pairing.