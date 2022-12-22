file = open('day1.in')


i = 0
x = 0
with file:
    data = [file.read().strip().split('\n')]
print(x)
while len(data):
    if data[i] == '':
        x = x + 1
        i = i + 1
print(str(x))
