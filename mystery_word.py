import random
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
    "y", "z",
]

def get_random_word():
    random_word = (random.choice(open("words.txt").read().split()))
    # print(random_word.lower())
    return random_word.lower()


def user_guesses():
    while True:
        guess_by_user = input("Enter your guess: ")
        if (len(str(guess_by_user)) == 1) and (guess_by_user.isalpha()):
            break
        else:
            print("Guess again")
    return guess_by_user


def letter_guess(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"


def game_sequence():
    print("You have 8 guesses available to you, 1 letter per guess!")

    word = get_random_word()
    current_guesses = []
    guesses = 0
    while guesses < 8:
        for letter in word:
            print(letter_guess(letter, current_guesses), end = ' ')
        guess = user_guesses()
        guesses = guesses + 1

        all_correct = True
        for letter in word:
            if letter not in current_guesses:
                all_correct = False
        if all_correct:
            play_again = input("You win! Play again? y or n: ")
            if play_again == "y":
                game_sequence()
            else:
                return

        if guess in word:
            current_guesses.append(guess)
            print("Correct! Guess again.")
        else:
            print("Guess was incorrect")
        if guesses == 8:
            play_again = input("Play again? y or n: ")
            if play_again == "y":
                game_sequence()
            return
        print("Guess again!")

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








