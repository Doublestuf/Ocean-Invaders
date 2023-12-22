import pygame as pg

shoot_sound = pg.mixer.Sound("audio/shoot.wav")
hurt_sound = pg.mixer.Sound("audio/hurt.wav")
select_sound = pg.mixer.Sound("audio/select.wav")
hit_sound = pg.mixer.Sound("audio/hit.wav")

select_sound.set_volume(0.25)

pg.mixer_music.load("audio/SeeingDouble.wav")
pg.mixer_music.set_volume(0.5)
pg.mixer_music.play(loops=-1)