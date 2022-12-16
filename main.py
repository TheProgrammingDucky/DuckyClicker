import sys
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ducky Clicker")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
