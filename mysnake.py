from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

runing = True
while runing:
    clock.tick(1)

    for event in pg.event.get():
        if event.type == pg.QUIT :
            runing = False
        elif event.type == pg.KEYDOWN :
            if event.key == pg.K_q :    
                runing = False

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()

pg.quit()








#damier verifier si c'est pair ou impair :  i%2==0 pair