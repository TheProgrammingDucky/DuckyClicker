import pygame.mixer
from pygame_functions import *
import runpy
import globals

# All images/fonts below here
pygame.init()
WIDTH, HEIGHT = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(f"images/backgrounds/background{globals.bgNum}.xcf")
pygame.display.set_caption("Ducky Clicker")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
font1 = pygame.font.SysFont("monospace", 75)
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
quack_sound = pygame.mixer.Sound("sounds/quack.wav")
pygame.mixer.Sound.set_volume(quack_sound, 0.03)


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
    scoreText = font1.render("Quacks: {0}".format(globals.score), True, white)
    SCREEN.blit(scoreText, (150, 20))

    mainDuck = Button(image=pygame.image.load("images/duckInc logo.png"), pos=(400, 500))
    shopIcon = Button(image=pygame.image.load("images/shopIcon.png"), pos=(200, 900))
    settingsIcon = Button(image=pygame.image.load("images/settingsIcon.png"), pos=(400, 900))
    prestigeIcon = Button(image=pygame.image.load("images/prestigeIcon2.png"), pos=(600, 900))

    for button in [mainDuck, shopIcon, settingsIcon, prestigeIcon]:
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save = open("save.txt", "wt")
            save.write(str(globals.score))
            save.write("\n" + str(globals.clickPower))
            save.close()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mainDuck.checkForInput(mouse_pos):
                globals.score += globals.clickPower
                pygame.mixer.Sound.play(quack_sound)
            if shopIcon.checkForInput(mouse_pos):
                save = open("save.txt", "wt")
                save.write(str(globals.score))
                save.write("\n" + str(globals.clickPower))
                save.close()
                runpy.run_module(mod_name="shop")
            if settingsIcon.checkForInput(mouse_pos):
                save = open("save.txt", "wt")
                save.write(str(globals.score))
                save.write("\n" + str(globals.clickPower))
                save.close()
                runpy.run_module(mod_name="settings")
            if prestigeIcon.checkForInput(mouse_pos):
                save = open("save.txt", "wt")
                save.write(str(globals.score))
                save.write("\n" + str(globals.clickPower))
                save.close()
                runpy.run_module(mod_name="prestige")
    pygame.display.update()
