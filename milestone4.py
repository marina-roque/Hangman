import random
    
class Hangman:
    
    word_list =  ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]

    def __init__(self, num_lives=5):
        self.word = random.choice(self.word_list)
        self.letter_guessed =["_"] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word_list = word_list
     
    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess, {guess} is in the word!")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.letter_guessed[index] = guess
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} left!")
        ###return len(self.num_letters) - 1

    def ask_for_input(self):
        while self.num_lives > 0 and "_" in self.letter_guessed:
            guess = input("Type one letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print(f"Invalid letter. Please insert a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You have already tried this letter!")
            else:
                self.check_guess(guess)
                print(" ".join(self.letter_guessed))
        if "_" not in self.letter_guessed:
            print("Congratulations, you've guessed the word!")
        else:
            self.list_of_guesses.append(guess)
            print(f"Sorry, you've run out of lives. The word was '{self.word}'.")
            
game = Hangman()
game.ask_for_input()