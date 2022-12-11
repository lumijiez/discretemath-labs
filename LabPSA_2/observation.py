
import random
import matplotlib.pyplot as plt

def getRoll():
    l = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
    if l[0] + l[1] + l[2] == 9:
        return 1
    elif l[0] + l[1] + l[2] == 10:
        return 2

tries = 1000000
count10, count9 = 0, 0
xc, yc, y2c = [], [], []
for i in range(1, tries):
    x = getRoll()
    count9 = count9 + 1 if x == 1 else count9
    count10 = count10 + 1 if x == 2 else count10
    xc.append(i)
    yc.append(count9/i)
    y2c.append(count10/i)

plt.plot(xc, y2c, label="Sum of dices is 10")
plt.plot(xc, yc, label="Sum of dices is 9")
plt.legend()
plt.show()
