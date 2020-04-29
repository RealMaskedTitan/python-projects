import random

def verify_p1():
    while True:
        p1 = str(input("Please enter player one username: "))
        if p1 == 'Mustaeen':
            p1_psswd = str(input('Please enter player one password: '))
            if p1_psswd == '1234':
                print('Authentication successful, enjoy your session!')
                p1_score = 0
                break
            else:
                print('Authentication failed!')
        else:
            print('Authentication failed!')

def verify_p2():
    while True:
        p2 = str(input("Please enter player two username: "))
        if p2 == 'Mai Sakurijima':
            p2_psswd = str(input('Please enter player two password: '))
            if p2_psswd == '1234':
                print('Authentication successful, enjoy your session!')
                p2_score = 0
                break
            else:
                print('Authentication failed!')
        else:
            print('Authentication failed!')

times_executed = 0

def game():
    print('starting player one game!')
    input('Press enter to begin!')
    p1_score = 0
    while times_executed >= 5:
        times_executed = times_executed + 1
        roll1 = random.randint(0, 6)
        print("You have rolled: ", roll1)
        roll2 = random.randint(0, 6)
        print("You have rolled: ", roll1)
        p1_score = roll1 + roll2 + p1_score
        if ((roll1 + roll2) % 2) == 0:
            print("You have rolled an even number, you will be awarded with 10 points!")
            p1_score  = p1_score + 10
        else:
            print("You have rolled an odd number, you will have 5 points deducted!")
            if p1_score > 5:
                p1_score  = p1_score - 5
            else:
                p1_score = 0

    print('starting player two game!')
    times_executed = 0
    input('Press enter to begin!')
    p2_score = 0
    while times_executed >= 5:
        roll1 = random.randint(0, 6)
        print("You have rolled: ", roll1)
        roll2 = random.randint(0, 6)
        print("You have rolled: ", roll1)
        p2_score = p2_score + roll1 + roll2
        if ((roll1 + roll2) % 2) == 0:
            print("You have rolled an even number, you will be awarded with 10 points!")
            p2_score  = p2_score + 10
        else:
            print("You have rolled an odd number, you will have 5 points deducted!")
            if p2_score > 5:
                p2_score  = p2_score - 5
            else:
                p2_score = 0

    if p1_score > p2_score:
        print("Player one  has won!")
    if p1_score < p2_score:
        print("Player two has won!")
    else:
        print("There has been a draw!")
        input("Player one press enter to roll!")
        p1_roll = random.randint(1, 6)
        p1_score = p1_score + p1_roll
        print("Player one your final score is: ", p1_score)
        input("Player two press enter to roll!")
        p2_roll = random.randint(1, 6)
        p2_score = p1_score + p2_roll
        print("Player two your final score is: ", p2_score)

verify_p1()
verify_p2()
game()
