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

    guesses = []
    letters_guessed = []
    incorrect_guesses = 0

    print("Starting Game!")
    words = read_words()
    word = pick_word(words)

    # Count number of unique letters
    letters_in_word = []
    for letter in word:
        if letter not in letters_in_word:
            letters_in_word.append(letter)

    while len(letters_guessed) != len(letters_in_word) and incorrect_guesses < NUMBER_GUESSES_ALLOWED:
        crypto_word = get_crypto_word(word, guesses)

        guess = get_valid_guess(crypto_word, letters_guessed, incorrect_guesses, guesses)
        guesses.append(guess)

        if guess in word:
            letters_guessed.append(guess)
            print("{} is in the word\n".format(guess))
        else:
            incorrect_guesses += 1
            print("{} is not in the word\n".format(guess))

    if not incorrect_guesses == NUMBER_GUESSES_ALLOWED:
        print("You successfully guessed {}!".format(word))
    else:
        print("Game Over!\nThe word was: {}".format(word))


def get_crypto_word(word, guesses):
    crypto_word = ''
    for letter in word:
        if letter not in guesses:
            crypto_word += '*'
        else:
            crypto_word += letter
    return crypto_word


def get_valid_guess(crypto_word, letters_guessed, incorrect_guesses, guesses):
    """Display guesses and get valid user guess."""
    is_valid_guess = False
    while not is_valid_guess:
        print(crypto_word)
        if len(guesses) != 0:
            print("Previous Guesses: ", end='')
            print(*guesses, sep=',')
            print("Guesses Remaining: {}".format((NUMBER_GUESSES_ALLOWED - incorrect_guesses)))
        guess = input("Guess a letter: ")

        # check guess is valid
        if guess.isalpha() and guess not in letters_guessed and len(guess) == 1 and guess not in guesses:
            is_valid_guess = True
            return guess.lower()
        else:
            if not guess.isalpha():
                print("Invalid (not a Letter)")
            if guess in letters_guessed:
                print("Letter already guessed!")
            if len(guess) != 1:
                print("Only guess one letter at a time!")
            if guess in guesses:
                print("You have already guessed {}".format(guess))
            print('\n')


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
