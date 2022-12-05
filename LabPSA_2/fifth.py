import random
from numpy import sqrt

real = 0
positive = 0
for _ in range(10000):
    b = random.uniform(-1, 1)
    c = random.uniform(-1, 1)
    delta = b ** 2 - 4*c
    if delta > 0:
        real += 1
        x1 = (-b + sqrt(delta))/2
        x2 = (-b - sqrt(delta))/2
        if x1 > 0 and x2 > 0:
            positive += 1
print(real/10000)
print(positive/10000)


