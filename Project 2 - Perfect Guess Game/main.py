import random

def play_game():
    random_number = random.randint(1, 100)
    guesses = 1
    previous_guesses = []
    higher_messages = [
        "Try a bigger number! 📈",
        "Almost there! Think higher. 📊",
        "Keep going! The number is higher. 💪",
        "Not quite, guess a higher number. 🧐"
    ]
    lower_messages = [
        "Try a smaller number! 📉",
        "That's too high. Aim lower! 🎯",
        "Keep going! The number is lower. ⬇️",
        "Nope! That was high. Let's descend! 🪂"
    ]
    winning_messages = [
        "Congratulations! 🎉 You guessed it right! 🏆",
        "Woo-hoo! 🎈 You got it! 🥳",
        "You've conquered the game! 🗡️👑"
    ]

    print("-" * 50)
    print("***GAME STARTS FROM HERE***\n")
    print("Welcome to the (GUESS PERFECT NUMBER) game...")
    print("Guess the number between (1 to 100) to complete it!")

    while True:
        try:
            print('-' * 50)
            user_input = int(input("Guess the number: "))
            if (user_input < 1) or (user_input > 100):
                print("\n⚠️ Invalid input! Enter the number between (1 and 100)!")
                continue

            previous_guesses.append(user_input)

            if (user_input > random_number):
                print(random.choice(lower_messages))
            elif (user_input < random_number):
                print(random.choice(higher_messages))
            else:
                print(f"\n{random.choice(winning_messages)}")
                break

            guesses += 1
            print(f"\nYour previous guesses: {previous_guesses}")

        except ValueError:
            print("\n❌ Invalid input! Please enter a valid integer.")
    
    if (guesses <= 3):
        print(f"Legend detected! You have detected the (number {random_number}) in {guesses} attempts!!")
        print('-' * 50)
    else:
        print(f"Nice job! You have detected the (number {random_number}) in {guesses} attempts!!")
        print('-' * 50)

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if (play_again != 'y'):
        print("\nThanks for playing...\nHope you enjoyed it!\n\n***GAME ENDS HERE***")
        print('-' * 50)
        break