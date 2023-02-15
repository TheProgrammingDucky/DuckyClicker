import pygame.font
from pygame_functions import *
import runpy
import globals

pygame.init()
infoObject = pygame.display.Info()
SCREEN = pygame.display.set_mode((infoObject.current_w / 2, infoObject.current_h / 1.167))
bg = pygame.image.load(f"images/backgrounds/background{globals.bgNum}.xcf")
pygame.display.set_caption("Ducky Clicker - Settings")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
font1 = pygame.font.SysFont("monospace", 75)
font2 = pygame.font.SysFont("monospace", 100)
font3 = pygame.font.SysFont("monospace", 35)
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


class Button2:
    def __init__(self, pos, colour, width, height, text):
        self.x = pos[0]
        self.y = pos[1]
        self.colour = colour
        self.text = text
        self.width = width
        self.height = height

    def draw(self, SCREEN, outline=None):
        # call to draw button
        if outline:
            pygame.draw.rect(SCREEN, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(SCREEN, self.colour, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont("monospace", 50)
            text = font.render(self.text, True, (0, 0, 0))
            SCREEN.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def checkForInput(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


while True:

    clock.tick(20)
    SCREEN.blit(bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    images = []
    for num in range(1, 6):
        img = pygame.image.load(f"images/backgrounds/background{num}.xcf")
        images.append(img)

    # All Text Elements Below
    settingsText = font2.render("Settings:", True, black)
    SCREEN.blit(settingsText, (200, 45))

    match globals.bgNum:
        case 1:
            bgText = font3.render("-Blue and Dark Blue", True, black)
        case 2:
            bgText = font3.render("-Green and Blue", True, black)
        case 3:
            bgText = font3.render("-Red and Green", True, black)
        case 4:
            bgText = font3.render("-Yellow and Green", True, black)
        case 5:
            bgText = font3.render("-Pink and Purple", True, black)
        case _:
            bgText = font3.render("-Idk how in the name of fuck you got this tbh the game should have broke ages ago "
                                  "to get this message", True, white)

    SCREEN.blit(bgText, (375, 255))

    # All Buttons Below
    backButton = Button(image=pygame.image.load("images/back.png"), pos=(100, 100))
    backgroundButton = Button2((75, 250), white, 300, 50, "Background")

    backgroundButton.draw(SCREEN)

    for button in [backButton]:
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if backgroundButton.checkForInput(mouse_pos):
                if globals.bgNum >= 5:
                    globals.bgNum = 0
                bg = images[globals.bgNum]
                globals.bgNum += 1
            if backButton.checkForInput(mouse_pos):
                runpy.run_module(mod_name="game")

    pygame.display.update()
