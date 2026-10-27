from random import randint
import pygame as pg

#Exercice1

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

def draw_board() :

    x, y = 0, 0            # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 255, 255)        # rouge, en (R, V, B)
    
    for i in range(30)  :
        for j in range(15):
            rect = pg.Rect(x, y, width, height)
            pg.draw.rect(screen, color, rect)
            y = y +40
        x=x+20
        if i%2==0:
            y=20
        else :
            y=0
    return

runing = True
while runing:
    clock.tick(1)
     

    for event in pg.event.get():
        if event.type == pg.QUIT :
            runing = False
        elif event.type == pg.KEYDOWN :
            if event.key == pg.K_q :    
                runing = False
    draw_board()
    pg.display.update()

pg.quit()







