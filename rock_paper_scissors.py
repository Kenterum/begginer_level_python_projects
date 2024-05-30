import random

user_win = 0
computer_win = 0
tie = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock, paper, or scissors? (q to quit): ").lower()
    if user_input == "q":
        quit()

    if user_input not in options:
        print("Please type a valid option.")
        continue

    random_number = random.randint(0, 2)
    computer_input = options[random_number]

    print("Computer chose " + computer_input + ".")

    if user_input == computer_input:
        print("It's a tie!")
        tie += 1
    elif user_input == "rock" and computer_input == "scissors":
        print("You win!")
        user_win += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You win!")
        user_win += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You win!")
        user_win += 1
    else:
        print("Computer wins!")
        computer_win += 1

    play_again = input("Do you want to play again? ").lower()
    if play_again != "yes":
        break

 