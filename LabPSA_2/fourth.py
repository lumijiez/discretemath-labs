import random
from numpy import pi, cos, sin, sqrt

counter = 0
for _ in range(100000):
    (x1, y1) = (cos(random.uniform(0, 2*pi)), sin(random.uniform(0, 2*pi)))
    (x2, y2) = (cos(random.uniform(0, 2 * pi)), sin(random.uniform(0, 2 * pi)))
    (x3, y3) = (cos(random.uniform(0, 2 * pi)), sin(random.uniform(0, 2 * pi)))
    len1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    len2 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    len3 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    list1 = [len1, len2, len3]
    list1.sort()
    if list1[0] ** 2 + list1[1] ** 2 > list1[2] ** 2:
        counter+=1
print(counter/100000)

