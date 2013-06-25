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
        helpSrc = "rsrc/large/title_Help.png"
        exitSrc = "rsrc/large/title_Exit.png"
        loginPos = LRG_LOGIN_POS
        createPos = LRG_CREATE_POS
        leaderPos = LRG_LEADER_POS
        helpPos = LRG_HELP_POS
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
    helpImg = pygame.image.load(helpSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    # Create Buttons
    loginBtn = Button(loginImg, loginPos)
    createBtn = Button(createImg, createPos)
    leaderBtn = Button(leaderImg, leaderPos)
    helpBtn = Button(helpImg, helpPos)
    exitBtn = Button(exitImg, exitPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    if mouseDown:
        if loginBtn.checkTouch(mousePos): screenToGo = LOGIN
        elif createBtn.checkTouch(mousePos): screenToGo = NEWUSER
        elif leaderBtn.checkTouch(mousePos): screenToGo = HIGHSCORES
        elif helpBtn.checkTouch(mousePos): screenToGo = HELP
        elif exitBtn.checkTouch(mousePos): screenToGo = EXITGAME
        else: screenToGo = TITLE
    else: screenToGo = TITLE


    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(bwText, LRG_TITLE_POS)
        screen.blit(loginImg, LRG_LOGIN_POS)
        screen.blit(createImg, LRG_CREATE_POS)
        screen.blit(leaderImg, LRG_LEADER_POS)
        screen.blit(helpImg, LRG_HELP_POS)
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

def displayLoginScreen(screen, size):
    mouseDown = False
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True

    # Get image src
    if size == "L":
        bgImageSrc = "rsrc/large/title_BG.png"
        loginTextSrc = "rsrc/large/login_Text.png"
        usernameSrc = "rsrc/large/login_Username.png"
        passwordSrc = "rsrc/large/login_Password.png"
        fieldSrc = "rsrc/large/login_Field.png"
        confirmSrc = "rsrc/large/login_Confirm.png"
        exitSrc = "rsrc/large/title_Exit.png"
        confirmPos = LRG_LOGIN_CONFIRM_POS
        exitPos = LRG_LOGIN_EXIT_POS
    elif size == "M":
        pass
    elif size == "S":
        pass

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    loginTextImg = pygame.image.load(loginTextSrc).convert_alpha()
    usernameImg = pygame.image.load(usernameSrc).convert_alpha()
    passwordImg = pygame.image.load(passwordSrc).convert_alpha()
    fieldImg = pygame.image.load(fieldSrc).convert_alpha()
    confirmImg = pygame.image.load(confirmSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    # Create buttons
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    if mouseDown:
        if confirmBtn.checkTouch(mousePos): print "Pressed Confirm"
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        else: screenToGo = LOGIN
    else: screenToGo = LOGIN

    # Blit
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(loginTextImg, LRG_TITLE_POS)
        screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)
        screen.blit(confirmImg, LRG_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, LRG_LOGIN_EXIT_POS)

    return screenToGo