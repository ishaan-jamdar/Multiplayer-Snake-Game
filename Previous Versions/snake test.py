import pygame, sys, time, random
from pygame.locals import *
fpsClock = pygame.time.Clock()

#set the stage
w = 800
h = 600
wso = pygame.display.set_mode((w,h))
pygame.init()
pygame.display.set_caption("Light Cycles")

#colour definitions
colourRed = pygame.Color(255,0,0)
colourBlue = pygame.Color(0,0,255)
colourGreen = pygame.Color(0,255,0)
colourWhite = pygame.Color(255,255,255)
colourBlack = pygame.Color(0,0,0)
colourLightPurple = pygame.Color(221,160,221)

step = 5
x_dir1 = 0
y_dir1 = -1
x_dir2 = 0
y_dir2 = 1

board_w = w / step
board_h = h / step

cycle1_start_x = 25
cycle1_start_y = 60
cycle2_start_x = 125
cycle2_start_y = 60

cycle1 = [[cycle1_start_x,cycle1_start_y],[cycle1_start_x,cycle1_start_y - 1],[cycle1_start_x,cycle1_start_y - 2]]
cycle2 = [[cycle2_start_x,cycle2_start_y],[cycle2_start_x,cycle2_start_y + 1],[cycle2_start_x,cycle2_start_y + 2]]

count1 = len(cycle1)
count2 = len(cycle2)

def drawBox (wso, x, y, s, c):
    pygame.draw.rect(wso, c, (x * s, y * s, s, s))

done = False
wso.fill(colourLightPurple)

for i in range(len(cycle1)):
    drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourGreen)

for i in range(len(cycle2)):
    drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourRed)

while not done:
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                done = True
            if (event.key == K_w):
                if y_dir1 == 0:
                    y_dir1 = -1
                    x_dir1 = 0
            if (event.key == K_s):
                if y_dir1 == 0:
                    y_dir1 = 1
                    x_dir1 = 0
            if (event.key == K_d):
                if x_dir1 == 0:
                    x_dir1 = 1 
                    y_dir1 = 0
            if (event.key == K_a):
                if x_dir1 == 0:
                    x_dir1 = -1
                    y_dir1 = 0
            if (event.key == K_UP):
                if y_dir2 == 0:
                    y_dir2 = -1
                    x_dir2 = 0
            if (event.key == K_DOWN):
                if y_dir2 == 0:
                    y_dir2 = 1
                    x_dir2 = 0
            if (event.key == K_RIGHT):
                if x_dir2 == 0:
                    x_dir2 = 1 
                    y_dir2 = 0
            if (event.key == K_LEFT):
                if x_dir2 == 0:
                    x_dir2 = -1
                    y_dir2 = 0

    drawBox (wso, cycle1[-1][0],cycle1[-1][1],step,colourGreen)
    drawBox (wso, cycle2[-1][0],cycle2[-1][1],step,colourRed)

    drawBox (wso, cycle1[0][0],cycle1[0][1],step,colourGreen)
    new_x1 = cycle1[-1][0] + x_dir1
    new_y1 = cycle1[-1][1] + y_dir1
    print (new_x1,new_y1)
    drawBox (wso, cycle2[0][0],cycle2[0][1],step,colourGreen)
    new_x2 = cycle2[-1][0] + x_dir2
    new_y2 = cycle2[-1][1] + y_dir2
    print (new_x2,new_y2)

    count1 += 1
    count2 += 1

    for i in range(len(cycle1)):
        if cycle1[i][0] == new_x1 and cycle1[i][1] == new_y1:
            print ('exit',cycle1)
            done = True
        if cycle1[i][0] == new_x2 and cycle1[i][1] == new_y2:
            print ('exit',cycle1)
            done = True
        
    for i in range(len(cycle2)):
        if cycle2[i][0] == new_x2 and cycle2[i][1] == new_y2:
            print ('exit',cycle2)
            done = True
        if cycle2[i][0] == new_x1 and cycle2[i][1] == new_y1:
            print ('exit',cycle2)
            done = True
    
    if count1 == len(cycle1):
        cycle1.pop(0)
    cycle1.append([cycle1[-1][0] + x_dir1,cycle1[-1][1] + y_dir1])
    if count2 == len(cycle2):
        cycle2.pop(0)
    cycle2.append([cycle2[-1][0] + x_dir2,cycle2[-1][1] + y_dir2])

    if cycle1[-1][0] >= board_w -1:
        cycle1[-1][0] = 1 

    elif cycle1[-1][0] < 1:
        cycle1[-1][0] = board_w - 2

    if cycle1[-1][1] >= board_h -1:
        cycle1[-1][1] = 1
        
    elif cycle1[-1][1] < 1:
        cycle1[-1][1] = board_h - 2

    if cycle2[-1][0] >= board_w -1:
        cycle2[-1][0] = 1 

    elif cycle2[-1][0] < 1:
        cycle2[-1][0] = board_w - 2

    if cycle2[-1][1] >= board_h -1:
        cycle2[-1][1] = 1
        
    elif cycle2[-1][1] < 1:
        cycle2[-1][1] = board_h - 2
    #window is not drawn until the update command is called
    pygame.display.update()
    fpsClock.tick(30)

for i in range(len(cycle1)):
    drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourLightPurple)
    pygame.display.update()
    fpsClock.tick(120)
for i in range(len(cycle2)):
    drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourLightPurple)
    pygame.display.update()
    fpsClock.tick(120)
time.sleep(.5)
sys.exit(0)
