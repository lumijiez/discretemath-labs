def print_power_set(set, set_size):
    pow_set_size = 2
    for x in range(set_size-1):
        pow_set_size *= 2

    for counter in range(0, pow_set_size):
        sett = []
        for j in range(0, set_size):
            if counter & (1 << j):
                sett.append(set[j])
        print(sett)
        print()


elem = [1, 2, 3, 4, 5, 6]
print_power_set(elem, len(elem))
