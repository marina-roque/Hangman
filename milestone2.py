import random 

word_list = ["orange", "apple", "watermelon", "strawberry", "blueberry", "banana", "cherry", "kiwi", "mango", "grapefruit", "pineaple", "peach"]

word = random.choice(word_list)
print(word)

while True: 
  guess = input ("Type one letter: ")
  if len(guess) == 1 and guess.isalpha() and guess in word:
    print("Good guess")
    break
  else:
    print("that is not a valid input!")