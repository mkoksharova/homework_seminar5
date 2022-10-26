import random
import json
candy = ["candy"] * 2021
user_took = []
computer_took = []

def user_step(candy, user_took):
	print("Возьмите конфеты от 1 до 28: ")
	motion = int(input("Сколько конфет возьмете?"))
	for i in range(motion):
		user_took.append(candy[i])
		candy.pop(i)
	return len(candy), user_took
		
def computer_step(candy, computer_took):
	if len(candy) > 56:
		motion = 28
	elif len(candy) < 56:
		motion = len(candy) - 28
	elif len(candy) < 28:
		motion = len(candy)
		
	for i in range(motion):
		computer_took.append(candy[i])
		candy.pop(i)
	return len(candy), computer_took
		
def toss():
	input("жеребьевка: ")
	toss_user = random.randint(1, 6)
	toss_computer = random.randint(1,6)
	if toss_user < toss_computer:
		return True
	else:
		return False

def game(candy, user_took, computer_took):
	if False:
		while len(candy) != 0:
			print(len(candy), len(user_took), len(computer_took))
			user_step(candy, user_took)
			computer_step(candy, computer_took)
	else:
		while len(candy) != 0:
			print(len(candy), len(user_took), len(computer_took))
			computer_step(candy, computer_took)
			user_step(candy, user_took)
game(candy, user_took, computer_took)