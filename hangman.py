import random
from random import randint

with open("hangman.txt", "r") as word_list:
    wordlist = list(word_list)

#wordlist = ['taz', 'abraham', 'bennie', 'cameron']


def hangman():
    attempts = 0
    word = wordlist[random.randint(0, len(wordlist) - 1)]
    space_num = len(word)
    word_list = []
    game_over = False

    # fills a list with underscores
    for i in range(space_num):
        word_list.append("-")
    print(word)

    print("Welcome to a game of hangman. You will see spaces from a random word. Choose a letter to try in the word "
          "and see if you can figure it out! You will have 6 attempts before the game is over")
    play = input("Would you like to play? (Yes/No) \n").lower()

    if play == "yes":
        while not game_over:

            # prints the underscore spaces
            print_list(word_list)

            # gets user input for choosing a letter
            user_letter = input("\nChoose a letter: ").lower()

            # checks if the user inputted letter in present in the word
            if user_letter.lower() in word.lower():
                char_index = []

                # loops through the Word and adds the indexes that the user inputted letter is present at. It then appends these indexes into the char_index list
                for i in range(len(word)):
                    if user_letter == word[i]:
                        char_index.append(i)

                # updates the word_list list with the new letters in their respective indexes
                for i in range(len(char_index)):
                    word_list[char_index[i]] = user_letter
            else:
                print("'{}' is not in this word".format(user_letter))
                attempts += 1
                print("{} attempts left\n".format(6-attempts))
            if attempts == 6:
                game_over = True
                print("Game over, you lost. The word was '{}''".format(word))
            elif "-" not in word_list:
                print("You win! It only took you {} tries".format(attempts))
                game_over = True
    else:
        print("\nWell fuck you too then bitch")


# prints the underscore spaces
def print_list(word_list):
    for i in range(len(word_list)):
        print(word_list[i], end=" ")


hangman()
