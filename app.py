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


def levelLoad(level):
    with open(level) as f:
        print(f.read())


#### LOOP
while True:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    if gameActive == False:
        #### MENU
        pass

    else:

        levelLoad(('level.txt'))
        print('----')

        #### GAME
        for i in range (20):
            pg.draw.line(win, (255,255,255), (i*30,0), (i*30,winHeight), width=1)
        for j in range(20):
            pg.draw.line(win, (255,255,255), (0,j*30), (winWidth,j*30), width=1)

    pg.display.update()
    clock.tick(FPS)
