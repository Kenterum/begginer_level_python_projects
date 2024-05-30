# Prompt the user to enter their name
name = input("Please enter your name: ")

# Welcome the user to the adventure
print("Welcome", name, "to this adventure!")

# Prompt the user to choose a direction
answer = input("You are on a dirt road that ends. You can go left or right. Which way would you like to go? ").lower()

# Handle the user's choice
if answer == "left":
    # Prompt the user to choose how to cross the river
    answer = input("You come across a river. Do you want to walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ")

    if answer == "swim":
        # The user chose to swim and gets eaten by an alligator
        print("You swam across and got eaten by an alligator.")
    elif answer == "walk":
        # The user chose to walk and loses the game
        print("You walked for a long time, ran out of water, and lost the game.")
    else:
        # The user entered an invalid option
        print('Not a valid option. You lose.')

elif answer == "right":
    # Prompt the user to choose whether to cross the bridge or go back
    answer = input("You come across a wobbly bridge. Do you want to cross it or go back? Type 'cross' to cross the bridge and 'back' to go back: ")

    if answer == "back":
        # The user chose to go back and loses
        print("You go back and lose.")
    elif answer == "cross":
        # Prompt the user to choose whether to talk to the stranger
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to them? Type 'yes' or 'no': ")

        if answer == "yes":
            # The user chose to talk to the stranger and wins
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            # The user chose not to talk to the stranger and loses
            print("You ignore the stranger and they are offended. You lose.")
        else:
            # The user entered an invalid option
            print('Not a valid option. You lose.')
    else:
        # The user entered an invalid option
        print('Not a valid option. You lose.')

else:
    # The user entered an invalid option
    print('Not a valid option. You lose.')

# Thank the user for playing
print("Thank you for playing,", name)
