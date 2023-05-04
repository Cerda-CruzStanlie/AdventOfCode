# Advent Of Code: Author Stanlie Cerda-Cruz


with open('day2.in') as file:
    data = [x for x in file.read().strip().split('\n')]


# ROCK = A and X
# PAPER = B and Y
# SCISSORS = C and Z

# PAPER beats ROCK, ROCK beats SCISSORS, SCISSORS beats PAPER

# the points given to you depend on the choice you make, ROCK = 1
# PAPER = 2, SCISSORS = 3
choiceTally = 0

for line in data:
    if 'X' in line:
        choiceTally = choiceTally + 1
    if 'Y' in line:
        choiceTally = choiceTally + 2
    if 'Z' in line:
        choiceTally = choiceTally + 3

# Winning give you 6 points, loosing gives you 0 points, and drawing gives you 3 points.
winTally = 0
for line in data:
    if "A X" in line:
        winTally = 3 + winTally
    if "A Y" in line:
        winTally = 6 + winTally
    if "A Z" in line:    
        winTally = 0 + winTally
    if "B X" in line:
        winTally = 0 + winTally
    if "B Y" in line:
        winTally = 3 + winTally
    if "B Z" in line:
        winTally = 6 + winTally
    if "C X" in line:
        winTally = 6 + winTally
    if "C Y" in line:
        winTally = 0 + winTally
    if "C Z" in line:
        winTally = 3 + winTally


print(winTally + choiceTally)
