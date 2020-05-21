import random

def call_random_word():
    # print(random.choice(open("words.txt").read().split()))
    random_word = (random.choice(open("words.txt").read().split()))
    length_word = (len(random_word) * "_ ")
    return length_word

# def letter_guess(letter, guesses):
    # word = 



def game_sequence():
    random_word_call = call_random_word()
    print("The mystery word is: " + random_word_call)
    print("You have 8 guesses available to you, 1 letter per guess!")
    print("Your first guess: ")

game_sequence()


# game starts by showing user how many characters in the word
# game alerts user that they have 8 guesses of 1 letter each guess
# game prompts user to make a guess and provides an input
# user enters a letter
# game shows empty spaces of word and if letter correct, fills in
# game prompts user to continue guessing until they've guessed 8x
# after each guess, game reminds user how many more guesses they have
# if user guesses wrong, they lose a guess
# if user guesses right, they do not lose a guess
# if user makes duplicate guess, game alerts user they already made guess
# game ends if: user gets word OR if user runs out of guesses
# game asks user if they want to play again, gives yes or no choice
# game begins again if user says yes








