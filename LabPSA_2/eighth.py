import random


def get_list(z):
    rand_lst, i = [], 0
    while len(rand_lst) < 10:
        z = random.randint(1, z)
        if z not in rand_lst:
            rand_lst.append(z)
    return rand_lst


n, counter, tries = 10, 0, 100000
for _ in range(tries):
    lunch, l_p, dinner, d_p = get_list(n), [], get_list(n), []
    for x in range(n - 1):
        l_p.append({lunch[x], lunch[x + 1]})
        d_p.append({dinner[x], dinner[x + 1]})
    l_p.append({lunch[0], lunch[-1]})
    d_p.append({dinner[0], dinner[-1]})
    counter = counter + 1 if sum(el in l_p for el in d_p) > 0 else counter
print(1 - counter/tries)
