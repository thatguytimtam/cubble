import pygame as pg

#### INIT
pg.init()
pg.font.init()
winWidth, winHeight = 600, 600

clock = pg.time.Clock()
win = pg.display.set_mode((winWidth, winHeight))
pg.display.set_caption('Cubble v.0.01')

FPS = 120
gameActive = True

#### LOOP
while True:
    win.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if gameActive == False:
        #### MENU
        pass

    else:
        #### GAME
        pass    

    pg.display.update()
    clock.tick(FPS)
