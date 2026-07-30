import random

user_name = input("Hi there, Enter your name: ")
print("Welcome, " + user_name + "!!")

choices = ["rock", "paper", "scissors"]

play_again = "yes"

while play_again == "yes":

    user_choice = input("Choose rock, paper, or scissors: ")

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")

    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing, " + user_name + "!")