# Advent Of Code: Author Stanlie Cerda-Cruz
# Code Inspiration: Jefffery Frederic

with open('day1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

# Traversing string in data
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

#Max Calories
print('The max calories are held by elve number ' + str(elves[elves.index(max(elves))-1]) + ', which is:\n' + str(max(elves)))

#Removes elve count then organizes
for item in elves:
    if item <= count:
        elves.remove(item)
elves.sort()
print('\nThe decending order of calories is:')
print(elves)

top3 = [0,0,0]
for item in elves:
    if item > top3[0] and top3[1] >= top3[0] and top3[2] >= top3[0]:
        top3[0] = item
        continue
    if item > top3[1] and top3[0] >= top3[1] and top3[2] >= top3[1]:
        top3[1] = item
        continue
    if item > top3[2] and top3[1] >= top3[2] and top3[0] >= top3[2]:
        top3[2] = item
        continue
print('\nThe top 3 amount of calories collected are:')
print(top3)

print('\nThe top 3 total amount of calories collected are:')
totalTop3=sum(top3)
print(totalTop3)