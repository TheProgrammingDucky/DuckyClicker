from pygame_functions import *
import runpy
import globals

pygame.init()
WIDTH, HEIGHT = 800, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(f"images/backgrounds/background{globals.bgNum}.xcf")
pygame.display.set_caption("Ducky Clicker - Shop")
pygame.display.set_icon(pygame.image.load("images/duckInc logo.jpg"))
font1 = pygame.font.SysFont("monospace", 75)
font2 = pygame.font.SysFont("monospace", 100)
font3 = pygame.font.SysFont("monospace", 20)
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
clickPower_level = 7867846884684685684686


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
    backButton = Button(image=pygame.image.load("images/back.png"), pos=(100, 100))
    clickPower_button = Button(image=pygame.image.load("images/duckyPower.xcf"), pos=(200, 300))

    for button in [backButton, clickPower_button]:
        button.update(SCREEN)

    shopText = font2.render("Shop", True, white)
    SCREEN.blit(shopText, (300, 50))
    clickPower_levelTxt = font3.render("Level: " + str(clickPower_level), True, blue)
    SCREEN.blit(clickPower_levelTxt, (180, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if backButton.checkForInput(mouse_pos):
                runpy.run_module(mod_name="game")
            if clickPower_button.checkForInput(mouse_pos):
                clickPower_level += 1

    pygame.display.update()
