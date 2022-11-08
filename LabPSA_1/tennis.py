import random

ann_won = 0
for _ in range(10000):
    pointsAnn = 0
    pointsDan = 0
    ann_going = random.randint(0,1)
    while(pointsDan <= 25 and pointsAnn <= 25):
        while ann_going:
            x = random.uniform(0, 1)
            if x > 0.3:
                pointsAnn += 1
            else:
                ann_going = 0
                pointsDan += 1
        while not ann_going:
            x = random.uniform(0, 1)
            if x > 0.5:
                pointsDan += 1
            else:
                ann_going = 1
                pointsAnn += 1
    if pointsAnn > pointsDan:
        ann_won += 1
print(ann_won/10000)
