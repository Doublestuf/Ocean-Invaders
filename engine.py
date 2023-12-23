import pygame as pg
#import pygame

pg.font.init()
#initialize pygame fonts

pg.mixer.init()
#initialize pygame sfx and music

window = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
#initialize game window

pg.display.set_caption("Ocean Invaders")
pg.display.set_icon(pg.image.load("assets/icon.png"))
#set game window name

pg.mouse.set_visible(False)
#set mouse cursor as invisible

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

LIGHTBLUE = (80, 140, 255)
DARKGREEN = (50, 200, 50)
DARKRED = (150, 0, 0)

OCEANBLUE = (50, 150, 255)
#color constant variables

default_font_name = "assets/pixel_font.ttf"

dolphin_sprite = pg.image.load("assets/dolphin.png")
heart_sprite = pg.image.load("assets/heart.png")
#variables