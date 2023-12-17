from engine import *

class Bullet:
    def __init__(self) -> None:
        self.bullet_rect = pg.Rect(0, 0, 10, 30)
        self.bullet_active = False
        
        self.bullets = []
        
        self.shoot_timer = 0
        
    def shoot(self, rect:pg.Rect):
        bullet = self.bullet_rect.copy()
        bullet.centerx = rect.centerx
        bullet.bottom = rect.top
        self.bullets.append(bullet)
        
        self.bullet_active = True
        
        self.shoot_timer = 60
    
    def update(self, rect:pg.Rect):
        if not self.shoot_timer and [event for event in pg.event.get(pg.KEYUP) if event.key == pg.K_SPACE]:
            self.shoot(rect)
            
        if self.bullet_active:
            self.shoot_timer -= 1
            for bullet in self.bullets:
                bullet.move_ip(0, -4)
                
            if window.get_rect().collidelist(self.bullets) == -1:
                self.bullet_active = False
                self.bullets = []
                
        if self.shoot_timer < 1:
            self.shoot_timer = 0
                
        pg.event.clear(pg.KEYUP)
    
    def draw(self):
        if self.bullet_active:
            for bullet in self.bullets:
                pg.draw.rect(window, RED, bullet)