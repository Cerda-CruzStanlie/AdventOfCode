# Advent Of Code: Author Stanlie Cerda-Cruz
# Code Inspiration: Jefffery Frederic

with open('day1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# Traversing every STRING in our DATA
x = 0
i = 0
calories = 0
count = 0
elves = []
for item in data:
    x = x + 1
    if item == '':
        count = count + 1
        elves.append(count)
        elves.append(calories)
        calories = 0
    else:
        calories = calories + int(item)
    if len(data) == x:
        count = count + 1
        elves.append(count)
        elves.append(calories)

print(elves)

#Max Calories
max = max(elves)
print(max)

#Removes elve count then organizes
for item in elves:
    if item <= count:
        elves.remove(item)
elves.sort(*)
print(elves)

