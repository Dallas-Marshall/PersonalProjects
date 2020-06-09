"""
Hangman Game:
- Words to be guessed - *max word string is 10*
- Number of Guesses
- Guess
    - Check guess is valid
- main function
    - read csv file into list
    - filter out by min length
    - select random word
    - asks for necessary details to start
    - takes users guess
        - error check guess
    - check if guess is correct
        - display guess where letter lies
        - or show that guess was a failure
    - keep asking until word is uncovered or number of wrong guesses is reached
"""

import random

# QUOTA_OF_INCORRECT_GUESSES = int(input("Please enter the number of incorrect guesses allowed: "))
is_valid_input = False
while not is_valid_input:
    try:
        MINIMUM_WORD_LENGTH = int(input("\nPlease select minimum word length (1-10): "))
        if MINIMUM_WORD_LENGTH < 1 or MINIMUM_WORD_LENGTH > 10:
            print("Please select minimum word length between 1 and 10 letters")
        else:
            is_valid_input = True
    except ValueError:
        print("Invalid (not an integer)")


WORD_FILE = 'words.txt'


def main():
    """Program is a game of hangman where user tries to guess a random word."""
    words = read_words()
    word = pick_word(words)
    print(word)


def read_words():
    """Read the text file containing words and save as a list."""
    words = []
    in_file = open('{}'.format(WORD_FILE), 'r', encoding='utf-8-sig')
    for line in in_file:
        word = line.strip()
        words.append(word)
    in_file.close()
    return words


def pick_word(words):
    """Pick a word above minimum length"""
    long_enough_words = []
    for word in words:
        if len(word) >= MINIMUM_WORD_LENGTH:
            long_enough_words.append(word)
    else:
        return long_enough_words[random.randint(0, len(long_enough_words))]


if __name__ == '__main__':
    main()
