import random

square = [[]]

for row in range(12):
    c = []
    while c in square:
        for column in range(12):
            x = 0
            while x in c:
                x = random.randint(1, 12)
            c.append(x)
    square.append(c)

print(square[1::])
