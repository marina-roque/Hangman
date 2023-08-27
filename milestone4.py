##### Milestone 4.test
import random

word_list =  ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.letter_guessed = list("_ " * len(word))
        self.num_letters = len(word)
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        if guess in word:
            print(f"Good guess, {guess} is in the word!")
            for index, letter in enumerate(word):
                if letter == guess:
                    letter_guessed[index] = guess
        else:
            num_lives - 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {num_lives} left!")
        return len(num_letters) - 1

    def ask_for_input(self):
        while True:
            guess = input ("Type one letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print(f"Invalid letter. Please insert a single alphabetical letter.")
            elif guess in list_of_guesses:
                print("You have already tried this letter!")
            else:
                check_guess(guess)
        else:
            guess.append(list_of_guesses)
