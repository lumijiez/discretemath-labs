import random


def generateBullets(number, adjacent):
    bullets = [0 for _ in range(number)]
    no_bullet_pos = []
    if adjacent:
        bullet_pos = random.randint(0, number - 1)
        bullets[bullet_pos] = 1
        if bullet_pos + 1 == number:
            bullets[0] = 1
        else:
            bullets[bullet_pos + 1] = 1
    else:
        x = random.randint(0, number - 1)
        if x == number - 1:
            adj1, adj2 = 0, x - 1
        elif x == 0:
            adj1, adj2 = x + 1, number - 1
        else:
            adj1, adj2 = x + 1, x - 1
        y = random.randint(0, number - 1)
        while y == adj1 or y == adj2 or y == x:
            y = random.randint(0, number - 1)
        bullets[x], bullets[y] = 1, 1
    for x in range(len(bullets)):
        if bullets[x] == 0:
            no_bullet_pos.append(x)
    return bullets, no_bullet_pos


def getProb(slots, adjacent):
    alive_changed = 0
    alive_next = 0
    for _ in range(count):
        bullets, no_bullet_pos = generateBullets(slots, adjacent)
        current_revolver_pos = random.choice(no_bullet_pos)
        current_revolver_pos = 0 if current_revolver_pos + 1 == slots else current_revolver_pos + 1
        alive_next = alive_next + 1 if bullets[current_revolver_pos] == 0 else alive_next
        x = random.randint(0, slots - 1)
        alive_changed = alive_changed + 1 if bullets[x] == 0 else alive_changed
    return alive_next / (count / 100), alive_changed / (count / 100)


count = 100000
print("6 slot, adjacent, not spin: ", getProb(6, True)[0], "%")
print("6 slot, adjacent, spin: ", getProb(6, True)[1], "%")
print("6 slot, not adjacent, not spin: ", getProb(6, False)[0], "%")
print("6 slot, not adjacent, spin: ", getProb(6, False)[1], "%")
print("5 slot, adjacent, not spin: ", getProb(5, True)[0], "%")
print("5 slot, adjacent, spin: ", getProb(5, True)[1], "%")
print("5 slot, not adjacent, not spin: ", getProb(5, False)[0], "%")
print("5 slot, not adjacent, spin: ", getProb(5, False)[1], "%")
