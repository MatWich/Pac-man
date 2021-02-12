import pygame
from config import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(RED)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.game = game
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass