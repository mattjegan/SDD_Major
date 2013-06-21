## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 21st June 2013

import os
import sys
import time
import pygame
from bw_Cons import *
from pygame.locals import *

## Class used for button detection
class Button:
    def __init__(self, image, topPos):
        self.x = topPos[0]
        self.y = topPos[1]
        self.x_len = image.get_width()
        self.y_len = image.get_height()
    def checkTouch(self, pos): ## Compares pos to the location of the ScreenImage instance
        mos_x, mos_y = pos[0], pos[1]
        if mos_x > self.x and mos_x < self.x + self.x_len:
            x_inside = True
        else:
            x_inside = False
        if mos_y > self.y and mos_y < self.y + self.y_len:
            y_inside = True
        else:
            y_inside = False
        if x_inside and y_inside:
            return True
        else:
            return False

def displayTitleScreen(screen, size):
    mouseDown = False
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
    
    if size == "L": 
        bgImageSrc = "rsrc/large/title_BG.png"
        bwTextSrc = "rsrc/large/title_Text.png"
        loginSrc = "rsrc/large/title_Login.png"
        createSrc = "rsrc/large/title_CreateAcc.png"
        leaderSrc = "rsrc/large/title_Leaderboards.png"
        exitSrc = "rsrc/large/title_Exit.png"
        loginPos = LRG_LOGIN_POS
        createPos = LRG_CREATE_POS
        leaderPos = LRG_LEADER_POS
        exitPos = LRG_EXIT_POS
    elif size == "M":
        bgImageSrc = "rsrc/medium/title_BG.png"
        bwTextSrc = "rsrc/medium/title_Text.png"
        loginSrc = "rsrc/medium/title_Login.png"
        createSrc = "rsrc/medium/title_CreateAcc.png"
        leaderSrc = "rsrc/medium/title_Leaderboards.png"
        exitSrc = "rsrc/medium/title_Exit.png"
    elif size == "S": 
        bgImageSrc = "rsrc/smallBG.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha() # Convert alpha since png is transparent
    bwText = pygame.image.load(bwTextSrc).convert_alpha()
    loginImg = pygame.image.load(loginSrc).convert_alpha()
    createImg = pygame.image.load(createSrc).convert_alpha() 
    leaderImg = pygame.image.load(leaderSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    # Create Buttons
    loginBtn = Button(loginImg, loginPos)
    createBtn = Button(createImg, createPos)
    leaderBtn = Button(leaderImg, leaderPos)
    exitBtn = Button(exitImg, exitPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    if mouseDown:
        if loginBtn.checkTouch(mousePos): screenToGo = LOGIN
        elif createBtn.checkTouch(mousePos): screenToGo = NEWUSER
        elif leaderBtn.checkTouch(mousePos): screenToGo = HIGHSCORES
        elif exitBtn.checkTouch(mousePos): screenToGo = EXITGAME
    else: screenToGo = TITLE


    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(bwText, LRG_TITLE_POS)
        screen.blit(loginImg, LRG_LOGIN_POS)
        screen.blit(createImg, LRG_CREATE_POS)
        screen.blit(leaderImg, LRG_LEADER_POS)
        screen.blit(exitImg, LRG_EXIT_POS)
    elif size == "M":
        screen.blit(bwText, MED_TITLE_POS)
        screen.blit(loginImg, MED_LOGIN_POS)
        screen.blit(createImg, MED_CREATE_POS)
        screen.blit(leaderImg, MED_LEADER_POS)
        screen.blit(exitImg, MED_EXIT_POS)
    elif size == "S":
        pass

    return screenToGo