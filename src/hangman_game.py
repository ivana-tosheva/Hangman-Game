"""Guessing game - Hangman."""

word = "hangman"

print("The word you neet to guess is", "_ " * len(word))
guessed_letters = []
wrong_letters = []
guesses_left = 6

# itterate through word with while loop to check if letter is part of it
while guesses_left > 0:
    print(f"Guessed letters: {guessed_letters} ")
    print(f"Wrong letters: {wrong_letters} ")
    user_input = input("Enter your next letter: ").lower()
    while user_input in wrong_letters or user_input in guessed_letters:
        print("You already guessed that letter! ")
        user_input = input("Enter your next letter: ").lower()
    if user_input in word:
        print(f"The letter {user_input} is in the word! ")
        guessed_letters.append(user_input)
    else:
        print(f"The letter {user_input} is not part of the word! ")
        wrong_letters.append(user_input)
        guesses_left -= 1
