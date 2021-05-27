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

#variables
step = 5
choice = 0
spscore = 0
cpuscore = 0
cpumove = 0
p1score = 0
p2score = 0
playgn1 = False
playgn2 = False
h2p = False
arrowpo1 = 200
arrowpo2 = 215
arrowpo3 = 230
spwin = False
cpuwin = False
p1win = False
p2win = False
done = False

#rendering for texts used in game
boldFont48 = pygame.font.Font('freesansbold.ttf', 48)
boldFont32 = pygame.font.Font('freesansbold.ttf', 32)
boldFont30 = pygame.font.Font('freesansbold.ttf', 30)
boldFont24 = pygame.font.Font('freesansbold.ttf', 24)
boldFont16 = pygame.font.Font('freesansbold.ttf', 16)
lightcycleText = boldFont48.render('LIGHT CYCLES', True, colourNeonGreen, colourBlack)
spwinText = boldFont32.render('You WIN!', True, colourWhite, colourBlack)
cpuwinText = boldFont32.render('You LOSE!',True, colourWhite, colourBlack)
p1winText = boldFont32.render('Player 1 Wins!', True, colourWhite, colourBlack)
p2winText = boldFont32.render('Player 2 Wins!', True, colourWhite, colourBlack)
singleText = boldFont32.render('Singleplayer', True, colourWhite, colourBlack)
multiText = boldFont32.render('Multiplayer', True, colourWhite, colourBlack)
h2pText = boldFont32.render('How to play', True, colourWhite, colourBlack)
quitText = boldFont32.render('Quit', True, colourWhite, colourBlack)
h2pPT1 = boldFont30.render('Your goal is to outlast your opponent each round.', True, colourNeonGreen, colourBlack)
h2pPT2 = boldFont24.render('You will lose if you hit yourself, your oponent, or the walls.', True, colourLightPurple, colourBlack)
h2pPT3 = boldFont32.render('The first person to 3 points wins the game.', True, colourLightBlue, colourBlack)
h2pPT4 = boldFont16.render('In singleplayer, use the WASD keys to move up, left, down, and right respectively.', True, colourWhite, colourBlack)
h2pPT5 = boldFont16.render('In multiplayer, player 1 will use the WASD keys to move up, left, down, and right respectively', True, colourWhite, colourBlack)
h2pPT51 = boldFont16.render('and player 2 will use the arrow keys to move based on arrow direction.', True, colourWhite, colourBlack)
playgnText = boldFont16.render('Press Enter to play again', True, colourWhite, colourBlack)
mainmText = boldFont16.render('Press Escape to return to the main menu', True, colourWhite, colourBlack)
mainm2Text = boldFont32.render('Press Enter to return to the main menu', True, colourWhite, colourBlack)

#height/width of board
board_w = w / step
board_h = h / step

#first cycle cube starting positions
cycle1_start_x = 35
cycle1_start_y = 60
cycle2_start_x = 125
cycle2_start_y = 60

#list of 3 cubes making the starting cycle
cycle1 = [[cycle1_start_x,cycle1_start_y],[cycle1_start_x,cycle1_start_y - 1],[cycle1_start_x,cycle1_start_y - 2]]
cycle2 = [[cycle2_start_x,cycle2_start_y],[cycle2_start_x,cycle2_start_y + 1],[cycle2_start_x,cycle2_start_y + 2]]

#function used to draw each cube of the light cycle
def drawBox (wso, x, y, s, c): 
    pygame.draw.rect(wso, c, (x * s, y * s, s, s))

