"""
Hangman Game:
- Words to be guessed - *max word string is 10*
- Number of Guesses
- Guess
    - Check guess is valid
- main function
    - read csv file into list
    - filter out by min length
    - select random word and display asterisks
    - asks for necessary details to start
    - takes users guess
        - error check guess
    - check if guess is correct
        - display guess where letter lies
        - or show that guess was a failure
    - keep asking until word is uncovered or number of wrong guesses is reached
"""

import random

NUMBER_GUESSES_ALLOWED = int(input("Please enter the number of incorrect guesses allowed: "))
is_valid_limit = False
while not is_valid_limit:
    try:
        MINIMUM_WORD_LENGTH = int(input("Please select minimum word length (1-10): "))
        if MINIMUM_WORD_LENGTH < 1 or MINIMUM_WORD_LENGTH > 10:
            print("Please select minimum word length between 1 and 10 letters")
        else:
            is_valid_limit = True
    except ValueError:
        print("Invalid (not an integer)")
WORD_FILE = 'words.txt'


def main():
    """Program is a game of hangman where user tries to guess a random word."""
    words = read_words()
    word = pick_word(words)
    # print(word)
    guesses = []
    letters_guessed = []
    incorrect_guesses = 0

    while len(letters_guessed) != len(word) and incorrect_guesses < NUMBER_GUESSES_ALLOWED: # bug more than 1 of letter
        # print(len(letters_guessed))
        # print(len(word))
        crypto_word = ''
        for letter in word:
            if letter not in guesses:
                crypto_word += '*'
            else:
                crypto_word += letter
        print(crypto_word)

        guess = get_valid_guess(letters_guessed, incorrect_guesses, guesses)
        guesses.append(guess)
        if guess in word:
            letters_guessed.append(guess)
        else:
            incorrect_guesses += 1


def get_valid_guess(letters_guessed, incorrect_guesses, guesses):
    """Display guesses and get valid user guess."""
    is_valid_guess = False
    while not is_valid_guess:
        if len(guesses) != 0:
            print("Previous Guesses: ", end='')
            print(*guesses, sep=',')
            print("Guesses Remaining: {}".format((NUMBER_GUESSES_ALLOWED - incorrect_guesses)))
        guess = input("Guess a letter: ")
        if guess.isalpha() and guess not in letters_guessed and len(guess) == 1 and guess not in guesses:
            is_valid_guess = True
            return guess.lower()
        if not guess.isalpha():
            print("Invalid (not a Letter)")
        if guess in letters_guessed:
            print("Letter already guessed!")
        if len(guess) != 1:
            print("Only guess one letter at a time!")
        if guess in guesses:
            print("You have already guessed {}".format(guess))


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
