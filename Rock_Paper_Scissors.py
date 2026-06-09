import random
print("Type 'Exit' to quit the game anytime.")
choices = ["Rock" , "Paper" , "Scissor"]
win = ""
wins = 0
losses = 0
draws = 0
points = 0
name = input("What's your name: ")
while True :
    computer = random.choice(choices)
    user = input("Rock , Paper , Scissor: ").strip().capitalize()

    if user == "Exit":
        print(" Game Statistics")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Draws:", draws)
        print(f"{name}, you got {points} points in total!")
        print(f"Thanks {name} for playing my game!")
        break

    if user not in choices:
        print("Invalid choice!")
    else:

        if user == "Rock" and computer == "Scissor":
            win = "Congratulations, you won!"
            wins += 1
            points += 3

        elif user == "Paper" and computer == "Rock":
            win = "Congratulations, you won!"
            wins += 1
            points += 3

        elif user == "Scissor" and computer == "Paper":
            win = "Congratulations, you won!"
            wins += 1
            points += 3

        elif user == computer:
            win = "Equal!"
            draws += 1
            points += 1

        else:
            win = "You lost, try again!"
            losses += 1

        print("Computer: " , computer)
        print(win) 