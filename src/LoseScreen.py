from engine import *
from audio import select_sound
class LoseScreen:
    def __init__(self) -> None:
        big_font = pg.font.Font(default_font_name, 120)
        self.lose_text = big_font.render("Game Over", False, WHITE)
        
        self.lose_text_rect = self.lose_text.get_rect()
        self.lose_text_rect.center = window.get_rect().center
        
        self.small_font = pg.font.Font(default_font_name, 50)
        self.restart_text = self.small_font.render("Press ENTER to restart", False, WHITE)
        
        self.restart_text_rect = self.restart_text.get_rect()
        self.restart_text_rect.centerx = window.get_rect().centerx
        self.restart_text_rect.top = self.lose_text_rect.bottom + 10
        
    def update(self):
        return_pressed = pg.key.get_pressed()[pg.K_RETURN]

        if return_pressed:
            select_sound.play()
        return return_pressed
    
    def draw(self, highscore:int):
        window.fill(DARKRED)
        #fill background with color
        
        highscore_text = self.small_font.render(f"Highscore: {highscore}", False, WHITE)
        highscore_rect = highscore_text.get_rect()
        highscore_rect.centerx = window.get_rect().centerx
        highscore_rect.bottom = self.lose_text_rect.top - 10
        
        window.blit(self.lose_text, self.lose_text_rect)
        window.blit(self.restart_text, self.restart_text_rect)
        window.blit(highscore_text, highscore_rect)