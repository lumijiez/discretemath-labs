
import random

estimation = (50*200)/8
print('estimated number of deer:' + str(estimation))
prob_deer, deer, n = 1/25, 0, 10000

for i in range(n):
    flag = 0
    while flag < 50:
        deer += 1
        if random.uniform(0, 1) <= prob_deer:
            flag += 1

print('number of deer by simulation:' + str(deer/n))
