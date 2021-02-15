import pygame
import config
from config import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        pygame.sprite.Sprite.__init__(self, game.allSprites)
        self.game = game
        self.images = config.PAC_MAN
        self.image = pygame.Surface((config.TILE_SIZE, config.TILE_SIZE))
        self.image.fill(config.BLUE)
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.hit_rect = config.PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center

        self.current_img = 1
        self.img_time_swap = None
        #self.rect.x = x
        #self.rect.y = y
        self.pos = vec(x, y) * config.TILE_SIZE
        self.vel = vec(0, 0)

        self.invincible = False

    def update(self):

        if self.img_time_swap == None:
            self.img_time_swap = pygame.time.get_ticks()
        else:
            duration = pygame.time.get_ticks() - self.img_time_swap
            if duration > 20:
                self.current_img += 1
                if self.current_img % len(config.PAC_MAN) == 0:
                    self.current_img = 0
                self.img_time_swap = None

        self.get_keys()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.pos
        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        config.collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        config.collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def img_swap(self, dir):
        if dir == 'left':
            self.image = self.images[self.current_img]
        if dir == 'right':
            self.image = pygame.transform.rotate(self.images[self.current_img], 180)
        if dir == 'up':
            self.image = pygame.transform.rotate(self.images[self.current_img], -90)
        if dir == 'down':
            self.image = pygame.transform.rotate(self.images[self.current_img], 90)




    def get_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel = vec(-config.PLAYER_SPEED, 0)
            self.img_swap('left')
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel = vec(config.PLAYER_SPEED, 0)
            self.img_swap('right')
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel = vec(0, -config.PLAYER_SPEED)
            self.img_swap('up')
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel = vec(0, config.PLAYER_SPEED)
            self.img_swap('down')


