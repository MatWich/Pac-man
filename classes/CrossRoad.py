import pygame
from config import *

class CrossRoad(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites, game.crossRoads)
        self.image = pygame.Surface((1, 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.game = game
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass