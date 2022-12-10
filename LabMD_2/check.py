def checkLength(passw):
    if 20 >= len(passw) >= 8:
        return 0
    elif len(passw) > 20:
        return len(passw) - 20
    return 8 - len(passw)


def checkRepeating(passw):
    steps = 0
    letters = {x: 0 for x in passw}
    for x in passw:
        letters[x] += 1
    for x in letters:
        if letters[x] > 2:
            steps += letters[x] - 2
    if steps == 0:
        return 0
    return steps


def checkComposition(passw):
    # lowercase, uppercase, numeric, special
    values = [0, 0, 0, 0]
    counter = 0
    for x in passw:
        if x.islower():
            values[0] = 1
        if x.isupper():
            values[1] = 1
        if x.isnumeric():
            values[2] = 1
        if x in ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\'', '|', '}', '{', '~',
                 ':', '-']:
            values[3] = 1
    for x in values:
        if x == 1:
            counter += 1
    return 4 - counter


def checkPassword(passw):
    x = max(checkLength(passw), checkComposition(passw), checkRepeating(passw))
    if x:
        return x
    return "good"


passw = input()
print(checkPassword(passw))
