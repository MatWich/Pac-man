import pygame
import os

SCR_SIZE = (WIDTH, HEIGHT) = (600, 400)
TITLE = "PAC-MAN"
BG_COLOR = (200, 200, 200)
FPS = 60

PLAYER_SPEED = 100

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40 ,40)
TILE_SIZE = 30

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