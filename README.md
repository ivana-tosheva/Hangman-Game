# Hangman-Game
Hangman -  is a word guessing game. Proggram randomlly selects a word, phrase, or sentence and the player tries to guess it by suggesting letters or numbers within a certain number of guesses.

## Overview
A word is chosen from a list and is represented by a row of dashes for each letter or number of the word. If the player suggests a letter which occurs in the word, the programm writes it in all its correct positions. If the suggested letter is not present in the word, the programm adds (or alternatively, removes) one hanged element as game progress counter. 
The game ends once the word is guessed, or if all parts are hanged, signifying that all guesses have been used.

## Features
- Random word selection from a word list  
- Tracks correct and incorrect guesses  
- Displays the current word progress  
- Input validation (only single letters allowed)  
- Simple text-based interface (console) GUI comes in further steps

## How to Play

1. The program picks a random word.
2. You guess letters one by one.
3. Each wrong guess adds a piece to the hangman.
4. The game ends when:
- You guess the whole word
- or the hangman is complete

## Technologies Used

1. Python
2. Git & GitHub for version control
3. Pygame for GUI
