
import random

places = [i for i in range(0, 100)]
last, n = 0, 10000

for i in range(n):
    random.shuffle(places)
    occupied = [random.randint(0, 99)]
    for j in range(1, 100):
        last = last + 1 if j == 99 and places[j] not in occupied else last
        if places[j] in occupied:
            x = random.choice(places)
            while x in occupied:
                x = random.choice(places)
            occupied.append(x)
        else:
            occupied.append(places[j])

print(last/n)
