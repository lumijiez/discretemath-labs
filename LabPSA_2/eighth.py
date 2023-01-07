import random


n, counter, tries = 10, 0, 100000
for _ in range(tries):
    lunch, l_p, dinner, d_p = random.sample(range(n), n), [], random.sample(range(n), n), []
    for x in range(n - 1):
        l_p.append({lunch[x], lunch[x + 1]})
        d_p.append({dinner[x], dinner[x + 1]})
    l_p.append({lunch[0], lunch[-1]})
    d_p.append({dinner[0], dinner[-1]})
    counter = counter + 1 if sum(el in l_p for el in d_p) > 0 else counter
print(1 - counter/tries)
