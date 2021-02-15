import pygame
from config import *

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites, game.powerUps)
        self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2), 2)
        self.image.fill(POWER_UP_COLOR)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect

        self.game = game
        self.rect.x = x * TILE_SIZE + TILE_SIZE / 2 - 3
        self.rect.y = y * TILE_SIZE + TILE_SIZE / 2 - 3

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # if collide with player destroy and add 1 to score

    def update(self):
        pass