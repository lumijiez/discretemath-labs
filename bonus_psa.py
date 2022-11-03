import random 
from PIL import Image

img = Image.open("bonus.png").convert('RGB')
w, h, c = img.width, img.height, 0
for _ in range(100000):
    c = c + 1 if img.getpixel((random.randint(0, w - 1), random.randint(0, h - 1))) == (255, 0, 0) else c
print(c/100000 * 42)
