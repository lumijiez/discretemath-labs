
import random

participants, n, days = list(), 10, 10000


def random_list():
    l = list()
    while len(l) < n:
        x = random.randint(1,n)
        if x not in l:
            l.append(x)
    return l


for i in range(n):
    participants.append(i)

ans = 0
for i in range(days):
    lunch, dinner = random_list(), random_list()
    # print(dinner)
    # print(lunch)
    for j in range(1, n+1):
        idx1 = lunch.index(j)
        # print(idx1)
        idx2 = dinner.index(j)
        q = [lunch[idx1-1], lunch[(idx1+1) % n]]
        w = [dinner[idx2-1], dinner[(idx2+1) % n]]
        # print(w)
        # print(q)
        if q[0] in w or q[1] in w:
            ans += 1
            break
print(1 - ans/days)
