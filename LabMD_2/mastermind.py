
import random

num = random.randrange(1000, 10000)
n = int(input("Guess the number: XXXX"))
if (n == num):
	print("You won! You're a Mastermind!")
else:
	ctr = 0
	while (n != num):
		ctr += 1
		count = 0
		n = str(n)
		num = str(num)
		correct = ['X']*4
		for i in range(0, 4):
			if (n[i] == num[i]):
				count += 1
				correct[i] = n[i]
			else:
				continue
		if (count < 4) and (count != 0):
			print("Not really. But you guessed ",
				count, " digit(s) correct!")
			print("These digits are correct: ")
			for k in correct:
				print(k, end=' ')
			print('\n')
			print('\n')
			n = int(input("Enter next numbers: "))
		elif (count == 0):
			print("All digits are wrong.")
			n = int(input("Enter next numbers: "))
	if n == num:
		print("You became a Mastermind!")
		print("It took ", ctr, "tries.")
