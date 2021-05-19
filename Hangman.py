#!/usr/bin/env python3

answer_string = 'chicken'
answer = list(answer_string.upper())
guess = ['_' for _ in answer]

letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
wrong_guesses = []

mistakes_made = 0


def hangman_drawing(mistakes: int):
    """Draws the hangman based on the number of mistakes."""
    if mistakes == 0:
        drawing = '''
_______
|     |
|
|
|
|_______
'''
        print(drawing)
    elif mistakes == 1:
        drawing = '''
_______
|     |
|     O
|
|
|_______
'''
        print(drawing)
    elif mistakes == 2:
        drawing = '''
_______
|     |
|     O
|     |
|
|_______
'''
        print(drawing)
    elif mistakes == 3:
        drawing = '''
_______
|     |
|     O
|    /|
|
|_______
'''
        print(drawing)
    elif mistakes == 4:
        drawing = '''
_______
|     |
|     O
|    /|\\
|
|_______
'''
        print(drawing)
    elif mistakes == 5:
        drawing = '''
_______
|     |
|     O
|    /|\\
|    /
|_______
'''
        print(drawing)
    elif mistakes == 6:
        drawing = '''
_______
|     |
|     O
|    /|\\
|    / \\
|_______
'''
        print(drawing)


def print_progress(guess_so_far):
    global wrong_guesses
    global answer_string
    print()
    print('Word:', ''.join(guess_so_far), ' ({} letters)'.format(str(len(answer_string))))
    if len(wrong_guesses) == 0:
        print('Wrong guesses: (None so far)')
    else:
        print('Wrong guesses:', ', '.join(wrong_guesses))


print('Word:', ''.join(guess), ' ({} letters)'.format(str(len(answer_string))))
while True:  # game is still playing
    print()
    guess_letter = input('Guess letter: ').upper()
    if guess_letter not in letters:
        print()
        print('Your guess was not a letter.')
        print_progress(guess)
        continue

    if guess_letter in guess:
        print()
        print('You already guessed {} and it is correct.'.format(guess_letter))
        print_progress(guess)

    elif guess_letter in answer:
        for answer_index in range(len(answer)):
            if guess_letter == answer[answer_index]:
                guess[answer_index] = guess_letter
        print_progress(guess)
        if guess == answer:
            print()
            print('-'*50)
            print('Congratulations!')
            print('The word was, indeed, {}.'.format(answer_string.upper()))
            print('-'*50)
            break
    else:
        if guess_letter in wrong_guesses:
            print()
            print('You already guessed {} and it is wrong.'.format(guess_letter))
            print_progress(guess)
        else:
            wrong_guesses.append(guess_letter)
            mistakes_made += 1
            hangman_drawing(mistakes_made)
            print_progress(guess)
            if mistakes_made == 6:
                print()
                print('-'*50)
                print('Game over!')
                print('The word was {}.'.format(answer_string.upper()))
                print('-'*50)
                break
