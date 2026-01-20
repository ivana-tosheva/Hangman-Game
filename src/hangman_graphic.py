#!/usr/bin/env python3
"""Hangman game to learn words, think hard and have fun."""
import pygame
import string
import random


# Window
WIDTH, HEIGHT = 1000, 700
FPS = 60
BUTTON_SIZE = 50
BUTTON_SPACING = 15

# init
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman GUI")
clock = pygame.time.Clock()

# Set background image
background = pygame.image.load("../assets/images/blackboard.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Set gallows
G_WIDTH = 450
G_HEIGHT = 400
gallows_position = (100, 50)

gallows = pygame.image.load("../assets/images/gallows.png").convert_alpha()
gallows = pygame.transform.scale(gallows, (G_WIDTH, G_HEIGHT))

# Font
FONT = pygame.font.SysFont("Arial", 45)
# Colors
GOLD = (222, 184, 135)
WOOD_BROWN = (139, 69, 19)
LIGHT_BROWN = (180, 120, 60)
GRAY = (122, 84, 35)
BLACK = (0, 0, 0)

GALLOWS_X, GALLOWS_Y = gallows_position
# Hang point
HANG_X = GALLOWS_X + 124
HANG_Y = GALLOWS_Y + 110


def load_file_content(filename: str) -> list[str]:
    """Load a comma-separated word list from a text file."""
    with open(filename) as file:
        return file.read().split(", ")


categories = {
    "E": load_file_content("../assets/files/emotions.txt"),
    "A": load_file_content("../assets/files/animals.txt"),
    "F": load_file_content("../assets/files/food.txt"),
    "S": load_file_content("../assets/files/science.txt"),
    "H": load_file_content("../assets/files/hobby.txt")
}
category_names = {
    "E": "Emotions",
    "A": "Animals",
    "F": "Food",
    "S": "Science",
    "H": "Hobby"
}
chosen_category = random.choice(list(categories.keys()))
word = random.choice(categories[chosen_category]).upper()

guessed_letters = []
wrong_letters = []
guesses_left = 6
game_over = False
win = False


def get_display_word(word, guessed):
    """Create the displayed version of the secret word."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def draw_word(screen, word, guessed):
    """Draw the current state of the guessed word on the screen."""
    text = FONT.render(get_display_word(word, guessed), True, GOLD)
    text_rect = text.get_rect(center=(WIDTH // 2, 350))
    screen.blit(text, text_rect)


# LETTER BUTTONS
def create_letter_buttons(start_x, start_y):
    """Create clickable letter buttons for the alphabet."""
    buttons = []
    letters_per_row = 13

    for index, letter in enumerate(string.ascii_uppercase):
        # choses between row0 and row1(14//13=1)
        row = index // letters_per_row
        # sets the column number (1%13=1, 5%13=5)
        column = index % letters_per_row

        x = start_x + column * (BUTTON_SIZE + BUTTON_SPACING)
        y = start_y + row * (BUTTON_SIZE + BUTTON_SPACING)

        buttons.append({
            "rect": pygame.Rect(x, y, BUTTON_SIZE, BUTTON_SIZE),
            "letter": letter,
            "active": True
            })
    return buttons


def draw_letter_buttons(screen, buttons):
    """Draw all letter buttons (active-dark, inactive-light)."""
    draw_rect = pygame.draw.rect  # alias to shorten line
    for b in buttons:
        letter_color = GOLD if b["active"] else GRAY
        bg_color = WOOD_BROWN if b["active"] else LIGHT_BROWN
        border_color = GOLD if b["active"] else GRAY

        # Draw background and border
        draw_rect(screen, bg_color, b["rect"], border_radius=6)
        draw_rect(screen, border_color, b["rect"], width=5, border_radius=6)

        # Draw the letter
        txt = FONT.render(b["letter"], True, letter_color)
        screen.blit(txt, txt.get_rect(center=b["rect"].center))


def handle_button_click(mouse_pos, buttons):
    """
    Handle mouse clicks: deactivates clicked button and returns its letter.
    """
    for button in buttons:
        if button["active"] and button["rect"].collidepoint(mouse_pos):
            button["active"] = False  # deactivate permanently
            return button["letter"]     # can be used for Hangman logic
    return None


def draw_hangman(screen, mistakes):
    """Draw the hangman figure based on the number of mistakes."""
    if mistakes > 0:  # head
        pygame.draw.circle(
            screen, BLACK, (HANG_X, HANG_Y), 30, 4
        )

    if mistakes > 1:  # body
        pygame.draw.line(
            screen,
            BLACK,
            (HANG_X, HANG_Y + 30),
            (HANG_X, HANG_Y + 100),
            4,
        )

    if mistakes > 2:  # right arm
        pygame.draw.line(
            screen,
            BLACK,
            (HANG_X, HANG_Y + 50),
            (HANG_X + 30, HANG_Y + 70),
            5,
        )

    if mistakes > 3:  # left arm
        pygame.draw.line(
            screen,
            BLACK,
            (HANG_X, HANG_Y + 50),
            (HANG_X - 30, HANG_Y + 70),
            5,
        )

    if mistakes > 4:  # right leg
        pygame.draw.line(
            screen,
            BLACK,
            (HANG_X, HANG_Y + 100),
            (HANG_X + 30, HANG_Y + 130),
            5,
        )

    if mistakes > 5:  # left leg
        pygame.draw.line(
            screen,
            BLACK,
            (HANG_X, HANG_Y + 100),
            (HANG_X - 30, HANG_Y + 130),
            5,
        )


def draw_result(screen, win, word):
    """Draw the win or lose message on the screen."""
    if win:
        text = FONT.render("YOU WIN!", True, GOLD)
    else:
        text = FONT.render(f"YOU LOSE! Word was: {word}", True, GOLD)

    rect = text.get_rect(center=(WIDTH // 2, 260))
    screen.blit(text, rect)


def draw_category(screen, category_key):
    """Draw the selected category name on the screen."""
    text = FONT.render(f"Category: {category_names[category_key]}", True, GOLD)
    rect = text.get_rect(center=(WIDTH // 2, 100))
    screen.blit(text, rect)


# SETUP
alphabet_buttons = create_letter_buttons(70, 435)
running = True

# Main loop
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            letter = handle_button_click(mouse_pos, alphabet_buttons)

            if letter:
                # placeholder for game logic
                if letter in word:
                    guessed_letters.append(letter)
                else:
                    wrong_letters.append(letter)
                    guesses_left -= 1

                if all(l in guessed_letters for l in word):
                    game_over = True
                    win = True

                if guesses_left <= 0:
                    game_over = True

    # Draw background
    screen.blit(background, (0, 0))
    screen.blit(gallows, gallows_position)
    draw_hangman(screen, len(wrong_letters))

    # Draw category
    draw_category(screen, chosen_category)

    # Draw word
    draw_word(screen, word, guessed_letters)

    # Draw win / lose message
    if game_over:
        draw_result(screen, win, word)

    # Draw letter buttons
    draw_letter_buttons(screen, alphabet_buttons)

    # Update display (show)
    pygame.display.update()

pygame.quit()