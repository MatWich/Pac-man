import pygame
from config import *
from classes.Wall import Wall

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = False

        self.set_up()

    def set_up(self):
        self.run = True
        self.allSprites = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()

        wall = Wall(self, 3, 6)



    def mainloop(self):
        while self.run:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def draw(self):
        self.screen.fill(BG_COLOR)
        self.allSprites.draw(self.screen)
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.kye == pygame.K_ESCAPE:
                    self.quit()

    def update(self):
        self.allSprites.update()

    def quit(self):
        pygame.quit()
        self.run = False