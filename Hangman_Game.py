import random

words = ["python", "apple", "tiger", "chair", "robot"]

word = random.choice(words)

guessed = []
attempts = 6
letter = input("Enter a letter: ")
for char in word:
    if char in guessed:
        print(char, end=" ")
    else:
        print("_", end=" ")
if letter not in word:
    attempts -= 1
if all(char in guessed for char in word):
    print("You Win!")