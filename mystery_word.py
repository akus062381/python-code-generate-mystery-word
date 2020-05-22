import random
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
    "y", "z",
]

def call_random_word():
    # print(random.choice(open("words.txt").read().split()))
    random_word = (random.choice(open("words.txt").read().split()))
    return random_word
    
def length_word():
    random_word = (random.choice(open("words.txt").read().split()))
    length_word = (len(random_word) * "_ ")
    return length_word

def start_game():
    random_word_call = call_random_word()
    word_length = length_word()
    print("The mystery word is: " + word_length)
    print("You have 8 guesses available to you, 1 letter per guess!")

def user_guesses(alphabet):
    guess_by_user = input("Enter your first guess: ")
    if guess_by_user.isalpha():
        return guess_by_user
    else:
        print("Try again")


# def letter_guess(letter, random_wordpull):
#     random_wordpull = call_random_word()
#     output = []
#     if letter in random_wordpull:
#         return letter
#     else:
#         return "_"

#     for letter in random_wordpull:
#         output.append(letter_guess(letter))
#     return output

    


def game_sequence():
    start_game()
    letter = user_guesses(alphabet)
    random_wordpull = call_random_word()
    user_guesses(alphabet)
    # letter_guess(letter, random_wordpull)

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








