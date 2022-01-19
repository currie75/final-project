# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This my final project which is hangman

# Imports
import random
from words import word_list
from datetime import datetime
# This adding the real time now
now = datetime.now()
# 
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#hangman body
Hangman = ['''

    +---+
    |   |
    |
    |
    |
    |
 =========''', '''

    +---+
    |   |
    |   O
    |
    |
    |
 =========''', '''

    +---+
    |   |
    |   O
    |   |
    |
    |
 =========''', '''

    +---+
    |   |
    |   O
    |   |\\
    |
    |
 =========''', '''

    +---+
    |   |
    |   O
    |  /|\\
    |
    |
 =========''', '''

    +---+
    |   |
    |   O
    |  /|\\
    |  /
    |
 =========''', '''

    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
 =========''']

#
Max_wrong = len(Hangman) - 1
#
word = random.choice(word_list)
#
current_guess = "-" * len(word)
#
wrong_guess = 0
#
used_letters = []

#
print("\033[1;35;34m \n")
print("This is Hangman")
print("lets play")
print(Hangman[0])
#


def run():
    global wrong_guess
    global current_guess

    playing = True

    while playing:
        guess = input("enter letters here:")
        guess = guess.lower()

        #
        while guess in used_letters:
            print("You have already used that letter", guess)
            guess = input("add your letters to guess:")
            guess = guess.upper()

        used_letters.append(guess)

        if guess in word:
            print("you have correctly guess a letter!")

            new_current_guess = ""
            for letters in range(len(word)):
                if guess == word[letters]:
                    new_current_guess += guess
                else:
                    new_current_guess += current_guess[letters]

            current_guess = new_current_guess
        else:
            print("sorry thats a wrong guess")

            wrong_guess += 1

        if wrong_guess == Max_wrong:
            print(Hangman[wrong_guess])
            print('\033[1;31;40m you got hanged up mann!')
            print("the correct word is", word)
            playing = False

        if wrong_guess < Max_wrong and current_guess != word:
            print(Hangman[wrong_guess])
            print("you have used these following letter: ", used_letters)
            print("your current word is so far: ", current_guess)

run()
