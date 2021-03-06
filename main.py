import pygame
import os
import time
import random

WIDTH,HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets" "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets" "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets" "pixel_ship_blue_small.png"))

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets" "pixel_ship_yellow.png"))

#lasers
RED_LASER = RED_SPACE_SHIP = pygame.image.load(os.path.join("assets" "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets" "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets" "pixel_laser_blue.png"))
YELOW_LASER = pygame.image.load(os.path.join("assets" "pixel_laser_yellow.png"))