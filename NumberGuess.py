from random import randint

attempts = 0


def show_score():
    if attempts == 0:
        print("There is currently no high score!")
    else:
        print("The current high score is: " + str(attempts))


def start_game():
    global attempts
    MAX = 10
    MIN = 0
    random_number = randint(MIN, MAX)
    print("Hi there, lets play a game")
    player_name = input("First, what is your name? ")
    player_choice = input("{}? cool name. Do you want to play? (Enter Yes/No) ".format(player_name))

    while player_choice.lower() == "yes":

        try:
            guess = int(input("Enter a number between {} and {}: ".format(MIN, MAX)))
            if int(guess) < MIN or int(guess) > MAX:
                raise ValueError("Please enter a number between the given range")
            if guess == random_number:
                print("Nice, you got it!")
                attempts += 1
                print("It took you {} attempts to guess it. ".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                random_number = randint(MIN, MAX)
                if play_again.lower() == "no":
                    print("Thank you, lets play again later")
                    break
            elif guess > random_number:
                print("Guess lower")
                attempts += 1
            elif guess < random_number:
                print("Guess higher")
                attempts += 1
        except ValueError as err:
            print("Oh no, that's not a valid value, try again")
            print("({})".format(err))


start_game()
