import random
from words import words
import string

def get_valid_word(words):
    word=random.choice(words).upper()
    if 4<len(word)<6 and '-' not in word:
        return word
    else:
        return get_valid_word(words)

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    #let user guess
    lives=6
    print("Welcome to HangMan !")
    while lives > 0 and len(word_letters) > 0:
        #Showing users letters they used
        print(f"You have {lives} lives left and you have used these Words {' '.join(used_letters)}")
        #what the current word is ? in dashed terms
        word_list=[letter if letter in used_letters else '_'for letter in word]
        print("Current word : ",' '.join(word_list))

        #user input
        user_letter=input("Guess a Letter : ").upper()

        if user_letter in alphabet-used_letters :
            used_letters.add(user_letter)
            if(user_letter in word_letters):
                word_letters.remove(user_letter)
                print("Correct Guess !")
            else:
                lives-=1
                print("Incorrect Guess , You lost a Life ",lives)
        elif user_letter in used_letters:
            print("You have already used that letter, Try a Different letter")        
        else:
            print("Invalid Guess ,Type a Valid Character between A to Z")

    if lives == 0:
        print(f"You lost! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word}!")


hangman()
