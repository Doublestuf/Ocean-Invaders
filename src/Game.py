from engine import *

from src.Player import Player
from src.Enemy import Enemy
from src.TitleScreen import TitleScreen

class Game:
    def __init__(self) -> None:
        self.running = True
        self.in_menu = True
        
        self.player = Player()
        self.enemies = []
        
        self.grass = pg.Rect(0, 0, window.get_width(), 200)
        self.grass.bottomleft = window.get_rect().bottomleft
        
        self.title_screen = TitleScreen()

    def run(self):
        for x in range(100, window.get_width()-100, 200):
            self.enemies.append(Enemy(x+15, 100))
        
        while self.running:
            if pg.event.get(pg.QUIT):
                self.running = False
            
            if self.in_menu:
                self.in_menu = not self.title_screen.update()
                self.title_screen.draw()
            else:
                self.update()
                self.draw()

            pg.display.update()
    
    def update(self) -> None:
        self.player.update(pg.key.get_pressed())
        
        player_bullets = self.player.bullet.bullets
        
        for enemy in self.enemies:
            if enemy.rect.collidelist(player_bullets) != -1:
                self.enemies.remove(enemy)
                
            enemy_bullets = enemy.bullet.bullets
                
            for bullet in enemy_bullets:
                if bullet.collidelist(player_bullets) != -1:
                    enemy_bullets.remove(bullet)
                    player_bullets.remove(player_bullets[bullet.collidelist(player_bullets)])
            
            enemy.update()
            
        clock.tick(60)
    
    def draw(self) -> None:
        window.fill(LIGHTBLUE)
        
        pg.draw.rect(window, DARKGREEN, self.grass)
        
        self.player.draw()
        
        for enemy in self.enemies:
            enemy.draw()