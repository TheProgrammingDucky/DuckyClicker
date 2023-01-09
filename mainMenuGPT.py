import pygame
import runpy
import globals

pygame.init()
WIDTH, HEIGHT = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ducky Clicker - Start")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
font1 = pygame.font.SysFont("monospace", 75)
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
bg = pygame.image.load(f"images/backgrounds/background{globals.bgNum}.xcf")
start_game_button_image = pygame.image.load("images/startGameButton.png")
start_game_button_rect = start_game_button_image.get_rect(center=(400, 500))

class Button:
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

    def update(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

    def checkForInput(self, position):
        if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
            return True
        return False

start_game_button = Button(image=start_game_button_image, rect=start_game_button_rect)

while True:
    clock.tick(20)
    SCREEN.blit(bg, (0, 0))
    start_game_button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
