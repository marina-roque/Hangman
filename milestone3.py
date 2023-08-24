import random 

word_list = ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]

word = random.choice(word_list)
print(word)

while True: 
  guess = input ("Type one letter: ")
  if len(guess) == 1 and guess.isalpha() and guess in word:
    print(f"Good guess, {guess} is in the word!")
    break
  elif guess not in word and guess.isalpha():
    print(f"Sorry, {guess} is not in the word. Try again.")
  else:
    print("that is not a valid input!")
