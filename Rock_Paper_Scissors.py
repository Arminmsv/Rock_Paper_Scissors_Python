print("Type 'Exit' to quit the game anytime.")
import random
choices = ["Rock" , "Paper" , "Scissor"]
win = ""
while True :
    computer = random.choice(choices)
    user = input("Rock , Paper , Scissor: ").strip().capitalize()

    if user == "Exit":
        break

    if user not in choices:
        print("Invalid choice!")
    else:

        if user == "Rock" and computer == "Scissor":
            win = "Congratulations, you won!"

        elif user == "Paper" and computer == "Rock":
            win = "Congratulations, you won!"

        elif user == "Scissor" and computer == "Paper":
            win = "Congratulations, you won!"

        elif user == computer:
            win = "Equal!"

        else:
            win = "You lost, try again!"

        print("Computer: " , computer)
        print(win) 