import random

ans, n = 0, 100000
for i in range(n):
    x, j = random.uniform(0, 1), 0
    while True:
        y = random.uniform(0, 1)
        if y > x:
            break
        j += 1
    ans += j
print(ans/n)
