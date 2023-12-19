from engine import *

class TitleScreen:
    def __init__(self) -> None:
        title_font = pg.font.Font(default_font_name, 120)
        #create big font for title text
        
        self.title_text = title_font.render("Ocean Invaders", False, WHITE)
        #create text surface for the game title
        
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.centerx = window.get_rect().centerx
        self.title_text_rect.top = 100
        #set position of the game title text
        
        start_font = pg.font.Font(default_font_name, 30)
        #create smaller font for start text
        
        self.start_text = start_font.render("Press RETURN to Start", False, WHITE)
        #create text surface for starting text
        
        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.centerx = window.get_rect().centerx
        self.start_text_rect.top = self.title_text_rect.bottom + 100
        #set position of the starting text
        
    def update(self):
        return pg.key.get_pressed()[pg.K_RETURN]
        #return if player has started the game
    
    def draw(self):
        window.fill(LIGHTBLUE)
        #fill background with color
        
        window.blit(self.title_text, self.title_text_rect)
        window.blit(self.start_text, self.start_text_rect)
        #draw game title and start text to screen