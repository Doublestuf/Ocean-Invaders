from engine import *

class Player:
    def __init__(self) -> None:
        self.rect = pg.Rect(0, 0, 50, 50)
        self.rect.centerx = window.get_rect().centerx
        self.rect.centery = window.get_height() - 100
        
        self.bullet_rect = pg.Rect(0, 0, 10, 30)
        self.bullet_active = False
        
        self.bullets = []
        
        self.shoot_timer = 0
        
    def shoot(self):
        bullet = self.bullet_rect.copy()
        bullet.centerx = self.rect.centerx
        bullet.bottom = self.rect.top
        self.bullets.append(bullet)
        
        self.bullet_active = True
        
        self.shoot_timer = 60
    
    def update(self, keys_pressed:list):
        key_map = {pg.K_a:(-4, 0), pg.K_d:(4,0)}
        for key in key_map:
            if keys_pressed[key]:
                self.rect.move_ip(key_map[key])
        
        self.rect.clamp_ip(window.get_rect())

        if not self.shoot_timer and [event for event in pg.event.get(pg.KEYUP) if event.key == pg.K_SPACE]:
            self.shoot()
            
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
        pg.draw.rect(window, WHITE, self.rect)
        
        if self.bullet_active:
            for bullet in self.bullets:
                pg.draw.rect(window, RED, bullet)