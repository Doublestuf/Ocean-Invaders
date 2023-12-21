from engine import *

class Health:
    def __init__(self) -> None:
        self.health_amount = 3
        self.sprite = heart_sprite

    def update(self):
        if self.health_amount < 1:
            quit()
        
    def draw(self):
        for x in range(self.health_amount):
            window.blit(self.sprite, (x*55, 65))