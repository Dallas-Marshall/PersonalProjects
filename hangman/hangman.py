"""Hangman Game, where user tries to guess letters of a word by Dallas Marshall."""

import random

EASY = [3, 10]
NORMAL = [5, 7]
HARD = [10, 5]
hard_mw = 10
hard_ig = 5

WORD_FILE = 'words.txt'


def main():
    """Program is a game of hangman where user tries to guess a random word."""

    words = read_words()
    print("Welcome!\n")
    menu_selection = get_valid_menu_selection()
    while menu_selection.upper() != 'Q':

        # change to guesses remaining
        guesses = []
        letters_guessed = []
        game_variables = set_game_variables(menu_selection)
        remaining_guesses = game_variables[1]
        word = pick_word(words, game_variables[0])
        print("\nStarting Game!")

        # Count number of unique letters
        letters_in_word = []
        for letter in word:
            if letter not in letters_in_word:
                letters_in_word.append(letter)

        while len(letters_guessed) != len(letters_in_word) and remaining_guesses != 0:
            crypto_word = get_crypto_word(word, guesses)

            guess = get_valid_guess(letters_guessed, guesses, crypto_word, game_variables, remaining_guesses)
            guesses.append(guess)
            if guess in word:
                letters_guessed.append(guess)
                print("\n{} is in the word".format(guess))
            else:
                remaining_guesses -= 1
                print("\n{} is not in the word".format(guess))

        if remaining_guesses != 0:
            print("You successfully guessed {}!\n".format(word))
        else:
            print("Game Over!\nThe word was: {}\n".format(word))
        menu_selection = get_valid_menu_selection()
        print("Thanks for Playing!")


def get_crypto_word(word, guesses):
    """Display an '*' for all un-guessed letters."""
    crypto_word = ''
    for letter in word:
        if letter not in guesses:
            crypto_word += '*'
        else:
            crypto_word += letter
    return crypto_word


def get_valid_guess(letters_guessed, guesses, crypto_word, game_variables, remaining_guesses):
    """Get valid user guess."""
    is_valid_guess = False
    while not is_valid_guess:
        display_hud(crypto_word, guesses, remaining_guesses)
        guess = input("Guess a letter: ")
        # check guess is valid
        if guess.isalpha() and guess not in letters_guessed and len(guess) == 1 and guess not in guesses:
            is_valid_guess = True
            return guess.lower()
        else:
            print('\n')
            if not guess.isalpha():
                print("Invalid (not a Letter)")
            if len(guess) != 1:
                print("Please guess one letter at a time!")
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


def pick_word(words, minimum_word_length):
    """Pick a word above minimum length"""
    long_enough_words = []
    for word in words:
        if len(word) >= minimum_word_length:
            long_enough_words.append(word)
    else:
        return long_enough_words[random.randint(0, len(long_enough_words) - 1)]


def set_game_variables(user_menu_selection):
    """Set minimum word length and number of incorrect guesses allowed depending on user difficulty selection."""
    game_variables = []
    if user_menu_selection.upper == 'E':
        minimum_word_length = EASY[0]
        number_guesses_allowed = EASY[1]
    elif user_menu_selection.upper == 'N':
        minimum_word_length = NORMAL[0]
        number_guesses_allowed = NORMAL[1]
    else:
        minimum_word_length = HARD[0]
        number_guesses_allowed = HARD[1]
    game_variables.append(minimum_word_length)
    game_variables.append(number_guesses_allowed)
    return game_variables


def get_valid_menu_selection():
    """Display guesses and get valid user guess."""
    acceptable_selections = 'QENH'
    is_valid_input = False
    while not is_valid_input:
        menu_selection = input(
            "Please Select from the Following Menu:\n'Q' - Quit\n'E' - Easy\n'N' - Normal\n'H' - Hard\n>>> ")
        try:
            if menu_selection.upper() not in acceptable_selections or len(menu_selection) != 1:
                print("\nInvalid Selection")
            else:
                is_valid_input = True
                return menu_selection
        except AttributeError:
            print("\nInvalid Selection")


def display_hud(crypto_word, guesses, remaining_guesses):
    print(crypto_word)
    if len(guesses) != 0:
        print("Previous Guesses: ", end='')
        print(*guesses, sep=',')
        print("Guesses Remaining: {}".format(remaining_guesses))


if __name__ == '__main__':
    main()
