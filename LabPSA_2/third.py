import random

counter = 0
for _ in range(1000000):
    part1 = random.uniform(0, 1)
    part2 = 1 - part1
    if part2 > part1:
        part3 = random.uniform(0, part2)
        part2 -= part3
    else:
        part3 = random.uniform(0, part1)
        part1 -= part3
    if part1+part2 > part3 and part1+part3 > part2 and part2+part3 > part1:
        counter+=1
print(counter/1000000)

