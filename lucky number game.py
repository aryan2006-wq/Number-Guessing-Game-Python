import random

def play_game():
    lucky_number = random.randint(1, 50)
    while True:
        user_number = int(input("Guess the number (1-50): "))
        if user_number > lucky_number:
            print("too high")
        elif user_number < lucky_number:
            print("too low")
        else:
            print("Congo, You win🥳🥳")
            break

play_game()