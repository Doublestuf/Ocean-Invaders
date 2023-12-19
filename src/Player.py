from engine import *

from src.Bullet import Bullet

class Player:
    def __init__(self) -> None:
        self.rect = pg.Rect(0, 0, 50, 50)
        self.rect.centerx = window.get_rect().centerx
        self.rect.centery = window.get_height() - 100

        self.bullet = Bullet()

    def update(self, keys_pressed:list):
        key_map = {pg.K_a:(-4, 0), pg.K_d:(4, 0), pg.K_LEFT:(-4, 0), pg.K_RIGHT:(4, 0)}
        for key in key_map:
            if keys_pressed[key]:
                self.rect.move_ip(key_map[key])
        
        self.rect.clamp_ip(window.get_rect())
        
        self.bullet.update(self.rect)
    
    def draw(self):
        pg.draw.rect(window, WHITE, self.rect)
        
        self.bullet.draw()