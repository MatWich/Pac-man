import pygame
import os

from classes.Ghost import Ghost
from classes.Player import Player

SCR_SIZE = (WIDTH, HEIGHT) = (600, 400)
TITLE = "PAC-MAN"
BG_COLOR = (200, 200, 200)
FPS = 60

PLAYER_SPEED = 100
GHOST_SPEED = 80

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40 ,40)
TILE_SIZE = 16

# DIRS
PROJECT_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(PROJECT_DIR, 'imgs/')

# IMGS
#######################################
CYAN_GHOST = [pygame.transform.scale(pygame.image.load(IMG_DIR + "cyan" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(4)]
PINK_GHOST = [pygame.transform.scale(pygame.image.load(IMG_DIR + "pink" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(4)]
GREEN_GHOST = [pygame.transform.scale(pygame.image.load(IMG_DIR + "green" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(4)]
RED_GHOST = [pygame.transform.scale(pygame.image.load(IMG_DIR + "red" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(4)]

PAC_MAN = [pygame.transform.scale(pygame.image.load(IMG_DIR + "pac-man" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(3)]

SCARED_GHOST = [pygame.transform.scale(pygame.image.load(IMG_DIR + "ghost_scared" + str(x) + ".png"), (TILE_SIZE, TILE_SIZE)) for x in range(1)]

PLAYER_HIT_RECT = pygame.Rect(0, 0, TILE_SIZE - 5, TILE_SIZE - 5)



def collide_hit_rect(sp1, sp2):
    return sp1.hit_rect.colliderect(sp2.rect)

def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
            if isinstance(sprite, Ghost):
                sprite.new_path = True

    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y
            if isinstance(sprite, Ghost):
                sprite.new_path = True

