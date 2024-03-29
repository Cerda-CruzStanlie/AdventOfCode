# Advent Of Code: Author Stanlie Cerda-Cruz


with open('day2.in') as file:
    data = [x for x in file.read().strip().split('\n')]


# ROCK = A
# PAPER = B
# SCISSORS = C


# LOSE = X
# DRAW = Y
# WIN = Z

# PAPER beats ROCK, ROCK beats SCISSORS, SCISSORS beats PAPER

# the points given to you depend on the choice you make, ROCK = 1
# PAPER = 2, SCISSORS = 3
choiceTally = 0

for line in data:
    if 'B X' in line:
        choiceTally = choiceTally + 1
    if 'A Y' in line:
        choiceTally = choiceTally + 1
    if 'C Z' in line:
        choiceTally = choiceTally + 1
    if 'C X' in line:
        choiceTally = choiceTally + 2
    if 'B Y' in line:
        choiceTally = choiceTally + 2
    if 'A Z' in line:
        choiceTally = choiceTally + 2
    if 'A X' in line:
        choiceTally = choiceTally + 3
    if 'C Y' in line:
        choiceTally = choiceTally + 3
    if 'B Z' in line:
        choiceTally = choiceTally + 3

# Winning give you 6 points, loosing gives you 0 points, and drawing gives you 3 points.
winTally = 0
for line in data:
    if "Y" in line:
        winTally = 3 + winTally
    if "Z" in line:
        winTally = 6 + winTally
    if "X" in line:    
        winTally = 0 + winTally

print(winTally + choiceTally)
