from random import randint
import pygame as pg

#Exercice1

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

    x, y = 100, 200            # coin supérieur gauche, en pixels
    width, height = 20, 20     # largeur et hauteur, en pixels
    color = (255, 0, 0)      # rouge, en (R, V, B)
    rect = pg.Rect(x, y, width, height)
    pg.draw.rect(screen, color, rect)
    pg.display.update()

pg.quit()








#damier verifier si c'est pair ou impair :  i%2==0 pair