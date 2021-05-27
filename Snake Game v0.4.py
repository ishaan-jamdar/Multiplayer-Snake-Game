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
colourNeonGreen = pygame.Color(57,255,20)
colourWhite = pygame.Color(255,255,255)
colourBlack = pygame.Color(0,0,0)
colourLightPurple = pygame.Color(221,160,221)
colourLightBlue = pygame.Color(135,206,250)

step = 5
fin = 0
choice = 0
p1score = 0
p2score = 0
p1win = False
p2win = True

boldFont32 = pygame.font.Font('freesansbold.ttf', 32)
p1winText = boldFont32.render('Player 1 Wins!', True, colourWhite, colourBlack)
p2winText = boldFont32.render('Player 2 Wins!', True, colourWhite, colourBlack)

board_w = w / step
board_h = h / step

cycle1_start_x = 35
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
if choice == 0:
    
    while choice == 1:
        wso.fill(colourBlack)

        round = 1 + p1score + p2score

        if p1score > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if p1score > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)
                if p1score > 2:
                    pygame.draw.circle(wso, colourLightBlue, (65, 20), 10)
                        
        if p2score > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if p2score > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
                if p2score > 2:
                    pygame.draw.circle(wso, colourNeonGreen, (735, 20), 10)

        if p1score == 3:
            p1win = True
            choice = 0
            break

        if p2score == 3:
            p2win = True
            choice = 0
            break
        
        x_dir1 = 0
        y_dir1 = -1
        x_dir2 = 0
        y_dir2 = 1
        
        cycle1 = [[cycle1_start_x,cycle1_start_y],[cycle1_start_x,cycle1_start_y - 1],[cycle1_start_x,cycle1_start_y - 2]]
        cycle2 = [[cycle2_start_x,cycle2_start_y],[cycle2_start_x,cycle2_start_y + 1],[cycle2_start_x,cycle2_start_y + 2]]
        for i in range(len(cycle1)):
            drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourLightBlue)

        for i in range(len(cycle2)):
            drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourNeonGreen)

        while not done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if (event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
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

            drawBox (wso, cycle1[-1][0],cycle1[-1][1],step,colourLightBlue)
            drawBox (wso, cycle2[-1][0],cycle2[-1][1],step,colourNeonGreen)

            drawBox (wso, cycle1[0][0],cycle1[0][1],step,colourLightBlue)
            new_x1 = cycle1[-1][0] + x_dir1
            new_y1 = cycle1[-1][1] + y_dir1
            print (new_x1,new_y1)
            drawBox (wso, cycle2[0][0],cycle2[0][1],step,colourNeonGreen)
            new_x2 = cycle2[-1][0] + x_dir2
            new_y2 = cycle2[-1][1] + y_dir2
            print (new_x2,new_y2)

            count1 += 1
            count2 += 1

            for i in range(len(cycle1)):
                if cycle1[i][0] == new_x1 and cycle1[i][1] == new_y1:
                    print ('exit',cycle1)
                    done = True
                    fin = 2
                if cycle1[i][0] == new_x2 and cycle1[i][1] == new_y2:
                    print ('exit',cycle1)
                    done = True
                    fin = 1
                
            for i in range(len(cycle2)):
                if cycle2[i][0] == new_x2 and cycle2[i][1] == new_y2:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
                if cycle2[i][0] == new_x1 and cycle2[i][1] == new_y1:
                    print ('exit',cycle2)
                    done = True
                    fin = 2
            
            cycle1.append([cycle1[-1][0] + x_dir1,cycle1[-1][1] + y_dir1])
            
            cycle2.append([cycle2[-1][0] + x_dir2,cycle2[-1][1] + y_dir2])

            if cycle1[-1][0] >= board_w -1:
                print ('exit',cycle2)
                done = True
                fin = 2
            elif cycle1[-1][0] < 1:
                print ('exit',cycle2)
                done = True
                fin = 2
            if cycle1[-1][1] >= board_h -1:
                print ('exit',cycle2)
                done = True
                fin = 2
            elif cycle1[-1][1] < 1:
                print ('exit',cycle2)
                done = True
                fin = 2
            if cycle2[-1][0] >= board_w -1:
                print ('exit',cycle2)
                done = True
                fin = 1
            elif cycle2[-1][0] < 1:
                print ('exit',cycle2)
                done = True
                fin = 1
            if cycle2[-1][1] >= board_h -1:
                print ('exit',cycle2)
                done = True
                fin = 1
            elif cycle2[-1][1] < 1:
                print ('exit',cycle2)
                done = True
                fin = 1
            if new_x1 == new_x2 and new_y1 == new_y2:
                print ('exit')
                done = True
        
            #window is not drawn until the update command is called
            pygame.display.update()
            fpsClock.tick(180)

        if fin == 0:
            for i in range((len(cycle1)-1)):
                drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourBlack)
                drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourBlack)
                pygame.display.update()
                fpsClock.tick(180)

        if fin == 1:
            p1score += 1
            for i in range((len(cycle1)-1)):
                drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourBlack)
                drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourBlack)
                pygame.display.update()
                fpsClock.tick(180)
        if fin == 2:
            p2score += 1
            for i in range((len(cycle2)-1)):
                drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourBlack)
                drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourBlack)
                pygame.display.update()
                fpsClock.tick(180)
            
        done = False

    if p1win == True:
        wso.fill(colourBlack)
        wso.blit(p1winText,(300,300))
        if p1score > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if p1score > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)
                if p1score > 2:
                    pygame.draw.circle(wso, colourLightBlue, (65, 20), 10)                    
        if p2score > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if p2score > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
        pygame.display.update()
        fpsClock.tick(60)

    if p2win == True:
        wso.fill(colourBlack)
        wso.blit(p2winText,(300,300))
        if p1score > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if p1score > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)                    
        if p2score > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if p2score > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
                if p2score > 2:
                    pygame.draw.circle(wso, colourNeonGreen, (735, 20), 10) 
        pygame.display.update()
        fpsClock.tick(60)

    #while choice == 2:

    #if refresh:
