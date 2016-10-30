# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:59:15 2016

@author: Jeesoo
"""
from random import *
from math import *
import pygame

def gamePlay(fuel, placeThrust, score, g, planet, winsizeX, winsizeY, screen, black, white, grey, a,b,c,d,k,l,m,n,p,q,r,s, starsX, starsY, font, font1, font2, h, w, clock):
    textX = font.render("X POSITION ", 1, white)
    textY = font.render("ALTITUDE ", 1, white)
    textVX = font.render("HORIZONTAL VELOCITY ", 1, white)
    textVY = font.render("VERTICAL VELOCITY ", 1, white)
    textAngle = font.render("ANGLE ", 1, white)
    textFuel = font.render("FUEL ", 1, white)  
    textScore = font.render("SCORE ", 1, white)
    textPlanet = font.render("ENVIRONMENT ", 1, white)    
    
    x = 100
    y = 150
    vx = randrange(10, 30)
    vy = randrange(5, 15)
    theta = pi/2    
    
    
    run = True    
    while run:
        thrust = 0                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # check if key is pressed
            # if you use event.key here it will give you error at runtime
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if theta-pi/90 >= 0 and theta-pi/90 <= pi:
                        theta = theta - pi/90
       
                elif event.key == pygame.K_RIGHT:
                    if theta+pi/90 >= 0 and theta+pi/90 <= pi:
                        theta = theta + pi/90
  
                elif event.key == pygame.K_UP:
                    if fuel > 0:
                        thrust = placeThrust
                        fuel -= 1
                    
        screen.fill(black)
        x, y, vx, vy = lunarLander(x, y, vx, vy, theta, thrust, g, placeThrust)
                
        spaceship = [(a,b),(c,b),(a,d),(c, d), (k, m), (l, m), (k,b), (l,b), (p,0), (a,0), (p,s), (a,s), (q,0), (r,0), (q,s), (r,s), (c,0), (n,0), (c,s), (n,s)]
        spaceship = rotatePolygon(spaceship, theta-pi/2)
        
        xn1, yn1 = spaceship[0]
        xn2, yn2 = spaceship[1]       
        xn3, yn3 = spaceship[2]        
        xn4, yn4 = spaceship[3]  
        xn5, yn5 = spaceship[4]
        xn6, yn6 = spaceship[5]
        xn7, yn7 = spaceship[6]
        xn8, yn8 = spaceship[7]
        xn9, yn9 = spaceship[8]
        xn10, yn10 = spaceship[9]
        xn11, yn11 = spaceship[10]
        xn12, yn12 = spaceship[11]
        xn13, yn13 = spaceship[12]
        xn14, yn14 = spaceship[13]
        xn15, yn15 = spaceship[14]
        xn16, yn16 = spaceship[15]
        xn17, yn17 = spaceship[16]
        xn18, yn18 = spaceship[17]
        xn19, yn19 = spaceship[18]
        xn20, yn20 = spaceship[19]
        
        # draw a rectangle
        pygame.draw.line(screen, grey, (xn9+x, yn9+y), (xn10+x, yn10+y), 2)
        pygame.draw.line(screen, grey, (xn9+x, yn9+y), (xn11+x, yn11+y), 2)
        pygame.draw.line(screen, grey, (xn11+x, yn11+y), (xn12+x, yn12+y), 2)
        pygame.draw.line(screen, grey, (xn10+x, yn10+y), (xn12+x, yn12+y), 2)

        pygame.draw.line(screen, grey, (xn13+x, yn13+y), (xn14+x, yn14+y), 2)
        pygame.draw.line(screen, grey, (xn14+x, yn14+y), (xn16+x, yn16+y), 2)
        pygame.draw.line(screen, grey, (xn15+x, yn15+y), (xn16+x, yn16+y), 2)
        pygame.draw.line(screen, grey, (xn13+x, yn13+y), (xn15+x, yn15+y), 2)
        
        pygame.draw.line(screen, grey, (xn17+x, yn17+y), (xn18+x, yn18+y), 2)
        pygame.draw.line(screen, grey, (xn18+x, yn18+y), (xn20+x, yn20+y), 2)
        pygame.draw.line(screen, grey, (xn17+x, yn17+y), (xn19+x, yn19+y), 2)
        pygame.draw.line(screen, grey, (xn19+x, yn19+y), (xn20+x, yn20+y), 2)
        
        pygame.draw.line(screen, grey, (xn5+x, yn5+y), (xn6+x, yn6+y), 2)
        pygame.draw.line(screen, grey, (xn5+x, yn5+y), (xn7+x, yn7+y), 2)
        pygame.draw.line(screen, grey, (xn6+x, yn6+y), (xn8+x, yn8+y), 2)
        
        pygame.draw.line(screen, grey, (xn1+x, yn1+y), (xn2+x, yn2+y), 2)
        pygame.draw.line(screen, grey, (xn2+x, yn2+y), (xn4+x, yn4+y), 2)
        pygame.draw.line(screen, grey, (xn3+x, yn3+y), (xn4+x, yn4+y), 2)
        pygame.draw.line(screen, grey, (xn3+x, yn3+y), (xn1+x, yn1+y), 2)
        pygame.draw.line(screen, white, (0, winsizeY - 40), (winsizeX, winsizeY - 40), 2)
        
        # draw stars
        i = 0
        while i < 20:
            pygame.draw.circle(screen, white, (starsX[i], starsY[i]), 1)
            i += 1
        
        # display text on the screen
        # make print values into integers then into bytes        
        xB = str(int(x)).encode("utf-8").decode("utf-8")         
        yB = str(int(winsizeY - y - 52)).encode("utf-8").decode("utf-8") 
        vxB = str(int(vx)).encode("utf-8").decode("utf-8") 
        vyB = str(int(vy)).encode("utf-8").decode("utf-8") 
        angle = str(int(theta*(180/pi))).encode("utf-8").decode("utf-8") 
        fuelB = str(fuel).encode("utf-8").decode("utf-8")  
        scoreB = str(score).encode("utf-8").decode("utf-8") 
        
        # setting fonts, colors, locations of each text fragment and drawing to surface
        textXval = font.render(xB, 1, white)
        textYval = font.render(yB, 1, white)
        textVXval = font.render(vxB, 1, white)
        textVYval = font.render(vyB, 1, white)
        textAngleVal = font.render(angle, 1, white)
        textFuelVal = font.render(fuelB, 1, white)
        textScoreVal = font.render(scoreB, 1, white)
        textNoFuel = font2.render("NO FUEL", 1, white)
        textCrash = font2.render("YOU CRASHED! GAME OVER", 1, white)
        textCrash2 = font.render("YOUR FINAL SCORE IS ", 1, white)
        textWin = font2.render("PERFECT LANDING! YOU SCORED 100 POINTS", 1, white)
        textPlanetStr = font.render(planet.upper(), 1, white)
        
        textNames = font1.render("SCIENTIFIC PROGRAMMING IN BME FINAL PROJECT: BY JEESOO KIM, JAE LEE, SARAH LEE", 1, white)
        
        # blit to screen all text for display 
        screen.blit(textX, (winsizeX - 290, 25))
        screen.blit(textY, (winsizeX - 290, 50))
        screen.blit(textVX, (winsizeX - 290, 75))
        screen.blit(textVY, (winsizeX - 290, 100))
        screen.blit(textXval, (winsizeX - 90, 25))
        screen.blit(textYval, (winsizeX - 90, 50))
        screen.blit(textVXval, (winsizeX - 90, 75))
        screen.blit(textVYval, (winsizeX - 90, 100))
        screen.blit(textAngle, (winsizeX - 290, 125))
        screen.blit(textAngleVal, (winsizeX - 90, 125))
        screen.blit(textFuel, (50, 75))
        screen.blit(textFuelVal, (120, 75))
        screen.blit(textScore, (50, 50))
        screen.blit(textScoreVal, (120, 50))
        screen.blit(textPlanet, (50, 25))
        screen.blit(textPlanetStr, (170, 25))
        
        screen.blit(textNames, (winsizeX - 985, winsizeY - 25))

        if fuel == 0:
            screen.blit(textNoFuel, (winsizeX/2-50, winsizeY/2 - 50))
            pygame.display.update()
        
        if y >= winsizeY-(47+h/2):
                if vx < 10 and vy < 10 and theta*(180/pi) == 90:
                    screen.blit(textWin, (winsizeX/2-250, winsizeY/2-50))
                    score += 100
                    scoreB = str(score).encode("utf-8").decode("utf-8") 
                    textScoreVal = font.render(scoreB, 1, white)                    
                    pygame.display.update()
                    pygame.time.delay(2000)
                    check = 0
                    run = False
                else: 
                    screen.blit(textCrash, (winsizeX/2-175, winsizeY/2-50))
                    screen.blit(textCrash2, (winsizeX/2-150, winsizeY/2-20))
                    screen.blit(textScoreVal, (winsizeX/2 + 50, winsizeY/2-20))
                    pygame.display.update()
                    pygame.time.delay(3000)
                    closeCheck = True                   
                    while closeCheck:                    
                        event = pygame.event.wait()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            closeCheck = False
                            pygame.quit()
                        elif event.type == pygame.QUIT:
                            pygame.quit()
                    check = 1
                    run = False        
        pygame.display.update()
        clock.tick(20)
    
    return fuel, score, run, check


def location(planet):
    place = planet.lower()
    if place == "mercury":
        g = 3.7
        placeThrust = 4
    elif place == "venus":
        g = 8.87
        placeThrust = 4
    elif place == "earth":
        g = 9.8
        placeThrust = 4
    elif place == "mars":
        g = 3.711
        placeThrust = 4
    elif place == "jupiter":
        g = 24.79
        placeThrust = 4
    elif place == "saturn":
        g = 10.44
        placeThrust = 4
    elif place == "uranus":
        g = 8.69
        placeThrust = 4
    elif place == "neptune":
        g = 11.15
        placeThrust = 4
    elif place == "pluto":
        g = 0.62
        placeThrust = 4
    elif place == "moon":
        g = 1.622
        placeThrust = 4
    else:
        print ("That's not a valid planet/moon!")
    return g, placeThrust
        
def rotatePolygon(polygon,theta):

    rotatedPolygon = []
    for corner in polygon :
        rotatedPolygon.append(( corner[0]*cos(theta)-corner[1]*sin(theta) , corner[0]*sin(theta)+corner[1]*cos(theta)) )
    return rotatedPolygon

def lunarLander(x, y, vx, vy, theta, thrust, g, planetThrust):
    v = sqrt(vx * vx + vy * vy)
    g = 1.622
    dt = 0.1  

    #theta = uniform(0, pi/2)
    thrustX = -thrust * cos(theta)
    thrustY = -thrust * sin(theta)
    #thrust = sqrt(thrustX * thrustX + thrustY * thrustY)
    ax = thrustX
    ay = thrustY + g
    x = x + vx * dt
    y = y + vy * dt
    vx = vx + ax * dt
    vy = vy + ay * dt
    v = sqrt(vx * vx + vy * vy)
               
    return x, y, vx, vy


def main():
    planet = input("Enter a planet or moon name to set the environment of your landing: ")
    g, placeThrust = location(planet)
    x = 100 # initial x location
    y = 150 # initial y location
    w = 15  #width of spaceship body
    h = 15  #height of spaceship body
    vx = 15 #initial x velocity
    vy = 0 # initial y velocity
    fuel = 1000  
    score = 0
        
    winsizeX = 1000
    winsizeY = 700
    
    # initializing color rgb definitions
    black = (0, 0, 0)
    grey = (192, 192, 192)
    white = (255, 255, 255)

    # create array of random coordinates for 25 stars
    starsX = []
    starsY = []
    
    i = 0
    while i < 25 : 
        starsX.append(randrange(0, winsizeX))
        starsY.append(randrange(0, winsizeY - 40))
        i += 1

    #spaceship corners and important points
    a = -w/2
    b = -h/2
    c = w/2
    d = h/2
    k = a+3
    l = c-3
    m = b-3
    n = c + 4
    p = a - 4
    q = -0.5
    r = 0.5
    s = d + 5
    
    #initializing and setting up pygame windows and functions
    pygame.init()
    pygame.display.set_caption('Lunar Lander')
    size = [winsizeX, winsizeY]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    
    #initializing and defining fixed text
    font = pygame.font.SysFont("sebastiangothicNBP", 15)
    font1 = pygame.font.SysFont("sebastiangothicNBP", 12)
    font2 = pygame.font.SysFont("sebastiangothicNBP", 20)
    
    # by default the key repeat is disabled
    # call set_repeat() to enable it
    pygame.key.set_repeat(50, 50)

    #start page
    while True:
        #intro page text and display
        startTitle = font2.render("WELCOME TO LUNAR LANDER", 1, white)
        startText1 = font.render("INSERT COINS", 1, white)
        startText2 = font.render("CLICK TO PLAY", 1, white)
        startText3 = font.render("ARROW KEYS TO MOVE", 1, white)
        textNames = font1.render("SCIENTIFIC PROGRAMMING IN BME FINAL PROJECT: BY JEESOO KIM, JAE LEE, SARAH LEE", 1, white)
        textPName = font1.render("YOU ARE PLAYING ON ", 1, white)
        planetName = font1.render(planet.upper(), 1, white)

        screen.blit(startTitle, (winsizeX/2 - 180, 150))
        screen.blit(startText1, (winsizeX/2 - 80, winsizeY/2 - 80))
        screen.blit(startText2, (winsizeX/2 - 83, winsizeY/2 - 40))
        screen.blit(startText3, (winsizeX/2 - 107, winsizeY/2 - 18)) 
        screen.blit(textNames, (winsizeX - 985, winsizeY - 25))
        screen.blit(textPName, (winsizeX/2 - 130, 180))
        screen.blit(planetName, (winsizeX/2 + 20, 180))
        
        pygame.draw.line(screen, white, (0, winsizeY - 40), (winsizeX, winsizeY - 40), 2)
        
        # draw stars
        i = 0
        while i < 20:
            pygame.draw.circle(screen, white, (starsX[i], starsY[i]), 1)
            i += 1            
            
        #wait until mouse is clicked to proceed with game 
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            break
        elif event.type == pygame.QUIT:
            pygame.quit()
        
        # draw everything
        pygame.display.update()
    
    run = False                
    while fuel > 0 and run == False:        
        fuel, score, run, check = gamePlay(fuel, placeThrust, score, g, planet, winsizeX, winsizeY, screen, black, white, grey, a,b,c,d,k,l,m,n,p,q,r,s, starsX, starsY, font, font1, font2, h, w, clock)
        if check == 1:
            run == True

main()


    


