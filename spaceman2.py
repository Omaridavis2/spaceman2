import random

custom_words = ["ammo", "bomb", "gun", "real", "oily", "mars", "hood"]

def load_word():

    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ')  
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
  
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
 
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word

def is_guess_in_word(guess, secret_word):

    return guess in secret_word

def spaceman(secret_word):


    
    max_attempts = 7
    attempts = 0
    letters_guessed = []

    print("Welcome to Spaceman!")
    print("Try to guess the secret word.")

    while attempts < max_attempts:
        
        guess = input("Enter a letter: ").lower()

       
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        
        if is_guess_in_word(guess, secret_word):
            print("Good guess!")
        else:
            print("Incorrect guess. Try again.")
            attempts += 1

       
        letters_guessed.append(guess)

        
        current_guessed_word = get_guessed_word(secret_word, letters_guessed)
        print("Current word: " + current_guessed_word)

        
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations! You guessed the word: " + secret_word)
            break

    
    if attempts == max_attempts:
        print("Sorry, you ran out of attempts. The secret word was: " + secret_word)


secret_word = load_word()
spaceman(secret_word)
