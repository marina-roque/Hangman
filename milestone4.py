import random
    
word_list =  ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]
word = random.choice(word_list)
guess = input ("Type one letter: ")

class Hangman:
    
    def __init__(self):
        self.letter_guessed = ("_" * len(self.word))
        self.num_letters = len(self.word)
        self.word_list = ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]
        self.word = list(random.choice(self.word_list))
        self.num_lives = 5
        self.list_of_guesses = []
     
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
        return len(self.num_letters) - 1

    def ask_for_input(self):
        while True:
            guess = input ("Type one letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print(f"Invalid letter. Please insert a single alphabetical letter.")
            elif guess in self.list_of_guesses:
                print("You have already tried this letter!")
            else:
                self.check_guess(guess)
        else:
            guess.append(self.list_of_guesses)
        
print(word)          
test = Hangman()
test.check_guess()