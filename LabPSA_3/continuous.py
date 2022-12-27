import random
import numpy


def random_point():
    alpha = random.uniform(0, numpy.pi)
    r = random.uniform(0, 10)
    x, y = r*numpy.cos(alpha), r*numpy.sin(alpha)
    return [x, y, r]


def distance(a, b):
    return numpy.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


right_half, less_than_5, more_than_5, within_range = 0, 0, 0, 0
n = 10000
for i in range(n):
    point = random_point()
    if point[0] > 0:
        right_half += 1
    if point[2] < 5:
        less_than_5 += 1
    else:
        more_than_5 += 1
    if distance([point[0], point[1]], [0, 5]) < 5:
        within_range += 1

print('Right-half of target: ' + str(right_half / n))
print('Less than 5 inch from center: ' + str(less_than_5 / n))
print('More than 5 inches from center: ' + str(more_than_5 / n))
print('Within 5 inches from (0, 5): ' + str(within_range / n))

