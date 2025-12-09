"""Guessing game - Hangman."""

import random


def load_file_content(filename: str) -> list[str]:
    """Read a comma-separated word list from a file and return it as a list."""
    with open(filename) as file:
        content = file.read()
    parts = content.split(", ")
    return parts


# Load hangman category files
emotions = load_file_content("emotions.txt")

animals = load_file_content("animals.txt")

food = load_file_content("food.txt")

science = load_file_content("science.txt")

hobby = load_file_content("hobby.txt")


# Combine into a dictionary for easy access
categories = {
    "E": emotions,
    "A": animals,
    "F": food,
    "S": science,
    "H": hobby
}


def display_word(hidden: str, guessed: list[str]) -> str:
    """Return secret word with guessed letters shown and others hidden."""
    parts = []
    for letter in hidden:
        if letter in guessed:
            parts.append(letter)
        else:
            parts.append("_")
    return " ".join(parts)


# Choose category
chosen_category = input(
    "Please select a category ('E' - emotions, 'A' - animals, "
    "'F' - food, 'S' - science, 'H' - hobby): "
).upper()

# Make sure valid key is entered
while chosen_category not in categories:
    print("Invalid category! Please try again!")
    chosen_category = input("Choose again (E/A/S/F/H): ").upper()

word = random.choice(categories[chosen_category])

guessed_letters: list[str] = []
wrong_letters: list[str] = []
guesses_left = 6

print("The word you neet to guess is")
print(display_word(word, guessed_letters))
print()

HANGMAN_FIGURE = load_file_content("hangman_figure.txt")

# Game loop
while guesses_left > 0:
    print(f"Guessed letters: {guessed_letters} ")
    print(f"Wrong letters: {wrong_letters} ")
    print(f"Guesses left: {guesses_left}")

    user_input = input("Enter your next letter: ").lower()

    # Valid input check
    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a single letter!")
        continue

    # Repeated guesses check
    if user_input in guessed_letters or user_input in wrong_letters:
        print("You already guessed that letter! ")
        continue

    # If valid guess check and append to coresponding list
    if user_input in word:
        print(f"The letter {user_input} is in the word! ")
        guessed_letters.append(user_input)
    else:
        print(f"The letter {user_input} is not part of the word! ")
        wrong_letters.append(user_input)
        guesses_left -= 1

    if all(letter in guessed_letters for letter in word):
        print(f"Congratulations! You guessed the word: {word}")
        break

    if guesses_left == 0:
        print(HANGMAN_FIGURE[-1])
        print(f"You lose! The word is: {word}")
        break

    print(HANGMAN_FIGURE[len(wrong_letters)])
    print(display_word(word, guessed_letters))
    print()