"""Guessing game - Hangman."""

# Hangman word lists by category

import random

emotions = [
    "happy", "sad", "angry", "excited", "bored",
    "nervous", "surprised", "lonely", "confused", "proud"
]

animals = [
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin",
    "alligator", "tiger", "lion", "zebra", "rabbit"
]

food = [
    "pizza", "burger", "pasta", "sushi", "salad",
    "sandwich", "taco", "steak", "noodles", "pancakes"
]

science = [
    "gravity", "atom", "electron", "photosynthesis", "evolution",
    "neutron", "planet", "molecule", "cell", "enzyme"
]

hobby = [
    "soccer", "basketball", "tennis", "cricket", "swimming",
    "hockey", "volleyball", "baseball", "rugby", "cycling"
]

# Combine into a dictionary for easy access
categories = {
    "E": emotions,
    "A": animals,
    "F": food,
    "S": science,
    "H": hobby
}

chosen_category = input(
    "Please select a category ('E' - emotions, 'A' - animals, "
    "'F' - food, 'S' - science, 'H' - hobby): "
).upper()
word = random.choice(categories[chosen_category])

print("The word you neet to guess is", "_ " * len(word))
guessed_letters = []
wrong_letters = []
guesses_left = 6

# itterate through word with while loop to check if letter is part of it
while guesses_left > 0:
    print(f"Guessed letters: {guessed_letters} ")

    user_input = input("Enter your next letter: ").lower()

    while user_input in guessed_letters:
        print("You already guessed that letter! ")
        user_input = input("Enter your next letter: ").lower()

    if user_input in word:
        print(f"The letter {user_input} is in the word! ")
        guessed_letters.append(user_input)
    else:
        print(f"The letter {user_input} is not part of the word! ")
        guessed_letters.append(user_input)
        guesses_left -= 1
