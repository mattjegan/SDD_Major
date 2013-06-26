## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 26th June 2013

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

def displayLoginScreen(screen, size, username, password, onUserField, onPassField):
    mouseDown = False
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == KEYDOWN:
            if event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += str(pygame.key.name(event.key))
                elif onPassField:
                    password += str(pygame.key.name(event.key))
            elif event.key == K_BACKSPACE:
                if onUserField: username = username[:-1]
                elif onPassField: password = password[:-1]
            ## Capitals
            #elif event.key <= K_z and event.key >= K_a and (event.key == K_LSHIFT or event.key == K_RSHIFT):
            #    if onUserField:
            #        username += str(pygame.key.name(event.key))
            #    elif onPassField:
            #        password += str(pygame.key.name(event.key))

    # Display Debug Data
    #print onUserField, onPassField, username, password

    # Get image src
    if size == "L":
        bgImageSrc = "rsrc/large/title_BG.png"
        loginTextSrc = "rsrc/large/login_Text.png"
        usernameSrc = "rsrc/large/login_Username.png"
        passwordSrc = "rsrc/large/login_Password.png"
        fieldSrc = "rsrc/large/login_Field.png"
        confirmSrc = "rsrc/large/login_Confirm.png"
        exitSrc = "rsrc/large/title_Exit.png"
        field1Pos = LRG_LOGIN_FIELD1_POS
        field2Pos = LRG_LOGIN_FIELD2_POS
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

    # Load Letters
    letterDict = {} # A->Z->a->z filled
    for letterFile in os.listdir("rsrc/large/alphabet"):
        if letterFile[0] != "." and letterFile[-3:] != ".py":
            newLetterPath = "rsrc/large/alphabet/" + letterFile
            newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
            letterDict[letterFile[2]] = newLetterImage
    

    # Create buttons
    field1Btn = Button(fieldImg, field1Pos)
    field2Btn = Button(fieldImg, field2Pos)
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    screenToGo = LOGIN
    if mouseDown:
        if field1Btn.checkTouch(mousePos): onUserField = True; onPassField = False
        elif field2Btn.checkTouch(mousePos): onPassField = True; onUserField = False
        elif confirmBtn.checkTouch(mousePos): onUserField = False; onPassField = False; print "Pressed Confirm"; screenToGo = TITLE
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        else: onUserField = False; onPassField = False; screenToGo = LOGIN
    

    # Blit
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(loginTextImg, LRG_LOGIN_TITLE_POS)
        screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)

        totalWidth = 0
        for e, letter in enumerate(username[::-1]):
            totalWidth += letterDict[letter].get_width()
            screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] - totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))

        totalWidth = 0
        for e, letter in enumerate(password[::-1]):
            totalWidth += letterDict[letter].get_width()
            screen.blit(letterDict[letter], (LRG_PASSWORD_START_POS[0] - totalWidth, LRG_PASSWORD_START_POS[1] - letterDict[letter].get_height()))

        screen.blit(confirmImg, LRG_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, LRG_LOGIN_EXIT_POS)

    return screenToGo, username, password, onUserField, onPassField