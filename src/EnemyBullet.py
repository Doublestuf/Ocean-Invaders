from engine import *

class EnemyBullet:
    def __init__(self) -> None:
        self.bullet_rect = pg.Rect(0, 0, 10, 20)
        self.bullets = []
        
    def shoot(self, rect:pg.Rect):
        bullet = self.bullet_rect.copy()
        bullet.centerx = rect.centerx
        bullet.top = rect.bottom
        
        self.bullets.append(bullet)
        
    def update(self):
        for bullet in self.bullets:
            bullet.move_ip(0, 4)
            if not bullet.colliderect(window.get_rect()):
                self.bullets.remove(bullet)
            
    def draw(self):
        for bullet in self.bullets:
            pg.draw.rect(window, RED, bullet)