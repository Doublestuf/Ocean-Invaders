from engine import *

from src.EnemyBullet import EnemyBullet

class Enemy:
    def __init__(self, x, y) -> None:
        self.rect = pg.Rect(0, 0, 50, 100)
        self.rect.left = x
        self.rect.centery = y
        
        self.sprite = dolphin_sprite
        
        self.original_position_left = self.rect.left
        self.original_position_right = self.rect.right
        self.move_distance = 100
        self.times_moved = 0
                
        self.bullet = EnemyBullet()
        self.shoot_timer = 300
    
    def update(self):
        if self.shoot_timer:
            self.shoot_timer -= 1
        else:
            self.bullet.shoot(self.rect)
            self.shoot_timer = 300
        
        self.bullet.update()
        
        left_target = self.original_position_left - self.move_distance
        right_target = self.original_position_right + self.move_distance
        
        if self.rect.right == right_target or self.rect.left == left_target:
            self.times_moved += 1
        
        vector = pg.math.Vector2(self.rect.topleft)
        
        if not self.times_moved % 2:
            vector.move_towards_ip((right_target, self.rect.top), 1)
        else:
            vector.move_towards_ip((left_target, self.rect.top), 1)
            
        self.rect.topleft = vector
        
    def draw(self):
        window.blit(self.sprite, self.rect)
        # pg.draw.rect(window, WHITE, self.rect)
        
        self.bullet.draw()