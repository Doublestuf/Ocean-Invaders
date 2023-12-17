from engine import *

from src.EnemyBullet import EnemyBullet

class Enemy:
    def __init__(self, x, y) -> None:
        self.rect = pg.Rect(0, 0, 50, 100)
        self.rect.left = x
        self.rect.centery = y
        
        self.bullet = EnemyBullet()
        self.shoot_timer = 150
    
    def update(self):
        if self.shoot_timer:
            self.shoot_timer -= 1
        else:
            self.bullet.shoot(self.rect)
            self.shoot_timer = 150
        
        self.bullet.update()
    
    def draw(self):
        pg.draw.rect(window, WHITE, self.rect)
        
        self.bullet.draw()