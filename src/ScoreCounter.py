from engine import *

class ScoreCounter:
    def __init__(self) -> None:
        self.score_count = 0
        
        self.score_font = pg.font.Font(default_font_name, 40)
        self.score_surface = self.score_font.render("Score: 0", False, WHITE)
    
    def update(self, score_count):
        self.score_count = score_count
        self.score_surface = self.score_font.render(f"Score: {self.score_count}", False, WHITE)
    
    def draw(self):
         window.blit(self.score_surface, (20, 0))