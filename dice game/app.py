import random

while True:
	p1_usrname = input("Player One username : ")
	if p1_usrname == "MaskedTitan":
		p1_password = input("Player One password : ")
		if p1_password == "1234":
			print("Authentication successful!")
			break
		else:
			print("Authentication Error!\nTry Again!")
	else:
		print("Authentication Error!\nTry Again!")

while True:
	p2_usrname = input("Player Two username : ")
	if p2_usrname == "Mai Sakurijima":
		p2_password = input("Player Two password : ")
		if p2_password == "1234":
			print("Authentication successful!")
			break
		else:
			print("Authentication Error!\nTry Again!")
	else:
		print("Authentication Error!\nTry Again!")

def rounds():
	print("Round : " + str(Round))
	input("Player Two press enter to roll!")
	roll_one = random.randint(1, 6)
	print("Dice One : " + str(roll_one))
	roll_two = random.randint(1, 6)
	print("Dice Two : " + str(roll_two))
	total = roll_one + roll_two
	print("Total points this roll : " + str(total))
	if (total/2) is int:
		total = total +10
		print("You have gotten an even total!\nYou have gained 10 points")
	elif roll_one == roll_two:
		print("You have rolled a double!")
		roll_three = random.randint(1, 6)
		print("Third Dice : " + str(roll_three))
		total = total + roll_three
		print("Your new total is : ")
	else:
		total = total - 5
		print("You have gotten an odd total\nYou have lost 5 points!\nYour new total : " + str(total))
	return total



round_no = 0
player_One_Score = 0
while Round =< 5:
	if player_One_Score + rounds() <0:
		print("Your score is 0 and will not go down")
	else:
		player_One_Score = player_One_Score + rounds()
print("Player One your Score is : " + str(player_One_Score))

round_no = 0
player_Two_Score = 0
while Round =< 5:
	if player_Two_Score + rounds() <0:
		print("Your score is 0 and will not go down")
	else:
		player_Two_Score = player_One_Score + rounds()
print("Player Two your Score is : " + str(player_Two_Score))

def verdict(player_One_Score, player_Two_Score):
	if player_One_Score > player_Two_Score:
		print("Player One Won!")
		print("<Winner!> Player One score : " + str(player_One_Score))
		print("<Loser> player Two score : " + str(player_Two_score))
	elif player_One_Score < player_Two_Score:
		print("Player Two Won!")
		print("<Loser> Player One score : " + str(player_One_Score))
		print("<Winner!> player Two score : " + str(player_Two_score))
	else:
		print("There has been a tie!")
		player_1_roll = random.randint(1, 6)
		player_2_roll = random.randint(1, 6)
		verdict(player_1_roll, player_2_roll)