#main loop (is the title screen)
while choice == 0:
    #if play again variables are true skips title screen
    if playgn1:
        choice = 1
    if playgn2:
        choice = 2
    #prints title screen
    if choice == 0:
        wso.fill(colourBlack)
        wso.blit(lightcycleText,(225,100))
        wso.blit(singleText,(300,200))
        wso.blit(multiText,(300,300))
        wso.blit(h2pText,(300,400))
        wso.blit(quitText,(300,500))

    #draws arrow used to select options
    pygame.draw.polygon(wso, colourLightPurple, [(270, arrowpo1),(290, arrowpo2),(270, arrowpo3)])

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            #up and down keys used to move arrow and when enter is pressed option will be selected
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if (event.key == K_UP):
                arrowpo1 -= 100
                arrowpo2 -= 100
                arrowpo3 -= 100
                if arrowpo1 == 100:
                    arrowpo1 = 500
                    arrowpo2 = 515
                    arrowpo3 = 530
            if (event.key == K_DOWN):
                arrowpo1 += 100
                arrowpo2 += 100
                arrowpo3 += 100
                if arrowpo1 == 600:
                    arrowpo1 = 200
                    arrowpo2 = 215
                    arrowpo3 = 230
            if (event.key == K_RETURN):
                if arrowpo1 == 200:
                    choice = 1
                if arrowpo1 == 300:
                    choice = 2
                if arrowpo1 == 400:
                    choice = 3
                if arrowpo1 == 500:
                    pygame.quit()
                    sys.exit()
                    
    #updates display
    pygame.display.update()
    fpsClock.tick(60)

    #single player option
    while choice == 1:
        playgn1 = False
        wso.fill(colourBlack)

        round = 1 + spscore + cpuscore

        #draws circles to keep track of score
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

        #when someone hits a score of 3 goes to win screen
        if spscore == 3:
            spwin = True
            choice = 0
            break

        if cpuscore == 3:
            cpuwin = True
            choice = 0
            break

        #starting x and y directions
        x_dir = 0
        y_dir = -1
        cpux_dir = 0
        cpuy_dir = 1
        
        cycle1 = [[cycle1_start_x,cycle1_start_y],[cycle1_start_x,cycle1_start_y - 1],[cycle1_start_x,cycle1_start_y - 2]]
        cycle2 = [[cycle2_start_x,cycle2_start_y],[cycle2_start_x,cycle2_start_y + 1],[cycle2_start_x,cycle2_start_y + 2]]

        #draws each cycle
        for i in range(len(cycle1)):
            drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourLightBlue)

        for i in range(len(cycle2)):
            drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourNeonGreen)

        #main loop while game is being played
        while not done:
            for event in pygame.event.get():
                #using w,a,s,d you are able to move your cycle
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

            #draws each cube behind the cycle
            drawBox (wso, cycle1[-1][0],cycle1[-1][1],step,colourLightBlue)
            drawBox (wso, cycle2[-1][0],cycle2[-1][1],step,colourNeonGreen)

            #keeps track of new cube positions and draws them 
            drawBox (wso, cycle1[0][0],cycle1[0][1],step,colourLightBlue)
            new_x = cycle1[-1][0] + x_dir
            new_y = cycle1[-1][1] + y_dir
            print (new_x,new_y)
            drawBox (wso, cycle2[0][0],cycle2[0][1],step,colourNeonGreen)
            new_xcpu = cycle2[-1][0] + cpux_dir
            new_ycpu = cycle2[-1][1] + cpuy_dir
            print (new_xcpu,new_ycpu)

            #checks if cycle 1 hits itself or the opponent and ends the game if so
            for i in range(len(cycle1)):
                if cycle1[i][0] == new_x and cycle1[i][1] == new_y:
                    print ('exit',cycle1)
                    done = True
                    fin = 2
                if cycle1[i][0] == new_xcpu and cycle1[i][1] == new_ycpu:
                    print ('exit',cycle1)
                    done = True
                    fin = 1

            #the cpu will randomly make a move or accept its fate and hit itself or the opponent cycle
            for i in range(len(cycle2)):
                if cycle2[i][0] == new_xcpu and cycle2[i][1] == new_ycpu:
                    cpumove = random.randint(1,12)
                    if cpumove <= 5:
                        if cpux_dir == 0:
                            cpux_dir = 1
                            cpuy_dir = 0
                        elif cpuy_dir == 0:
                            cpux_dir = 0
                            cpuy_dir = 1
                    elif cpumove <=10:
                        if cpux_dir == 0:
                            cpux_dir = -1
                            cpuy_dir = 0
                        if cpuy_dir == 0:
                            cpux_dir = 0
                            cpuy_dir = -1
                    else:
                        print ('exit',cycle2)
                        done = True
                        fin = 1
                if cycle2[i][0] == new_x and cycle2[i][1] == new_y:
                    cpumove = random.randint(1,12)
                    if cpumove <= 5:
                        if cpux_dir == 0:
                            cpux_dir = 1
                            cpuy_dir = 0
                        elif cpuy_dir == 0:
                            cpux_dir = 0
                            cpuy_dir = 1
                    elif cpumove <=10:
                        if cpux_dir == 0:
                            cpux_dir = -1
                            cpuy_dir = 0
                        if cpuy_dir == 0:
                            cpux_dir = 0
                            cpuy_dir = -1
                    else:
                        print ('exit',cycle2)
                        done = True
                        fin = 2

            #adds new cube value to cycle list
            cycle1.append([cycle1[-1][0] + x_dir,cycle1[-1][1] + y_dir])
            
            cycle2.append([cycle2[-1][0] + cpux_dir,cycle2[-1][1] + cpuy_dir])

            #if cycle 1 hits the border it will end the game
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

            #if the cpu is about to hit the border it may make a random direction shift or accept its fate
            if cycle2[-1][0] >= board_w -2:
                cpumove = random.randint(1,12)
                if cpumove <= 5:
                    cpux_dir = 1
                    cpuy_dir = 0
                elif cpumove <=10:
                    cpux_dir = -1
                    cpuy_dir = 0
                else:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
            elif cycle2[-1][0] < 2:
                cpumove = random.randint(1,12)
                if cpumove <= 5:
                    cpux_dir = 1
                    cpuy_dir = 0
                elif cpumove <=10:
                    cpux_dir = -1
                    cpuy_dir = 0
                else:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
            if cycle2[-1][1] >= board_h -2:
                cpumove = random.randint(1,12)
                if cpumove <= 5:
                    cpux_dir = 0
                    cpuy_dir = 1
                elif cpumove <=10:
                    cpux_dir = 0
                    cpuy_dir = -1
                else:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
            elif cycle2[-1][1] < 2:
                cpumove = random.randint(1,12) 
                if cpumove <= 5:
                    cpux_dir = 0
                    cpuy_dir = 1 
                elif cpumove <=10:
                    cpux_dir = 0
                    cpuy_dir = -1
                else:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
            #if the cycles hit eachother no one gets a point and it is considered a draw
            if new_x == new_xcpu and new_y == new_ycpu:
                print ('exit')
                done = True
        
            #updates display
            pygame.display.update()
            fpsClock.tick(180)

        #once a round has ended both cycles are deleted simoltaneously a frame at a time
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

        #done becomes false again meaning the main game resets again   
        done = False

    #when the single player wins this is what prints
    while spwin == True:
        wso.fill(colourBlack)
        wso.blit(spwinText,(335,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
        #score of both players are printed
        pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
        pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)
        pygame.draw.circle(wso, colourLightBlue, (65, 20), 10)
        if cpuscore > 0:
            pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
            if cpuscore > 1:
                pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)

        #if escape is pressed goes to main menu if enter is pressed restarts
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

    #when the cpu wins this is what prints
    while cpuwin == True:
        wso.fill(colourBlack)
        wso.blit(cpuwinText,(325 ,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))
        #score of both players are printed
        if spscore > 0:
            pygame.draw.circle(wso, colourLightBlue, (15, 20), 10)
            if spscore > 1:
                pygame.draw.circle(wso, colourLightBlue, (40, 20), 10)                    
        pygame.draw.circle(wso, colourNeonGreen, (785, 20), 10)
        pygame.draw.circle(wso, colourNeonGreen, (760, 20), 10)
        pygame.draw.circle(wso, colourNeonGreen, (735, 20), 10)

        #if escape is pressed goes to main menu if enter is pressed restarts
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

    #multiplayer option  
    while choice == 2:
        playgn2 = False
        wso.fill(colourBlack)

        round = 1 + p1score + p2score

        #draws circles to keep track of score
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

        #when someone hits a score of 3 goes to win screen 
        if p1score == 3:
            p1win = True
            choice = 0
            break

        if p2score == 3:
            p2win = True
            choice = 0
            break

        #starting x and y directions
        x_dir1 = 0
        y_dir1 = -1
        x_dir2 = 0
        y_dir2 = 1
        
        cycle1 = [[cycle1_start_x,cycle1_start_y],[cycle1_start_x,cycle1_start_y - 1],[cycle1_start_x,cycle1_start_y - 2]]
        cycle2 = [[cycle2_start_x,cycle2_start_y],[cycle2_start_x,cycle2_start_y + 1],[cycle2_start_x,cycle2_start_y + 2]]
        
        #draws each cycle
        for i in range(len(cycle1)):
            drawBox (wso, cycle1[i][0],cycle1[i][1],step,colourLightBlue)

        for i in range(len(cycle2)):
            drawBox (wso, cycle2[i][0],cycle2[i][1],step,colourNeonGreen)

        #main loop while game is being played
        while not done:
            for event in pygame.event.get():
                #using w,a,s,d you are able to move your cycle
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

            #draws each cube behind the cycle
            drawBox (wso, cycle1[-1][0],cycle1[-1][1],step,colourLightBlue)
            drawBox (wso, cycle2[-1][0],cycle2[-1][1],step,colourNeonGreen)

            #keeps track of new cube positions and draws them 
            drawBox (wso, cycle1[0][0],cycle1[0][1],step,colourLightBlue)
            new_x1 = cycle1[-1][0] + x_dir1
            new_y1 = cycle1[-1][1] + y_dir1
            print (new_x1,new_y1)
            drawBox (wso, cycle2[0][0],cycle2[0][1],step,colourNeonGreen)
            new_x2 = cycle2[-1][0] + x_dir2
            new_y2 = cycle2[-1][1] + y_dir2
            print (new_x2,new_y2)

            #checks if cycle 1 hits itself or the opponent and ends the game if so
            for i in range(len(cycle1)):
                if cycle1[i][0] == new_x1 and cycle1[i][1] == new_y1:
                    print ('exit',cycle1)
                    done = True
                    fin = 2
                if cycle1[i][0] == new_x2 and cycle1[i][1] == new_y2:
                    print ('exit',cycle1)
                    done = True
                    fin = 1

            #checks if cycle 2 hits itself or the opponent and ends the game if so 
            for i in range(len(cycle2)):
                if cycle2[i][0] == new_x2 and cycle2[i][1] == new_y2:
                    print ('exit',cycle2)
                    done = True
                    fin = 1
                if cycle2[i][0] == new_x1 and cycle2[i][1] == new_y1:
                    print ('exit',cycle2)
                    done = True
                    fin = 2

            #adds new cube value to cycle list     
            cycle1.append([cycle1[-1][0] + x_dir1,cycle1[-1][1] + y_dir1])
            
            cycle2.append([cycle2[-1][0] + x_dir2,cycle2[-1][1] + y_dir2])

            #if cycle 1 hits the border it will end the game
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

            #if cycle 2 hits the border it will end the game
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
            #if the cycles hit eachother no one gets a point and it is considered a draw
            if new_x1 == new_x2 and new_y1 == new_y2:
                print ('exit')
                done = True
        
            #window is not drawn until the update command is called
            pygame.display.update()
            fpsClock.tick(180)


        #once a round has ended both cycles are deleted simoltaneously a frame at a time
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

        #done becomes false again meaning the main game resets again   
        done = False

    #when player 1 wins this is what prints
    while p1win == True:
        wso.fill(colourBlack)
        wso.blit(p1winText,(300,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))

        #score of both players are printed
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

        #if escape is pressed goes to main menu if enter is pressed restarts
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

    #when player 1 wins this is what prints
    while p2win == True:
        wso.fill(colourBlack)
        wso.blit(p2winText,(300 ,275))
        wso.blit(playgnText,(311,315))
        wso.blit(mainmText,(250,340))

        #score of both players are printed
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

        #if escape is pressed goes to main menu if enter is pressed restarts
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

        #updates display
        pygame.display.update()
        fpsClock.tick(60)

    #if how to play is selected
    while choice == 3:
        #tutorial text
        wso.fill(colourBlack)
        wso.blit(h2pPT1,(25,50))
        wso.blit(h2pPT2,(25,150))
        wso.blit(h2pPT3,(25,250))
        wso.blit(h2pPT4,(25,325))
        wso.blit(h2pPT5,(25,385))
        wso.blit(h2pPT51,(25,405))
        wso.blit(mainm2Text,(25,505))

        #checks if button pressed to exit the game or return to main menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if (event.key == K_RETURN):
                    choice = 0
        
        #updates display
        pygame.display.update()
        fpsClock.tick(60)
