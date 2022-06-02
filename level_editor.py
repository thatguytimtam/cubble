import pygame as pg
import sys

#### INIT
pg.init()
pg.font.init()
winWidth, winHeight = 600, 600

clock = pg.time.Clock()
win = pg.display.set_mode((winWidth, winHeight))
pg.display.set_caption('Cubble | Level Editor')

FPS = 120

color1_list = []
color2_list = []
color3_list = []
selected_color = 1

# ideas: generate 30x30 matrix consisting of either 1,2,3 to denote the colors
# then export to txt file to be read in app.py

#### LOOP
while True:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_presses = pg.mouse.get_pressed()
            if mouse_presses[0]:
                if selected_color == 1:
                    color1_list.append([pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]])
                elif selected_color == 2:
                    color2_list.append([pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]])
                elif selected_color == 3:
                    color3_list.append([pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]])
            if mouse_presses[-1]:
                for coord in color1_list:
                    if pg.mouse.get_pos()[0] > coord[0] - 20 and pg.mouse.get_pos()[0] < coord[0] + 20 and pg.mouse.get_pos()[1] > coord[1] - 20 and pg.mouse.get_pos()[1] < coord[1] + 20:
                        color1_list.pop(color1_list.index(coord))
                        
                for coord in color2_list:
                    if pg.mouse.get_pos()[0] > coord[0] - 20 and pg.mouse.get_pos()[0] < coord[0] + 20 and pg.mouse.get_pos()[1] > coord[1] - 20 and pg.mouse.get_pos()[1] < coord[1] + 20:
                        color2_list.pop(color2_list.index(coord))
                
                for coord in color3_list:
                    if pg.mouse.get_pos()[0] > coord[0] - 20 and pg.mouse.get_pos()[0] < coord[0] + 20 and pg.mouse.get_pos()[1] > coord[1] - 20 and pg.mouse.get_pos()[1] < coord[1] + 20:
                        color3_list.pop(color3_list.index(coord))
        if event.type == pg.KEYDOWN:
            if event.key== pg.K_RETURN:
                with open('level.txt', 'w') as f:
                    f.write(f"{color1_list}\r\n")
                    f.write(f"{color2_list}\r\n")
                    f.write(f"{color3_list}\r\n")
                print('submitted')


    #### DRAW GRID
    for i in range (20):
        pg.draw.line(win, (255,255,255), (i*30,0), (i*30,winHeight), width=1)
    for j in range(20):
        pg.draw.line(win, (255,255,255), (0,j*30), (winWidth,j*30), width=1)


    for coord in color1_list:
        cX, cY =  coord[0] // 30, coord[1] // 30
        pg.draw.rect(win, (255,0,0), (cX*30,cY*30, 30, 30), width=0)
    for coord in color2_list:
        cX, cY =  coord[0] // 30, coord[1] // 30
        pg.draw.rect(win, (0,255,0), (cX*30,cY*30, 30, 30), width=0)
    for coord in color3_list:
        cX, cY =  coord[0] // 30, coord[1] // 30
        pg.draw.rect(win, (0,0,255), (cX*30,cY*30, 30, 30), width=0)

    keys = pg.key.get_pressed()
    if keys[pg.K_1]:
        selected_color = 1
    elif keys[pg.K_2]:
        selected_color = 2
    elif keys[pg.K_3]:
        selected_color = 3
    elif keys[pg.K_ESCAPE]:
        for coord in color1_list:
            color1_list.pop(color1_list.index(coord))
        for coord in color2_list:
            color2_list.pop(color2_list.index(coord))
        for coord in color3_list:
            color3_list.pop(color3_list.index(coord))

    pg.display.update()
    clock.tick(FPS)
