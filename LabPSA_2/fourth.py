import random
from numpy import pi, cos, sin, sqrt


def distance(pointa, pointb):
    return sqrt((pointa[0] - pointb[0]) ** 2 + (pointa[1] - pointb[1]) ** 2)


def create_point():
    angle = random.uniform(0, 2*pi)
    x = cos(angle)
    y = sin(angle)
    return x, y


def check_acute(a, b, c):
    if a**2 + b**2 > c ** 2:
        return True
    else:
        return False


counter = 0
for _ in range(100000):
    x1, x2, x3 = create_point(), create_point(), create_point()
    l = [distance(x1, x2), distance(x1, x3), distance(x2, x3)]
    l.sort()
    if check_acute(l[0], l[1], l[2]):
        counter+=1
print(counter/100000)
