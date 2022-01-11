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

print("\033[1;34;20m \n")
print(word)
print(current_guess)
