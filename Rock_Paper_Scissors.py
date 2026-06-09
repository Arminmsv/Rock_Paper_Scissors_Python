import random
print("Type 'Exit' to quit the game anytime.")
choices = ["Rock" , "Paper" , "Scissor"]
win = ""
you_win = 0
losses = 0
draws = 0
point = 0
while True :
    computer = random.choice(choices)
    user = input("Rock , Paper , Scissor: ").strip().capitalize()

    if user == "Exit":
        print("Wins: " , you_win)
        print("Draws: " , draws)
        print("losses: " , losses)
        print("your point: " , point)
        break

    if user not in choices:
        print("Invalid choice!")
    else:

        if user == "Rock" and computer == "Scissor":
            win = "Congratulations, you won!"
            you_win += 1
            point += 3

        elif user == "Paper" and computer == "Rock":
            win = "Congratulations, you won!"
            you_win += 1
            point += 3

        elif user == "Scissor" and computer == "Paper":
            win = "Congratulations, you won!"
            you_win += 1
            point += 3

        elif user == computer:
            win = "Equal!"
            draws += 1
            point += 1

        else:
            win = "You lost, try again!"
            losses += 1

        print("Computer: " , computer)
        print(win) 