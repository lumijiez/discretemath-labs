from numpy import ceil
def checkLength(psw):
    if 20 >= len(psw) >= 8:
        return 0
    elif len(psw) > 20:
        return len(psw) - 20
    return 8 - len(psw)


def checkRepeating(psw):
    steps = 0
    tempSteps = 1
    while len(psw) > 0:
        x = psw[0]
        if len(psw) > 1:
            psw = psw[1:]
        elif len(psw) == 1:
            break
        if psw[0] == x:
            tempSteps += 1
            if tempSteps > 2:
                steps += 1
        else:
            tempSteps = 1
            psw = psw[1:]
    return steps


def checkComposition(psw):
    values = [0, 0, 0, 0]
    for x in psw:
        if x.islower():
            values[0] = 1
        if x.isnumeric():
            values[1] = 1
        if x.isupper():
            values[2] = 1
        if x in ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\'', '|', '}', '{', '~',
                 ':', '-']:
            values[3] = 1
    return values.count(0)


def checkPassword(psw):
    extraSteps = 0
    a = checkComposition(psw)
    b = checkLength(psw)
    c = checkRepeating(psw)
    if len(psw) < 8:
        return 8 - len(psw)
    if c > 20:
        extraSteps += c - 20
    if a == 0 and b == 0 and c == 0:
        return "good"
    if a == 0 and b == 0:
        return c
    else:
        return max(a, int(ceil((c+extraSteps+b)/3)))
    return "good"

passw = "aaaaaaaaaaaaaaaaaaaaaa"
print(checkPassword(passw))
print(checkLength(passw))
print(checkRepeating(passw))
print(checkComposition(passw))
