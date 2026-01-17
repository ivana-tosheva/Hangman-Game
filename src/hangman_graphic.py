import pygame
import string
import random


# Window
WIDTH, HEIGHT = 1000, 700
FPS = 60
BUTTON_SIZE = 50
BUTTON_SPACING = 15

#init
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

#font
FONT = pygame.font.SysFont("Arial", 45)
#colors
GOLD = (222, 184, 135)
WOOD_BROWN = (139, 69, 19)
LIGHT_BROWN = (180, 120, 60)
GRAY = (122,84,35)


def load_file_content(filename: str) -> list[str]:
    with open(filename) as file:
        return file.read().split(", ")

categories = {
    "E": load_file_content("emotions.txt"),
    "A": load_file_content("animals.txt"),
    "F": load_file_content("food.txt"),
    "S": load_file_content("science.txt"),
    "H": load_file_content("hobby.txt")
}

chosen_category = random.choice(list(categories.keys()))
word = random.choice(categories[chosen_category]).upper()

guessed_letters = []
wrong_letters = []
guesses_left = 6
game_over = False
win = False


def get_display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word)


def draw_word(screen, word, guessed):
    text = FONT.render(get_display_word(word, guessed), True, GOLD)
    text_rect = text.get_rect(center=(WIDTH // 2, 350))
    screen.blit(text, text_rect)


# LETTER BUTTONS
def create_letter_buttons(start_x, start_y):
    buttons = []
    letters_per_row = 13

    for index, letter in enumerate(string.ascii_uppercase):
        row = index // letters_per_row  # choses between row0 and row1(14//13=1)
        column = index % letters_per_row  # sets the column number (1%13=1, 5%13=5)

        x = start_x + column * (BUTTON_SIZE + BUTTON_SPACING)
        y = start_y + row * (BUTTON_SIZE + BUTTON_SPACING)
        
        buttons.append({
            "rect": pygame.Rect(x, y, BUTTON_SIZE, BUTTON_SIZE),
            "letter": letter,
            "active": True
            })
    return buttons


def draw_letter_buttons(screen, buttons):
    for button in buttons:
        if button["active"]:
            bg_color = WOOD_BROWN
            border_color = GOLD
            letter_color = GOLD
        else:
            bg_color = LIGHT_BROWN
            border_color = GRAY
            letter_color = GRAY
            
        
        # Draw button background
        pygame.draw.rect(screen, bg_color, button["rect"], border_radius=6)
        # Draw button border
        pygame.draw.rect(screen, border_color, button["rect"], width=5, border_radius=6)
        # Draw the letter
        letter = FONT.render(button["letter"], True, letter_color)
        letter_rect = letter.get_rect(center=button["rect"].center)
        screen.blit(letter, letter_rect)


def handle_button_click(mouse_pos, buttons):
    for button in buttons:
        if button["active"] and button["rect"].collidepoint(mouse_pos):
            button["active"] = False  # deactivate permanently
            return button["letter"]     # can be used for Hangman logic
    return None

#SETUP
alphabet_buttons = create_letter_buttons(70, 435)
running = True

#Main loop
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            letter = handle_button_click(mouse_pos, alphabet_buttons)
            
            if letter:
                #print("Clicked:", letter)  # placeholder for game logic
                if letter in word:
                    guessed_letters.append(letter)
                else:
                    wrong_letters.append(letter)
                    guesses_left -=1
                    
                if all(l in guessed_letters for l in word):
                    game_over = True
                    win = True
                
                if guesses_left <= 0:
                    game_over = True
    
    
    
    # Draw background
    screen.blit(background, (0,0))
    screen.blit(gallows, gallows_position)
    #Draw word
    draw_word(screen, word, guessed_letters)
    # Draw letter buttons
    draw_letter_buttons(screen, alphabet_buttons)

    # Update display (show)
    pygame.display.update()

pygame.quit()
