from config import *
import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites, game.food)
        self.image = pygame.Surface((TILE_SIZE//4, TILE_SIZE//4), 2)
        self.image.fill(YELLOW)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.game = game
        self.rect.x = x * TILE_SIZE + TILE_SIZE / 2
        self.rect.y = y * TILE_SIZE + TILE_SIZE / 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # if collide with player destroy and add 1 to score
    def update(self):
        pass
