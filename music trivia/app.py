import random
import time
import json

def authenticate():
    while True:                                                                     #authentication process of the player
        player_name = str(input('Please enter your name: '))
        if player_name == 'MaskedTitan':
            password  = str(input('Please enter your password: '))
            if password == '1234':
                authenticated = True
                score = 0
                print('You have been authenticated, enjoy!')
                menu()
                break
        else:
            print('Authentication failed, please try again!')

with open('files/questions.json')as file:                                       #parsing file "questions.txt"
    data = json.load(file)
    file.close()                                                                #file is no longer needed as data is parsed

def view_leaderboard():
    with open('files/leaderboard.json', 'r')as file_leaderboard:                # opens leaderboard file
        leaderboard = json.load(file_leaderboard)
        file_leaderboard.close()
        print("\nLEADERBOARD")
        print("\n1.) Name: "+str(leaderboard["first"]["Name"])+" Score: "+str(leaderboard["first"]["score"]))
        print("\n2.) Name: "+str(leaderboard["second"]["Name"])+" Score: "+str(leaderboard["second"]["score"]))
        print("\n3.) Name: "+str(leaderboard["third"]["Name"])+" Score: "+str(leaderboard["third"]["score"]))
        print("\n4.) Name: "+str(leaderboard["fourth"]["Name"])+" Score: "+str(leaderboard["fourth"]["score"]))
        print("\n5.) Name: "+str(leaderboard["fifth"]["Name"])+" Score: "+str(leaderboard["fifth"]["score"])+"\n")

def end_game(score):
    print("You have scored ", str(score), " points in this round!")             # outputs player's score of this round
    with open('files/leaderboard.json', 'r')as file_leaderboard:                # opens leaderboard file
        leaderboard = json.load(file_leaderboard)
        file_leaderboard.close()
        if int(leaderboard["fifth"]["score"]) < int(score):                     #checks the user's score againt the top players
            if int(leaderboard["fourth"]["score"]) < int(score):
                if int(leaderboard["third"]["score"]) < int(score):
                    if int(leaderboard["second"]["score"]) < int(score):
                        if int(leaderboard["first"]["score"]) < int(score):
                            print("You have gotten rank 1 in the leaderboard")  #if the player's points are bigger than one of the leaderboadrs it then
                            leaderboard["fifth"]["Name"] = leaderboard["fourth"]["Name"]
                            leaderboard["fifth"]["Score"] = leaderboard["fourth"]["score"]
                            leaderboard["fourth"]["Name"] = leaderboard["third"]["Name"]
                            leaderboard["fourth"]["Score"] = leaderboard["third"]["score"]
                            leaderboard["third"]["Name"] = leaderboard["second"]["Name"]
                            leaderboard["third"]["score"] = leaderboard["second"]["score"]
                            leaderboard["second"]["Name"] = leaderboard["first"]["Name"]
                            leaderboard["second"]["score"] = leaderboard["first"]["score"]
                            leaderboard["first"]["Name"] = player_name                  #announces the rank the player has gaines and then saves the leaderboard file
                            leaderboard["first"]["score"] = int(score)
                        else:
                            print("You have gotten rank 2 in the leaderboard")
                            leaderboard["fifth"]["Name"] = leaderboard["fourth"]["Name"]
                            leaderboard["fifth"]["Score"] = leaderboard["fourth"]["score"]
                            leaderboard["fourth"]["Name"] = leaderboard["third"]["Name"]
                            leaderboard["fourth"]["Score"] = leaderboard["third"]["score"]
                            leaderboard["third"]["Name"] = leaderboard["second"]["Name"]
                            leaderboard["third"]["score"] = leaderboard["second"]["score"]
                            leaderboard["second"]["Name"] = player_name
                            leaderboard["second"]["score"]  =int(score)
                    else:
                        print("You have gotten rank 3 in the leaderboard")
                        leaderboard["fifth"]["Name"] = leaderboard["fourth"]["Name"]
                        leaderboard["fifth"]["Score"] = leaderboard["fourth"]["score"]
                        leaderboard["fourth"]["Name"] = leaderboard["third"]["Name"]
                        leaderboard["fourth"]["Score"] = leaderboard["third"]["score"]
                        leaderboard["third"]["Name"] = player_name
                        leaderboard["third"]["score"] = int(score)
                else:
                    print("You have gotten rank 4 in the leaderboard")
                    leaderboard["fifth"]["Name"] = leaderboard["fourth"]["Name"]
                    leaderboard["fifth"]["Score"] = leaderboard["fourth"]["score"]
                    leaderboard["fourth"]["Name"] = player_name
                    leaderboard["fourth"]["score"] = int(score)
            else:
                print("You have gotten rank 5 in the leaderboard")
                leaderboard["fifth"]["Name"] = player_name
                leaderboard["fifth"]["score"] = int(score)
        else:
            print("you have not made it to the top 5 of the leaderboard!")
        with open('files/leaderboard.json', 'w')as file_leaderboard:            #reopens leaderboard in write mode
            json.dump(leaderboard, file_leaderboard)                            #writes new leaderboard data onto file
            file_leaderboard.close()                                            #closes instance of open leaderboard file

def start_game():
    input('Press enter to continue')                                                #when the user is ready he can then start the game by pressing enter
    print('The game is starting...')

    while True:                                                                     #starting the game loop
            question_data = random.choice(data)                                     #pulls choice data from parsed file in the program
            words = question_data["Name"].split()                                   #splits the name up so it can take its initals
            letters = [word[0] for word in words]                                   #adds the initials to a list
            print("guess the song:\nhints:Artist is \n", question_data["Artist"],
            "\nThe Words in the name of the song start as:")                        #outputs the question
            for x in range(len(letters)):
                print(letters[x])                                                   #gives hints
            guess = str(input("Guess the name of the song: "))                      #takes input form user
            if guess == question_data["Name"]:                                      #checks if it is correct the first time
                score = score+2                                                     #if so then it adds 2 more points onto the players score
            else:
                print("Wrong, try again!")
                guess = str(input("Guess the name of the song: "))                  #gives the user another chance
                if guess == question_data["Name"]:
                    print("You have guessed correctly!")
                    score = score+1                                                 #if guessed correctly on second change it gives the user 1 point
                else:
                    print("You have guessed wrong on both attempts, game over!")    #if user fails both attempts then the game is over
                    end_game(int(score))                                            #parses the user's score into the end_game function
                    break                                                           #breaks the loop
def menu():
    while True:
        print("1. Play music trivia\n2. view leaderboard\n3. Quit")
        option = str(input("Enter option number : "))
        if option == "1":
            start_game()
        if option == "2":
            view_leaderboard()
        if option == "3":
            print("Thank you for playing\nCome again!")
            exit(1)
        if option not in ["1", "2", "3"]:
            print("option not understood please try again!")


authenticate()
