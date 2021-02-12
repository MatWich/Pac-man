import pygame
from classes.Map import Map
from classes.Player import Player
from config import *
from classes.Wall import Wall
from classes.Food import Food
from os import path

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.run = None

        self.set_up()

    def set_up(self):
        self.run = True
        self.map = Map(path.join(PROJECT_DIR, 'map.txt'))
        self.allSprites = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)


    def what_to_create(self, tile, row, col):
        if tile == 'P':
            self.player = Player(self, col, row)
        if tile == 'W':
            Wall(self, col, row)

        if tile == '1':
            Food(self, col, row)



    def mainloop(self):
        while self.run:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def draw(self):
        self.screen.fill(BG_COLOR)
        self.allSprites.draw(self.screen)
        self.draw_grid()
        #self.screen.blit(PAC_MAN[0], (TILE_SIZE, TILE_SIZE))
        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def update(self):
        self.allSprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, RED, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, RED, (0, y), (WIDTH, y))

    def quit(self):
        self.run = False
        pygame.quit()