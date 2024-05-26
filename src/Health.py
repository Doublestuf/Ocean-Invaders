from engine import *

class Health:
    def __init__(self) -> None:
        self.health_amount = 3
        self.sprite = heart_sprite

    def update(self):
        return self.health_amount < 1
        
    def draw(self):
        for x in range(self.health_amount):
            window.blit(self.sprite, (20 + x*55, 65))