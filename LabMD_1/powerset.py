def get_powerset(set, set_size):
    pow_set_size = 2
    for x in range(set_size-1):
        pow_set_size *= 2
    for counter in range(0, pow_set_size):
        sett = []
        for j in range(0, set_size):
            if counter & (1 << j):
                sett.append(set[j])
        g.append(sett)


g = []
elem = [1, 2, [1,2]]
get_powerset(elem, len(elem))
print(g)
