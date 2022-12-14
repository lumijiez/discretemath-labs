
import random

students, jora, offence = 0, 0, 0
for i in range(730):
    students += 6
    y, x = random.uniform(0, 1), random.uniform(0, 1)
    if y <= 0.02:
        jora += 6
    if x <= 0.05:
        if offence == 0:
            jora += 50
        if offence == 1:
            jora += 150
        if offence > 1:
            jora += 300
        offence += 1

print("expected cost jora:" + str(jora))
print("expected cost students:" + str(students))
