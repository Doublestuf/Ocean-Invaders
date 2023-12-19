import pygame as pg
#import pygame

pg.font.init()
#initialize pygame fonts

window = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
#initialize game window

pg.display.set_caption("Ocean Invaders")
#set game window name

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

LIGHTBLUE = (50, 100, 255)
DARKGREEN = (50, 200, 50)
#color constant variables

default_font_name = "assets/pixel_font.ttf"
#variables