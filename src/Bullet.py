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
        if not self.shoot_timer and pg.key.get_pressed()[pg.K_SPACE]:
            self.shoot(rect)
            
        for bullet in self.bullets:
            if not bullet.colliderect(window.get_rect()):
                self.bullets.remove(bullet)
                
        if not self.bullets:
            self.bullet_active = False
            
        if self.bullet_active:
            self.shoot_timer -= 1
            for bullet in self.bullets:
                bullet.move_ip(0, -4)
        else:
            self.shoot_timer = 0
                
        if self.shoot_timer < 1:
            self.shoot_timer = 0
    
    def draw(self):
        if self.bullet_active:
            for bullet in self.bullets:
                pg.draw.rect(window, GREEN, bullet)