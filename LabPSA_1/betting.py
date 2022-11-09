import random
import statistics

results = []
for _ in range(100000):
    nr_success, x = 0, 1
    while x == 1:
        nr_success += 1
        x = random.randint(0, 1)
        results.append(pow(2, nr_success))
print(statistics.mean(results))

