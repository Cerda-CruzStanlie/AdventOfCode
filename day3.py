# Advent Of Code
# Author: Stanlie Cerda-Cruz

with open('day3.in') as file:
    data = [x for x in file.read().strip().split('\n')]

firstBank = []
secondBank = []

for x in data:
    firstBank.append(x[0:12])
    secondBank.append(x[12:24])

print(firstBank)
print(secondBank)