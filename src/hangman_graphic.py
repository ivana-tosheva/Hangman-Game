import pygame
import string


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
GOLD = (252, 214, 135)
WOOD_BROWN = (109, 59, 29)

#functions
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
            "letter": letter
            })
    return buttons


def draw_letter_buttons(screen, buttons, font):
    for button in buttons:
        # Button background
        pygame.draw.rect(screen, WOOD_BROWN, button["rect"], border_radius=6)
        # Border
        pygame.draw.rect(screen, GOLD, button["rect"], width=2, border_radius=6)
        # Draw letter
        text = font.render(button["letter"], True, GOLD)
        text_rect = text.get_rect(center=button["rect"].center)
        # Draw to screen
        screen.blit(text, text_rect)


#setup
alphabet_buttons = create_letter_buttons(70, 435)
running = True

#loop
while running:    # Main loop
    clock.tick(FPS)
    
    # Draw background
    screen.blit(background, (0,0))
    screen.blit(gallows, gallows_position)

    # Draw letter buttons
    draw_letter_buttons(screen, alphabet_buttons, FONT)

    # Update display (show)
    pygame.display.update()

pygame.quit()
