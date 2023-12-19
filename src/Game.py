from engine import *

from src.Player import Player
from src.Enemy import Enemy

from src.TitleScreen import TitleScreen
from src.ScoreCounter import ScoreCounter

class Game:
    def __init__(self) -> None:
        self.running = True
        self.in_menu = True
        
        self.player = Player()
        self.player_score = 0
        
        self.enemies = []
        self.spawn_timer = 30
        
        self.grass = pg.Rect(0, 0, window.get_width(), 200)
        self.grass.bottomleft = window.get_rect().bottomleft
        
        self.title_screen = TitleScreen()
        self.score_counter = ScoreCounter()
    
    def spawn_enemies(self, row:int = 1):
        for x in range(100 if row == 1 else 200, window.get_width()-(100 if row == 1 else 200), 200):
            enemy = Enemy(x+15, 100 if row == 1 else 215)
            enemy.shoot_timer = 300 if row == 1 else 400
            
            self.enemies.append(enemy)

    def run(self):
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
        self.score_counter.update(self.player_score)
        self.player.update(pg.key.get_pressed())
        
        if not self.enemies:
            self.spawn_timer -= 1
            if not self.spawn_timer:
                self.spawn_timer = 30
                self.spawn_enemies()
                self.spawn_enemies(2)
        
        player_bullets = self.player.bullet.bullets
        
        for enemy in self.enemies:
            if enemy.rect.collidelist(player_bullets) != -1:
                self.enemies.remove(enemy)
                self.player_score += 10
                
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
        self.score_counter.draw()