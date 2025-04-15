import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    Tori_1 = pg.image.load("fig/3.png")
    Tori_1 = pg.transform.flip(Tori_1,True,False)
    Tori_rct = Tori_1.get_rect()
    Tori_rct.center = 300, 200
    key_lst = pg.key.get_pressed()
    tmr = 0
    y=0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        dx,dy = 0,0
        key_lst = pg.key.get_pressed()
        if key_lst:
            Tori_rct.move_ip((-1,0))
        if key_lst[pg.K_UP]:
            dy = -1
            #Tori_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            dy = +1
            #Tori_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:
            dx = -1
            #Tori_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            dx = +2
            #Tori_rct.move_ip((+2,0))
        Tori_rct.move_ip((dx,dy))
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[-x+1600,0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(Tori_1,Tori_rct)
        # Tori_rct.x = 300-x
        y -=2
        pg.display.update()
        tmr += 1        
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()