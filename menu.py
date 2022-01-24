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
print('\033[1;33;35m Current Time =', current_time)

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

# max wrong guesses
Max_wrong = len(Hangman) - 1
# random word from word list
word = random.choice(word_list)
# your current guess
current_guess = "-" * len(word)
# the amount of bad guesses
wrong_guess = 0
# puts letter in brackets
used_letters = []

# the intro into hangman
print("\033[1;35;34m \n")
print("This is Hangman")
print("lets play")
print(Hangman[0])


# function that runs all the other functions
def run():
    global wrong_guess
    global current_guess

    playing = True
# function where you put the letters
    while playing:
        guess = input("enter letters here:")
        guess = guess.lower()

# function that tells you already used letters
        while guess in used_letters:
            print("You have already used that letter", guess)
            guess = input("add your letters to guess:")
            guess = guess.upper()

        used_letters.append(guess)
# function puts in letters that you have guessed right
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
# hangman setup for the start
            wrong_guess += 1
# losing function
        if wrong_guess == Max_wrong:
            print(Hangman[wrong_guess])
            print('\033[1;31;40m you got hanged up mann!')
            print("the correct word is", word)
            playing = False
# function that tell you the letters used and current letters guessed
        if wrong_guess < Max_wrong and current_guess != word:
            print(Hangman[wrong_guess])
            print("you have used these following letter: ", used_letters)
            print("your current word is so far: ", current_guess)
# wining function
        if current_guess in word:
            print("\033[1;32;40m you sovled the word", word)
            playing = False
# the call that runs everything
run()
