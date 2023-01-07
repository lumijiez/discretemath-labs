def checkLength(psw):
    if 20 >= len(psw) >= 8:
        return 0
    elif len(psw) > 20:
        return len(psw) - 20
    return 8 - len(psw)


def checkRepeating(psw):
    steps = 0
    tempSteps = 1
    while len(psw) > 1:
        x = psw[0]
        if psw[1] == x:
            tempSteps += 1
            psw = psw[1:]
        else:
            steps = tempSteps - 2 + steps if tempSteps > 2 else steps
            tempSteps = 1
            psw = psw[1:]
    return steps


def checkComposition(psw):
    values = [0, 0, 0, 0]
    for x in psw:
        values[0] = 1 if x.islower() else values[0]
        values[1] = 1 if x.upper() else values[1]
        values[2] = 1 if x.isnumeric() else values[2]
        if x in ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '\'', '|', '}', '{', '~',
                 ':', '-']:
            values[3] = 1
    return values.count(0)


def checkPassword(psw):
    x = max(checkLength(psw), checkComposition(psw), checkRepeating(psw))
    if x:
        return x
    return "Good!"


passw = input()
print(checkPassword(passw))
