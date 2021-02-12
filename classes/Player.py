import pygame
from config import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        #self.rect.x = x
        #self.rect.y = y
        self.pos = vec(x, y) * TILE_SIZE
        self.vel = vec(0, 0)

    def update(self):
        self.get_keys()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.pos += self.vel * self.game.dt


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel = vec(-PLAYER_SPEED, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel = vec(PLAYER_SPEED, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel = vec(0, -PLAYER_SPEED)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel = vec(0, PLAYER_SPEED)


