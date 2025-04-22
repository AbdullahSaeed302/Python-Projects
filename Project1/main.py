'''
-1 = Scissor
0 = Paper
1 = Rock
'''
def play_game():
    print("Welcome to (ROCK, PAPER, SCISSORS) Game!")
    import random

    Computer = random.choice([-1, 0, 1])
    user_input = input("Enter your choice from (r, p, s) respectively: ").lower()
    if user_input == "s" or user_input == "p" or user_input == "r":
        choices = {"s" : -1, "p" : 0, "r" : 1}
        reversed_choices = {-1 : "Scissors", 0 : "Paper", 1 : "Rock"}
        You = choices[user_input]

        print(f"You Choosed: '{reversed_choices[You]}'\nComputer Choosed: '{reversed_choices[Computer]}'")

        if (Computer == You):
            print("Its a Draw!")

        else:
            if (Computer == -1) and (You == 0):
                print("You Lost! Try Again...")

            elif (Computer == -1) and (You == 1):
                print("You Won! Hurrayy!")

            elif (Computer == 0) and (You == -1):
                print("You Won! Hurrayy!")

            elif (Computer == 0) and (You == 1):
                print("You Lost! Try Again...")

            elif (Computer == 1) and (You == -1):
                print("You Lost! Try Again...")

            elif (Computer == 1) and (You == 0):
                print("You Won! Hurrayy!")
    else:
        print("Something went wrong, Choose the right word!\ni.e. (r for Rock), (p for Paper), (s for Scissors)")

while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != "y":
        print("Thanks for playing!")
        break