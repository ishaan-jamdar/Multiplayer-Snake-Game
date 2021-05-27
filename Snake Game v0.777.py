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
choice = 0
spscore = 0
cpuscore = 0
cpumove = 0
p1score = 0
p2score = 0
playgn1 = False
playgn2 = False
arrowpo1 = 200
arrowpo2 = 215
arrowpo3 = 230
spwin = False
cpuwin = False
p1win = False
p2win = False

boldFont32 = pygame.font.Font('freesansbold.ttf', 32)
boldFont16 = pygame.font.Font('freesansbold.ttf', 16)
spwinText = boldFont32.render('You WIN!', True, colourWhite, colourBlack)
cpuwinText = boldFont32.render('You LOSE!',True, colourWhite, colourBlack)
p1winText = boldFont32.render('Player 1 Wins!', True, colourWhite, colourBlack)
p2winText = boldFont32.render('Player 2 Wins!', True, colourWhite, colourBlack)
singleText = boldFont32.render('Singleplayer', True, colourWhite, colourBlack)
multiText = boldFont32.render('Multiplayer', True, colourWhite, colourBlack)
quitText = boldFont32.render('Quit', True, colourWhite, colourBlack)
playgnText = boldFont16.render('Press Enter to play again', True, colourWhite, colourBlack)
mainmText = boldFont16.render('Press Escape to return to the main menu', True, colourWhite, colourBlack)

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
while choice == 0:
    if playgn1:
        choice = 1
    if playgn2:
        choice = 2
    if choice == 0:
        wso.fill(colourBlack)
        wso.blit(singleText,(300,200))
        wso.blit(multiText,(300,300))
        wso.blit(quitText,(300,400))

    pygame.draw.polygon(wso, colourLightPurple, [(270, arrowpo1),(290, arrowpo2),(270, arrowpo3)])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (event.key == K_UP):
                arrowpo1 -= 100
                arrowpo2 -= 100
                arrowpo3 -= 100
                if arrowpo1 == 100:
                    arrowpo1 = 400
                    arrowpo2 = 415
                    arrowpo3 = 430
            if (event.key == K_DOWN):
                arrowpo1 += 100
                arrowpo2 += 100
                arrowpo3 += 100
                if arrowpo1 == 500:
                    arrowpo1 = 200
                    arrowpo2 = 215
                    arrowpo3 = 230
            if (event.key == K_RETURN):
                if arrowpo1 == 200:
                    choice = 1
                if arrowpo1 == 300:
                    choice = 2
                if arrowpo1 == 400:
                    pygame.quit()
                    sys.exit()
                
    pygame.display.update()
    fpsClock.tick(60)

    while choice == 1:
        playgn1 = False
        wso.fill(colourBlack)

        round = 1 + spscore + cpuscore

        if spscore > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if spscore > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)
                if spscore > 2:
                    pygame.draw.circle(wso, colourLightBlue, (65, 20), 10)
                        
        if cpuscore > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if cpuscore > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
                if cpuscore > 2:
                    pygame.draw.circle(wso, colourNeonGreen, (735, 20), 10)

        if spscore == 3:
            spwin = True
            choice = 0
            break

        if cpuscore == 3:
            cpuwin = True
            choice = 0
            break
        
        x_dir = 0
        y_dir = -1
        cpux_dir = 0
        cpuy_dir = 1
        
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
                        if y_dir == 0:
                            y_dir = -1
                            x_dir = 0
                    if (event.key == K_s):
                        if y_dir == 0:
                            y_dir = 1
                            x_dir = 0
                    if (event.key == K_d):
                        if x_dir == 0:
                            x_dir = 1 
                            y_dir = 0
                    if (event.key == K_a):
                        if x_dir == 0:
                            x_dir = -1
                            y_dir = 0
                            
            for i in range(len(cycle2)):
                if cycle2[i][0] == new_xcpu - 1 and cycle2[i][1] == new_ycpu - 1:
                    cpumove = random.randint(1,12)
                    if cpux_dir == 0:
                        if cpumove >= 5:
                            cpux_dir = 1
                            cpuy_dir = 0
                        if cpumove <= 6:
                            cpux_dir = -1
                            cpuy_dir = 0
                    if cpuy_dir == 0:
                        if cpumove >= 5:
                            cpux_dir = 0
                            cpuy_dir = 1
                        if cpumove <= 6:
                            cpux_dir = 0
                            cpuy_dir = -1
                    
                if cycle2[i][0] == new_x and cycle2[i][1] == new_y:
                    cpumove = random.randint(1,12)
                    if cpux_dir == 0:
                        if cpumove >= 5:
                            cpux_dir = 1
                            cpuy_dir = 0
                        if cpumove <= 6:
                            cpux_dir = -1
                            cpuy_dir = 0
                    if cpuy_dir == 0:
                        if cpumove >= 5:
                            cpux_dir = 0
                            cpuy_dir = 1
                        if cpumove <= 6:
                            cpux_dir = 0
                            cpuy_dir = -1
                            
            if cycle2[-1][0] >= board_w -2:
                cpumove = random.randint(1,12)
                if cpux_dir == 0:
                    if cpumove >= 5:
                        cpux_dir = 1
                        cpuy_dir = 0
                    if cpumove <= 6:
                        cpux_dir = -1
                        cpuy_dir = 0
                if cpuy_dir == 0:
                    if cpumove >= 5:
                        cpux_dir = 0
                          cpuy_dir = 1
                    if cpumove <= 6:
                        cpux_dir = 0
                        cpuy_dir = -1
            elif cycle2[-1][0] < 2:
                print ('exit',cycle2)
                done = True
                fin = 1
            if cycle2[-1][1] >= board_h -2:
                print ('exit',cycle2)
                done = True
                fin = 1
            elif cycle2[-1][1] < 2:
                print ('exit',cycle2)
                done = True
                fin = 1
            if new_x == new_xcpu and new_y == new_ycpu:
                print ('exit')
                done = True

            drawBox (wso, cycle1[-1][0],cycle1[-1][1],step,colourLightBlue)
            drawBox (wso, cycle2[-1][0],cycle2[-1][1],step,colourNeonGreen)

            drawBox (wso, cycle1[0][0],cycle1[0][1],step,colourLightBlue)
            new_x = cycle1[-1][0] + x_dir
            new_y = cycle1[-1][1] + y_dir
            print (new_x,new_y)
            drawBox (wso, cycle2[0][0],cycle2[0][1],step,colourNeonGreen)
            new_xcpu = cycle2[-1][0] + cpux_dir
            new_ycpu = cycle2[-1][1] + cpuy_dir
            print (new_xcpu,new_ycpu)

            count1 += 1
            count2 += 1

            for i in range(len(cycle1)):
                if cycle1[i][0] == new_x and cycle1[i][1] == new_y:
                    print ('exit',cycle1)
                    done = True
                    fin = 2
                if cycle1[i][0] == new_xcpu and cycle1[i][1] == new_ycpu:
                    print ('exit',cycle1)
                    done = True
                    fin = 1
                
            for i in range(len(cycle2)):
                if cycle2[i][0] == new_xcpu and cycle2[i][1] == new_ycpu:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
                if cycle2[i][0] == new_x and cycle2[i][1] == new_y:
                    print ('exit',cycle2)
                    done = True
                    fin = 2
            
            cycle1.append([cycle1[-1][0] + x_dir,cycle1[-1][1] + y_dir])
            
            cycle2.append([cycle2[-1][0] + cpux_dir,cycle2[-1][1] + cpuy_dir])

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
            if new_x == new_xcpu and new_y == new_ycpu:
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
            spscore += 1
            for i in range((len(cycle1)-1)):
                drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourBlack)
                drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourBlack)
                pygame.display.update()
                fpsClock.tick(180)
        if fin == 2:
            cpuscore += 1
            for i in range((len(cycle2)-1)):
                drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourBlack)
                drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourBlack)
                pygame.display.update()
                fpsClock.tick(180)
            
        done = False
        
    while spwin == True:
        wso.fill(colourBlack)
        wso.blit(spwinText,(335,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
        pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
        pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)
        pygame.draw.circle(wso, colourLightBlue, (65, 20), 10)
        if cpuscore > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if cpuscore > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    choice = 0
                    spscore = 0
                    cpuscore = 0
                    spwin = False
                if (event.key == K_RETURN):
                    choice = 0
                    spscore = 0
                    cpuscore = 0
                    playgn1 = True
                    spwin = False
                    
        pygame.display.update()
        fpsClock.tick(60)

    while cpuwin == True:
        wso.fill(colourBlack)
        wso.blit(cpuwinText,(325 ,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
        if spscore > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if spscore > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)                    
        pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
        pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
        pygame.draw.circle(wso, colourNeonGreen, (735, 20), 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    choice = 0
                    spscore = 0
                    cpuscore = 0
                    cpuwin = False
                if (event.key == K_RETURN):
                    choice = 0
                    spscore = 0
                    cpuscore = 0
                    playgn1 = True
                    cpuwin = False
                
        pygame.display.update()
        fpsClock.tick(60)
                    
    while choice == 2:
        playgn2 = False
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

    while p1win == True:
        wso.fill(colourBlack)
        wso.blit(p1winText,(300,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
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

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    choice = 0
                    p1score = 0
                    p2score = 0
                    p1win = False
                if (event.key == K_RETURN):
                    choice = 0
                    p1score = 0
                    p2score = 0
                    playgn2 = True
                    p1win = False
                    
        pygame.display.update()
        fpsClock.tick(60)

    while p2win == True:
        wso.fill(colourBlack)
        wso.blit(p2winText,(300 ,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
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

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    choice = 0
                    p1score = 0
                    p2score = 0
                    p2win = False
                if (event.key == K_RETURN):
                    choice = 0
                    p1score = 0
                    p2score = 0
                    playgn2 = True
                    p2win = False
                
        pygame.display.update()
        fpsClock.tick(60)
