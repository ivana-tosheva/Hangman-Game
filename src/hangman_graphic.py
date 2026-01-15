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

running = True
while running:    # Main loop
    clock.tick(FPS)
    
    # Draw background
    screen.blit(background, (0,0))
    # Show to everyone
    pygame.display.update()

pygame.quit()
