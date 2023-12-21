from engine import *
from audio import select_sound

class LoseScreen:
    def __init__(self) -> None:
        pass
        
    def update(self):
        return_pressed = pg.key.get_pressed()[pg.K_RETURN]

        if return_pressed:
            select_sound.play()
        return return_pressed
    
    def draw(self):
        window.fill(DARKRED)
        #fill background with color
        
        
