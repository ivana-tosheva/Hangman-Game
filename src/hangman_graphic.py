import pygame

pygame.init()

# Window
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman GUI")

clock = pygame.time.Clock()
FPS = 60

pygame.quit()
