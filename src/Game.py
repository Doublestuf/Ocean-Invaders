from engine import *

from src.Player import Player
from src.Enemy import Enemy

class Game:
    def __init__(self) -> None:
        self.running = True
        
        self.player = Player()
        
        self.grass = pg.Rect(0, 0, window.get_width(), 200)
        self.grass.bottomleft = window.get_rect().bottomleft
    
    def run(self):
        while self.running:
            self.update()
            self.draw()
    
    def update(self) -> None:
        if pg.event.get(pg.QUIT):
            self.running = False
            
        self.player.update(pg.key.get_pressed())
            
        clock.tick(60)
    
    def draw(self) -> None:
        window.fill(BLUE)
        
        pg.draw.rect(window, GREEN, self.grass)
        
        self.player.draw()
        
        pg.display.update()