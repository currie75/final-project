# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This my final project which is hangman

# Imports
import random
from words import word_list

#hangman body
Hangman = ['''
    +---+
    |   |
    |
    |
    |
    |
 =========''','''

    +---+
    |   |
    |   O
    |
    |
    |
 =========''','''

    +---+
    |   |
    |   O
    |   |
    |
    |
 =========''','''

    +---+
    |   |
    |   O
    |   |\
    |
    |
 =========''','''

    +---+
    |   |
    |   O
    |  /|\
    |
    |
 =========''','''

    +---+
    |   |
    |   O
    |  /|\
    |  / 
    |
 =========''','''

    +---+
    |   |
    |   O
    |  /|\
    |  / \
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
print("\033[1;34;20m \n")
print("This is Hangman")
print("lets play")
#
while wrong_guess < Max_wrong and current_guess != word:
    print(Hangman[wrong_guess])
    print("you have used these following letter: ",used_letters)
    print("your current word is so far: ",current_guess)
#
guess = input("enter letters here:")
guess = guess.upper()