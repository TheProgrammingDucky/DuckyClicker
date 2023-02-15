import pygame
from pygame_functions import *
import runpy
import globals
from pygame.locals import *
import os

pygame.init()
infoObject = pygame.display.Info()
SCREEN = pygame.display.set_mode((infoObject.current_w / 2, infoObject.current_h / 1.167))
bg = pygame.image.load(f"images/backgrounds/background{globals.bgNum}.xcf")
pygame.display.set_caption("Ducky Clicker - Start")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
font1 = pygame.font.SysFont("monospace", 75)
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)


class Button:
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False


while True:

    clock.tick(20)
    SCREEN.blit(bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    startGameButton = Button(image=pygame.image.load("images/startGameButton.png"), pos=(400, 500))

    for button in [startGameButton]:
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if startGameButton.checkForInput(mouse_pos):
                runpy.run_module(mod_name="game")

    pygame.display.update()
