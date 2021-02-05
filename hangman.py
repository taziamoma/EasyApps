import random
import string
from random import randint

with open("hangman.txt", "r") as word_list:
    wordlist = list(word_list)


def hangman():
    print("Welcome to a game of hangman. You will see spaces from a random word. Choose a letter to try in the word "
          "and see if you can figure it out! You will have 6 attempts before the game is over")
    play = input("Would you like to play? (Yes/No) \n").lower()

    # ask user for their preferred difficulty
    if play == "yes":
        difficulty = input(
            "What difficulty would you like to play? Easy = 1-5 letters, Medium = 6-10 letters, Hard = 11+ letter \n").lower()

        word = wordlist[random.randint(0, len(wordlist) - 1)].strip()
        attempts = 0
        max_attempts = 0

        # check user defined difficulty
        if difficulty == "easy":
            max_attempts = 6
            while len(word) > 5:
                word = wordlist[random.randint(0, len(wordlist) - 1)].strip()
        elif difficulty == "medium":
            max_attempts = 9
            while len(word) < 5 or len(word) > 10:
                word = wordlist[random.randint(0, len(wordlist) - 1)].strip()
        else:
            max_attempts = 12
            while len(word) < 11:
                word = wordlist[random.randint(0, len(wordlist) - 1)].strip()

        # define setup variables
        space_num = len(word)
        word_list = []
        game_over = False
        letters_used = []

        # fills a list with underscores
        for i in range(space_num):
            word_list.append("-")

        while not game_over:

            # prints the underscore spaces
            print_list(word_list)

            # gets user input for choosing a letter
            user_letter = input("\nChoose a letter: ").lower()

            # adds letters used to list
            add_letters_used(user_letter, letters_used)

            print("Letters used: ", end="")
            print_used_list(letters_used)
            print("")
            print("Letters not used: ", end="")
            print_not_used_list(letters_used)
            print("")

            # checks if the user inputted letter in present in the word
            if user_letter.lower() in word.lower():
                char_index = []
                attempt = + 1
                add_letters_used(user_letter, letters_used)

                # loops through the Word and adds the indexes that the user inputted letter is present at. It then
                # appends these indexes into the char_index list
                for i in range(len(word)):
                    if user_letter == word[i]:
                        char_index.append(i)

                # updates the word_list list with the new letters in their respective indexes
                for i in range(len(char_index)):
                    word_list[char_index[i]] = user_letter
            else:
                add_letters_used(user_letter, letters_used)
                print("'{}' is not in this word".format(user_letter))
                attempts += 1

                print("{} attempts left\n".format(max_attempts - attempts))

            if attempts == max_attempts:
                game_over = True
                print("Game over, you lost. The word was '{}'".format(word))
            elif "-" not in word_list:
                print("\nYou win! The word word was '{}'. It only took you {} tries".format(word, attempts))
                game_over = True
            for _ in range(50):
                print("#", end=" ")
            print("")
    else:
        print("\nWe'll see you next time then!")


# prints the underscore spaces
def print_list(words_list):
    for i in range(len(words_list)):
        print(words_list[i], end=" ")


def print_used_list(list):
    for i in range(len(list)):
        print(list[i], end=" ")


def print_not_used_list(list):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for i in list:
        for k in alphabet:
            if i == k:
                alphabet.remove(k)

    for j in range(len(alphabet)):
        print(alphabet[j], end=" ")


def add_letters_used(user_letter, letters_used):
    if user_letter not in letters_used:
        letters_used.append(user_letter)


hangman()
