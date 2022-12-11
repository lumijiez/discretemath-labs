
import random
import matplotlib.pyplot as plt

tries = 1000
number_of_n = {x: 0 for x in range(35, 65)}

for x in range(tries):
	heads = 0
	for z in range(100):
		if random.randint(0, 1) == 1:
			heads += 1
	if heads in number_of_n:
		number_of_n[heads] += 1

x = list(number_of_n.keys())
y = list(number_of_n.values())

plt.bar(x, y, color ='maroon', width = 0.4)
plt.show()
