
import random

tries, wins = 1000000, 0
for _ in range(tries):
    if 375 <= random.randint(0, 1499) <= 1124 and 375 <= random.randint(0, 1499) <= 1124:
        wins += 1
print(wins/tries)
