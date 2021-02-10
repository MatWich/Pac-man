import pygame
from config import *

class Wall(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.image = pygame.Surface((SQR_SIZE, SQR_SIZE))
        self.image.fill(RED)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.color = RED
        self.game = game
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass