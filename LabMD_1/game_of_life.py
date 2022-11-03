
import random
from PIL import Image
from PIL import ImageDraw


def getNextChild(o, t, r):
    if o == t == r == 1:
        return 0
    elif o == t == r == 0:
        return 0
    elif o == t == 1 and r == 0:
        return 1
    elif o == r == 1 and t == 0:
        return 1
    elif o == 1 and t == r == 0:
        return 0
    elif o == 0 and t == r == 1:
        return 1
    elif o == r == 0 and t == 1:
        return 1
    elif o == t == 0 and r == 1:
        return 1


def getNextGen(previousgen):
    nextgen = []
    for x in range(0, len(previousgen)):
        if x == 0:
            nextgen.append(getNextChild(0, previousgen[x], previousgen[x + 1]))
        elif x == len(previousgen) - 1:
            nextgen.append(getNextChild(previousgen[x - 1], previousgen[x], 0))
        elif 1 <= x < (len(previousgen) - 1):
            nextgen.append(getNextChild(previousgen[x - 1], previousgen[x], previousgen[x + 1]))
    return nextgen

m = 100
pixelSize = 5
# 110 rule
#currentGen = [0 for x in range(m-1)]
#currentGen.append(1)

# random rule
#currentGen = [random.randint(0, 1) for x in range(m)]

# 0101010101...
#currentGen = []
#for x in range(1, 500):
#    for g in range(2):
#        currentGen.append(g)

width = height = m*pixelSize
img = Image.new('RGB', (width, height), (128, 128, 128))
draw = ImageDraw.Draw(img)
for x in range(m):
    for g in range(len(currentGen)):
        if currentGen[g] == 1:
            draw.rectangle([(g*pixelSize, x*pixelSize), (width, height)], fill="#000000")
        else:
            draw.rectangle([(g*pixelSize, x*pixelSize), (width, height)], fill="#ffffff")
    print(currentGen)
    currentGen = getNextGen(currentGen)
img.show()
