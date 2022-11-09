import random
import statistics

count = 100000
results = []
for _ in range(count):
    nr_success = 0
    x = 6
    while x > 5:
        nr_success += 1
        x = random.uniform(0, 10)
    if nr_success > 1:
        results.append(pow(2, nr_success))
results.sort()
print(statistics.mean(results))


