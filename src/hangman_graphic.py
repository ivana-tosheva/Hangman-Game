import pygame

pygame.init()

# Window
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman GUI")

clock = pygame.time.Clock()
FPS = 60

# Set background image
background = pygame.image.load("../assets/images/blackboard.jpg").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Set gallows
G_WIDTH = 450
G_HEIGHT = 400
gallows_position = (100, 50)

gallows = pygame.image.load("../assets/images/gallows.png").convert_alpha()
gallows = pygame.transform.scale(gallows, (G_WIDTH, G_HEIGHT))

running = True
while running:    # Main loop
    clock.tick(FPS)
    
    # Draw background
    screen.blit(background, (0,0))
    screen.blit(gallows, gallows_position)
    # Show to everyone
    pygame.display.update()

pygame.quit()
