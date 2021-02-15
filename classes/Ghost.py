import pygame
from config import *
import random
vec = pygame.math.Vector2
import config
import datetime


class Ghost(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites, game.ghosts)
        self.image = pygame.Surface((config.TILE_SIZE, config.TILE_SIZE))
        self.image.fill(config.YELLOW)
        self.image.convert_alpha()
        self.game = game
        self.rect = self.image.get_rect()
        self.hit_rect = self.rect
        self.new_path = False
        self.pos = vec(x, y) * config.TILE_SIZE
        self.vel = vec(0, -config.GHOST_SPEED)

    def choose_new_path(self):
        if self.new_path == True:
            #new_dest = random.randint(0, 1)
            new_dest = random.randint(0, 3)
            if new_dest == 0:
                self.vel = vec(0, config.GHOST_SPEED)
            if new_dest == 1:
                self.vel = vec(0, -config.GHOST_SPEED)
            if new_dest == 2:
                self.vel = vec(config.GHOST_SPEED, 0)
            if new_dest == 3:
                self.vel = vec(-config.GHOST_SPEED, 0)

        self.new_path = False


    def update(self):
        if self.game.player.invincible == True:
            self.image = config.SCARED_GHOST[0]
        else:
            self.image = config.GREEN_GHOST[random.randint(0, 3)]

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        config.collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        config.collide_with_walls(self, self.game.walls, 'y')
        self.choose_new_path()
        self.rect.center = self.hit_rect.center


    def draw(self, screen):
        screen.blit(self.image, self.rect)

