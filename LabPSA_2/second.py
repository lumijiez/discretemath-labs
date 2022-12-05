import random

counter = 0
for _ in range(100000):
    b1 = random.uniform(0, 1)
    b2 = random.uniform(0, 1)
    if b2 > b1:
        part1 = b1
        part2 = b2 - b1
        part3 = 1 - b2
    else:
        part1 = b2
        part2 = b1 - b2
        part3 = 1 - b1
    if part1+part2 > part3 and part1+part3 > part2 and part2+part3 > part1:
        counter+=1
print(counter/100000)
