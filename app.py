import random

#Bot
weapons = ["Scissors", "Paper", "Rock"]


#Game
while True:
    botChoice = random.choice(weapons)
    choice = input("\nPick your weapon (Scissors, Paper or Rock). You can quit game but typing quit: ")

    if choice == "quit":
        print("\nBot says: You little pussy...\n")
        break

    print(f"\n\nBot chose: {botChoice}")
    print(f"You chose: {choice}\n\n")

    if botChoice == "Scissors" and choice == "Rock":
        print("You won!")
    elif botChoice == "Rock" and choice == "Paper":
        print("You won!")
    elif botChoice == "Paper" and choice == "Scissors":
        print("You won!")
    elif botChoice == "Scissors" and choice == "Paper":
        print("Bot won!")
    elif botChoice == "Rock" and choice == "Scissors":
        print("Bot won!")
    elif botChoice == "Paper" and choice == "Rock":
        print("Bot won!")
    else:
        print("Draw!")