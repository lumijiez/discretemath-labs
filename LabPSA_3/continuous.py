import random
import numpy


def random_point():
    alpha = random.uniform(0, numpy.pi)
    r = random.uniform(0, 10)
    x, y = r*numpy.cos(alpha), r*numpy.sin(alpha)
    return [x, y, r]


def distance(a, b):
    return numpy.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


right_half, less_then_average, more_then_average, within_us = 0, 0, 0, 0
n = 10000
for i in range(n):
    point = random_point()
    if point[0] > 0:
        right_half += 1
    if point[2] < 5:
        less_then_average += 1
    else:
        more_then_average += 1
    if distance([point[0], point[1]], [0, 5]) < 5:
        within_us += 1

print('it lands in the right half of the target: ' + str(right_half/n))
print('its distance from the center is less than 5 inches: ' + str(less_then_average/n))
print('its distance from the center is greater than 5 inches: ' + str(more_then_average/n))
print('it lands within 5 inches of the point (0, 5): ' + str(within_us/n))


