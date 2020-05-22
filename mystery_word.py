import random
alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
    "y", "z",
]

def get_random_word():
    random_word = (random.choice(open("words.txt").read().split()))
    print(random_word.lower())
    return random_word.lower()
    

# def start_game():
#     random_word_call = get_random_word()
#     word_display = display_word(random_word_call)
#     print("The mystery word is: " + word_display)
#     print("You have 8 guesses available to you, 1 letter per guess!")

def user_guesses():
    count = 1
    while(count <= 8):
        guess_by_user = input("Enter your guess: ")
        if (len(str(guess_by_user)) == 1) and (guess_by_user.isalpha()):
            count = count + 1
            print("Guess again")
        else:
            break
    return guess_by_user

word = get_random_word()
current_guesses = user_guesses()

def letter_guess(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"
output = []
for letter in word:
    output.append(letter_guess(letter, current_guesses))
print(output)



    


# def game_sequence():
#     start_game()
#     user_guesses(alphabet)


# game_sequence()




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








