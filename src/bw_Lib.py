## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 15th August 2013

import os
import sys
import time
import string
import random
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
        helpSrc = "rsrc/medium/title_Help.png"
        exitSrc = "rsrc/medium/title_Exit.png"
        loginPos = MED_LOGIN_POS
        createPos = MED_CREATE_POS
        leaderPos = MED_LEADER_POS
        helpPos = MED_HELP_POS
        exitPos = MED_EXIT_POS
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
        screen.blit(helpImg, MED_HELP_POS)
        screen.blit(exitImg, MED_EXIT_POS)
    elif size == "S":
        pass

    return screenToGo

def displayLoginScreen(screen, size, username, password, onUserField, onPassField, hide):
    mouseDown = False
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == KEYDOWN:
            mods = pygame.key.get_mods()        
            if mods & KMOD_LSHIFT and event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += string.upper(str(pygame.key.name(event.key)))
                elif onPassField:
                    password += string.upper(str(pygame.key.name(event.key)))
            elif event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += str(pygame.key.name(event.key))
                elif onPassField:
                    password += str(pygame.key.name(event.key))
            elif event.key == K_BACKSPACE:
                if onUserField: username = username[:-1]
                elif onPassField: password = password[:-1]

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
        tickBoxSrc = "rsrc/large/tickBox.png"
        field1Pos = LRG_LOGIN_FIELD1_POS
        field2Pos = LRG_LOGIN_FIELD2_POS
        confirmPos = LRG_LOGIN_CONFIRM_POS
        exitPos = LRG_LOGIN_EXIT_POS
        tickBoxPos = LRG_TICKBOX
    elif size == "M":
        bgImageSrc = "rsrc/medium/title_BG.png"
        loginTextSrc = "rsrc/medium/login_Text.png"
        usernameSrc = "rsrc/medium/login_Username.png"
        passwordSrc = "rsrc/medium/login_Password.png"
        fieldSrc = "rsrc/medium/login_Field.png"
        confirmSrc = "rsrc/medium/login_Confirm.png"
        exitSrc = "rsrc/medium/title_Exit.png"
        field1Pos = MED_LOGIN_FIELD1_POS
        field2Pos = MED_LOGIN_FIELD2_POS
        confirmPos = MED_LOGIN_CONFIRM_POS
        exitPos = MED_LOGIN_EXIT_POS
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
    tickBoxImg = pygame.image.load(tickBoxSrc).convert_alpha()

    # Load Letters
    letterDict = {} # A->Z->a->z filled
    if size == "L":
        for letterFile in os.listdir("rsrc/large/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/large/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage
    elif size == "M":
        for letterFile in os.listdir("rsrc/medium/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/medium/alphabet/asterisk.png").convert_alpha()
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/medium/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage

    # Create buttons
    field1Btn = Button(fieldImg, field1Pos)
    field2Btn = Button(fieldImg, field2Pos)
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)
    tickBoxBtn = Button(tickBoxImg, tickBoxPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    screenToGo = LOGIN
    if mouseDown:
        if field1Btn.checkTouch(mousePos): onUserField = True; onPassField = False
        elif field2Btn.checkTouch(mousePos): onPassField = True; onUserField = False
        elif confirmBtn.checkTouch(mousePos): 
            onUserField = False
            onPassField = False
            #print "Pressed Confirm"
            #print checkLogin(username, password), "username/password"
            if checkLogin(username, password):
                screenToGo = GAME
            else:
                screenToGo = TITLE
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        elif tickBoxBtn.checkTouch(mousePos): 
            if hide == False:
                hide = True
            else:
                hide = False
        else: onUserField = False; onPassField = False; screenToGo = LOGIN
    #print hide

    # Blit
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(loginTextImg, LRG_LOGIN_TITLE_POS)
        screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)
        screen.blit(tickBoxImg, LRG_TICKBOX)

        if hide == True:
        	screen.blit(asteriskImage, LRG_CHK_AST)

        totalWidth = 0
        for e, letter in enumerate(username):
            screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()

        totalWidth = 0
        for e, letter in enumerate(password):
            if hide == False:
                screen.blit(letterDict[letter], (LRG_PASSWORD_START_POS[0] + totalWidth, LRG_PASSWORD_START_POS[1] - letterDict[letter].get_height()))
                totalWidth += letterDict[letter].get_width()
            else:
                screen.blit(asteriskImage, (LRG_PASSWORD_START_POS[0] + totalWidth, LRG_PASSWORD_START_POS[1] - asteriskImage.get_height()))
                totalWidth += asteriskImage.get_width()

        screen.blit(confirmImg, LRG_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, LRG_LOGIN_EXIT_POS)
    elif size == "M":
        #screen.blit(loginTextImg, MED_LOGIN_TITLE_POS)
        screen.blit(usernameImg, MED_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, MED_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, MED_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, MED_LOGIN_FIELD2_POS)

        totalWidth = 0
        for e, letter in enumerate(username):
            screen.blit(letterDict[letter], (MED_USERNAME_START_POS[0] + totalWidth, MED_USERNAME_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()

        totalWidth = 0
        for e, letter in enumerate(password):
            if hide == False:
                screen.blit(letterDict[letter], (MED_PASSWORD_START_POS[0] + totalWidth, MED_PASSWORD_START_POS[1] - letterDict[letter].get_height()))
                totalWidth += letterDict[letter].get_width()
            else:
                screen.blit(asteriskImage, (MED_PASSWORD_START_POS[0] + totalWidth, MED_PASSWORD_START_POS[1] - asteriskImage.get_height()))
                totalWidth += asteriskImage.get_width()

        screen.blit(confirmImg, MED_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, MED_LOGIN_EXIT_POS)

    return screenToGo, username, password, onUserField, onPassField, hide

def checkLogin(username, password):
    userFile = open("userFile.txt", "rU")
    userData = [line for line in userFile]
    userFile.close()

    isValid = False
    for line in userData:
        scannedUser, scannedPass = line.strip("\n").split(";")
        if scannedUser == username and scannedPass == password:
            isValid = True
            break

    return isValid

def displayNewUserScreen(screen, size, username, password, onUserField, onPassField):
    mouseDown = False
    hide = True
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == KEYDOWN:
            mods = pygame.key.get_mods()        
            if mods & KMOD_LSHIFT and event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += string.upper(str(pygame.key.name(event.key)))
                elif onPassField:
                    password += string.upper(str(pygame.key.name(event.key)))
            elif event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += str(pygame.key.name(event.key))
                elif onPassField:
                    password += str(pygame.key.name(event.key))
            elif event.key == K_BACKSPACE:
                if onUserField: username = username[:-1]
                elif onPassField: password = password[:-1]

    # Display Debug Data
    #print onUserField, onPassField, username, password

    # Get image src
    if size == "L":
        bgImageSrc = "rsrc/large/title_BG.png"
        newUserTextSrc = "rsrc/large/createAcc_Text.png"
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
        bgImageSrc = "rsrc/medium/title_BG.png"
        newUserTextSrc = "rsrc/medium/createAcc_Text.png" # Lost file
        usernameSrc = "rsrc/medium/login_Username.png"
        passwordSrc = "rsrc/medium/login_Password.png"
        fieldSrc = "rsrc/medium/login_Field.png"
        confirmSrc = "rsrc/medium/login_Confirm.png"
        exitSrc = "rsrc/medium/title_Exit.png"
        field1Pos = MED_LOGIN_FIELD1_POS
        field2Pos = MED_LOGIN_FIELD2_POS
        confirmPos = MED_LOGIN_CONFIRM_POS
        exitPos = MED_LOGIN_EXIT_POS
    elif size == "S":
        pass

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    newUserTextImg = pygame.image.load(newUserTextSrc).convert_alpha()
    usernameImg = pygame.image.load(usernameSrc).convert_alpha()
    passwordImg = pygame.image.load(passwordSrc).convert_alpha()
    fieldImg = pygame.image.load(fieldSrc).convert_alpha()
    confirmImg = pygame.image.load(confirmSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    # Load Letters
    letterDict = {} # A->Z->a->z filled
    if size == "L":
        for letterFile in os.listdir("rsrc/large/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/large/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage
    elif size == "M":
        for letterFile in os.listdir("rsrc/medium/alphabet"):
            if letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/medium/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage

    # Create buttons
    field1Btn = Button(fieldImg, field1Pos)
    field2Btn = Button(fieldImg, field2Pos)
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)

    mousePos = pygame.mouse.get_pos()

    # Check Actions
    screenToGo = NEWUSER
    if mouseDown:
        if field1Btn.checkTouch(mousePos): onUserField = True; onPassField = False
        elif field2Btn.checkTouch(mousePos): onPassField = True; onUserField = False
        elif confirmBtn.checkTouch(mousePos) and username != "" and password != "": 
            onUserField = False
            onPassField = False
            isValid = checkValidUser(username, password)
            #print "isValid", isValid
            ## 0 = Invalid password, 1 = Valid, 2 = Invalid username
            if isValid == True: storeNewUser(username, password); screenToGo = GAME
            elif isValid == False: pass
            elif isValid == 2: pass 
            screenToGo = TITLE
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        else: onUserField = False; onPassField = False; screenToGo = NEWUSER
    

    # Blit
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(newUserTextImg, LRG_NEWUSER_TITLE_POS)
        screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)

        totalWidth = 0
        for e, letter in enumerate(username):
            screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()

        totalWidth = 0
        for e, letter in enumerate(password):
            if hide == False:
                screen.blit(letterDict[letter], (LRG_PASSWORD_START_POS[0] + totalWidth, LRG_PASSWORD_START_POS[1] - letterDict[letter].get_height()))
                totalWidth += letterDict[letter].get_width()
            else:
                screen.blit(asteriskImage, (LRG_PASSWORD_START_POS[0] + totalWidth, LRG_PASSWORD_START_POS[1] - asteriskImage.get_height()))
                totalWidth += asteriskImage.get_width()

        screen.blit(confirmImg, LRG_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, LRG_LOGIN_EXIT_POS)
    elif size == "M":
        screen.blit(newUserTextImg, MED_NEWUSER_TITLE_POS)
        screen.blit(usernameImg, MED_LOGIN_USERNAME_POS)
        screen.blit(fieldImg, MED_LOGIN_FIELD1_POS)
        screen.blit(passwordImg, MED_LOGIN_PASSWORD_POS)
        screen.blit(fieldImg, MED_LOGIN_FIELD2_POS)

        totalWidth = 0
        for e, letter in enumerate(username):
            screen.blit(letterDict[letter], (MED_USERNAME_START_POS[0] + totalWidth, MED_USERNAME_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()

        totalWidth = 0
        for e, letter in enumerate(password):
            screen.blit(letterDict[letter], (MED_PASSWORD_START_POS[0] + totalWidth, MED_PASSWORD_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()

        screen.blit(confirmImg, MED_LOGIN_CONFIRM_POS)
        screen.blit(exitImg, MED_LOGIN_EXIT_POS)

    return screenToGo, username, password, onUserField, onPassField

def checkValidUser(username, password):
    isValid = False
    if len(username) >= 6 and len(password) >= 6: isValid = True
    elif len(username) < 6: isValid = 2
    elif len(password) < 6: isValid = 0
    return isValid

def storeNewUser(username, password):
    userFile = open("userFile.txt", "a")
    userFile.write(username+";"+password+"\n")
    userFile.close()

def displayHelpScreen(screen, size):
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
        helpTxtSrc = "rsrc/large/help_Text.png"
        helpBodySrc = "rsrc/large/help_Body.png"
        helpDoneSrc = "rsrc/large/help_Done.png"
    elif size == "M":
        bgImageSrc = "rsrc/medium/title_BG.png"
        helpTxtSrc = "rsrc/medium/help_Text.png"
        helpBodySrc = "rsrc/medium/help_Body.png"
        helpDoneSrc = "rsrc/medium/help_Done.png"
    elif size == "S":
        bgImageSrc = "rsrc/small/title_BG.png"
        helpTxtSrc = "rsrc/small/help_Text.png"
        helpBodySrc = "rsrc/small/help_Body.png"
        helpDoneSrc = "rsrc/small/help_Done.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    helpTxtImg = pygame.image.load(helpTxtSrc).convert_alpha()
    helpBodyImg = pygame.image.load(helpBodySrc).convert_alpha()
    helpDoneImg = pygame.image.load(helpDoneSrc).convert_alpha()

    # Create Buttons
    if size == "L":
        doneBtn = Button(helpDoneImg, LRG_HELP_DONE_POS)
    elif size == "M":
        doneBtn = Button(helpDoneImg, MED_HELP_DONE_POS)

    # Handle Actions
    mousePos = pygame.mouse.get_pos()
    if mouseDown:
        if doneBtn.checkTouch(mousePos): screenToGo = TITLE
        else: screenToGo = HELP
    else: screenToGo = HELP

    # Render
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(helpTxtImg, LRG_HELP_TITLE_POS)
        screen.blit(helpBodyImg, LRG_HELP_BODY_POS)
        screen.blit(helpDoneImg, LRG_HELP_DONE_POS)
    elif size == "M":
        screen.blit(helpTxtImg, MED_HELP_TITLE_POS)
        screen.blit(helpBodyImg, MED_HELP_BODY_POS)
        screen.blit(helpDoneImg, MED_HELP_DONE_POS)
    elif size == "S":
        screen.blit(helpTxtImg, SML_HELP_TITLE_POS)
        screen.blit(helpBodyImg, SML_HELP_BODY_POS)
        screen.blit(helpDoneImg, SML_HELP_DONE_POS)

    return screenToGo

def playGame(screen, size):
    score = playScrollingTextGame(screen, size)
    avatar = openStoreScreen(screen, size, score)
    playBattleScene(avatar)
    submitScore(user, score)
    screenToGo = TITLE
    return screenToGo

def playScrollingTextGame(screen, size):
    running = True
    score = 0

    wordList = readFileIntoArray("wordList.txt")
    for e, word in enumerate(wordList):
        wordList[e] = word.strip("\r\n")

    wordList = sattoloShuffle(wordList)

    startTime = time.time()
    currentWord = ""
    wordOnScreen = ""
    newWord = True

    # Game Loop
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:    
                if event.key <= K_z and event.key >= K_a:
                        currentWord += str(pygame.key.name(event.key))
                elif event.key == K_BACKSPACE:
                    currentWord = currentWord[:-1]
                #print currentWord, wordOnScreen

        if size == "L":
            bgImageSrc = "rsrc/large/title_BG.png"

        bgImage = pygame.image.load(bgImageSrc).convert_alpha()

        if newWord:
            wordOnScreen = wordList[score]
            wordList.remove(wordOnScreen)
            newWord = False

        if size == "L":
            # Load Letters
            letterDict = {} # A->Z->a->z filled
            for letterFile in os.listdir("rsrc/large/alphabet"):
                if letterFile == "asterisk.png":
                    asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
                elif letterFile[0] != "." and letterFile[-3:] != ".py":
                    newLetterPath = "rsrc/large/alphabet/" + letterFile
                    newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                    letterDict[letterFile[2]] = newLetterImage
            
            # Load Numbers
            numberDict = {} # 1->9->0 filled
            for numberFile in os.listdir("rsrc/large/numbers"):
                if numberFile[0] != "y": # b: yellow; y: blue
                    newNumberPath = "rsrc/large/numbers/" + numberFile
                    newNumberImage = pygame.image.load(newNumberPath).convert_alpha()
                    numberDict[numberFile[1]] = newNumberImage
            
            barSrc = "rsrc/large/game_Bar.png"
            fieldSrc = "rsrc/large/game_Field.png"
            typewordSrc = "rsrc/large/game_TypeWord.png"
            clockSrc = "rsrc/large/game_Clock.png"
            
        elif size == "M":
            for letterFile in os.listdir("rsrc/medium/alphabet"):
                if letterFile[0] != "." and letterFile[-3:] != ".py":
                    newLetterPath = "rsrc/medium/alphabet/" + letterFile
                    newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                    letterDict[letterFile[2]] = newLetterImage

        barImg = pygame.image.load(barSrc).convert_alpha()
        fieldImg = pygame.image.load(fieldSrc).convert_alpha()
        typewordImg = pygame.image.load(typewordSrc).convert_alpha()
        clockImg = pygame.image.load(clockSrc).convert_alpha()
        
        screen.blit(bgImage, ORIGIN)

        currentTime = time.time()
        elapsedTime = currentTime - startTime
        #writeText(screen, str(elapsedTime), ORIGIN)
        if elapsedTime >= 30:
            running = False

        if size == "L":
            screen.blit(barImg, LRG_GAME_BAR)
            screen.blit(fieldImg, LRG_GAME_FIELD)
            screen.blit(typewordImg, LRG_GAME_TYPE)
            screen.blit(clockImg, LRG_GAME_CLOCK)
                              
            # Display current word to type
            totalWidth = 0
            for e, letter in enumerate(wordOnScreen):
                screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
                totalWidth += letterDict[letter].get_width()
        
            # Display current typing progress of word
            totalWidth = 0
            for e, letter in enumerate(currentWord):
                screen.blit(letterDict[letter], (LRG_GAME_CRTWORD[0] + totalWidth, LRG_GAME_CRTWORD[1] - letterDict[letter].get_height()))
                totalWidth += letterDict[letter].get_width()
                
            # Display score
            totalWidth = 0
            for e, number in enumerate(str(int(30-elapsedTime))):
                screen.blit(numberDict[number], (LRG_GAME_CLOCK[0]+25 + totalWidth, LRG_GAME_CLOCK[1]+20+(94/2) - numberDict[number].get_height()))
                totalWidth += numberDict[number].get_width()
        
        if currentWord == wordOnScreen:
            newWord = True
            currentWord = ""
            score += 1     

        pygame.display.update()
    return score

def readFileIntoArray(fileName):
    f = open(fileName)
    array = [line for line in f]
    f.close()
    return array

def sattoloShuffle(array):
    i = len(array)
    while i > 1:
        i -= 1
        j = random.randint(0, i)
        array[j], array[i] = array[i], array[j]
    return array

def writeText(screen, text, location):
    pygame.font.init()
    font = pygame.font.Font(None, 16)
    obj = font.render(text, 1, (0,0,0))
    screen.blit(obj, location)

class Avatar:
    def __init__(self, attack, armor, magic):
        self.attack = 1
        self.armor = 1
        self.magic = 1
        
def openStoreScreen(screen, size, score):
    mouseDown = False
    running = True
    points = score
    avatar = Avatar(1, 1, 1)

    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouseDown = True
                
        if size == "L":
            bgImageSrc = "rsrc/large/title_BG.png"
            storeTextSrc = "rsrc/large/sText.png"
            attackSrc = "rsrc/large/attack.png"
            armorSrc = "rsrc/large/armor.png"
            magicSrc = "rsrc/large/magic.png"
            pointsLeftSrc = "rsrc/large/pointsLeft.png"
            storeBodySrc = "rsrc/large/sBody.png"
            storePlusSrc = "rsrc/large/plusBox.png"
            doneSrc = "rsrc/large/help_Done.png"
        elif size == "M":
            bgImageSrc = "rsrc/medium/title_BG.png"
        elif size == "S":
            BgImageSrc = "rsrc/small/title_BG.png"

        doneImg = pygame.image.load(doneSrc).convert_alpha()

        bgImage = pygame.image.load(bgImageSrc).convert_alpha()
        storeText = pygame.image.load(storeTextSrc).convert_alpha()
        attackImg = pygame.image.load(attackSrc).convert_alpha()
        armorImg = pygame.image.load(armorSrc).convert_alpha()
        magicImg = pygame.image.load(magicSrc).convert_alpha()
        pointsLeftImg = pygame.image.load(pointsLeftSrc).convert_alpha()
        storeBodyImg = pygame.image.load(storeBodySrc).convert_alpha()
        storePlusImg = pygame.image.load(storePlusSrc).convert_alpha()       
                
        # Load Numbers
        numberDict = {} # A->Z->a->z filled
        if size == "L":
            for numberFile in os.listdir("rsrc/large/numbers"):
                if numberFile[0] != "y":
                    newNumberPath = "rsrc/large/numbers/" + numberFile
                    newNumberImage = pygame.image.load(newNumberPath).convert_alpha()
                    numberDict[numberFile[1]] = newNumberImage

        # Create Buttons
        if size == "L":
            doneBtn = Button(doneImg, LRG_STORE_DONE_POS)
            attBtn = Button(storePlusImg, LRG_ATK_PLS_POS)
            arrBtn = Button(storePlusImg, LRG_ARR_PLS_POS)
            magBtn = Button(storePlusImg, LRG_MAG_PLS_POS)
        elif size == "M":
            doneBtn = Button(doneImg, MED_HELP_DONE_POS)

        # Handle Actions
        mousePos = pygame.mouse.get_pos()
        if mouseDown:
            if doneBtn.checkTouch(mousePos): 
                running = False
            else:
                if score > 0:
                    if attBtn.checkTouch(mousePos):
                        avatar.attack += 1
                    elif arrBtn.checkTouch(mousePos): 
                        avatar.armor += 1
                    elif magBtn.checkTouch(mousePos): 
                        avatar.magic += 1
                    score -= 1
            mouseDown = False

        #print avatar.attack, avatar.armor, avatar.magic , score

        screen.blit(bgImage, ORIGIN)
                
        if size == "L":
            screen.blit(storeText, LRG_HELP_TITLE_POS)
            screen.blit(storeBodyImg, LRG_STORE_BODY_POS)
            screen.blit(attackImg, LRG_STORE_ATK_POS)
            screen.blit(armorImg, LRG_STORE_ARR_POS)
            screen.blit(magicImg, LRG_STORE_MAG_POS)
            screen.blit(pointsLeftImg, LRG_PTNSLFT_POS)
            screen.blit(storePlusImg, LRG_ATK_PLS_POS)
            screen.blit(storePlusImg, LRG_ARR_PLS_POS)
            screen.blit(storePlusImg, LRG_MAG_PLS_POS)
            screen.blit(doneImg, LRG_STORE_DONE_POS)

            # Display points left
            totalWidth = 0
            for e, number in enumerate(str(score)):
                screen.blit(numberDict[number], (LRG_PTNSLFT_POS[0]+100 + totalWidth, LRG_PTNSLFT_POS[1]+100 - numberDict[number].get_height()))
                totalWidth += numberDict[number].get_width()

            # Display attack
            totalWidth = 0
            for e, number in enumerate(str(avatar.attack)):
                screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_ATK_PLS_POS[1]+10))
                totalWidth += numberDict[number].get_width()

            # Display armor
            totalWidth = 0
            for e, number in enumerate(str(avatar.armor)):
                screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_ARR_PLS_POS[1]+10))
                totalWidth += numberDict[number].get_width()

            # Display magic
            totalWidth = 0
            for e, number in enumerate(str(avatar.magic)):
                screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_MAG_PLS_POS[1]+10))
                totalWidth += numberDict[number].get_width()

        #elif size == "M":
            # All elements
        #elif size == "S":
            # All elements        
                
        pygame.display.update()
    return avatar

def playBattleScene(avatar):
    pass

def submitScore(user, score, fileName):
    scoreFile = open(fileName, "r+a")
    # Get current date from OS
    # Scores stored in format (user; score; date)
    scoreFile.write(user, score, date)
    scoreFile.close()

def displayHighScores(screen, size):
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
        highScoreTxtSrc = "rsrc/large/title_leaderboards.png"
        doneBtnSrc = "rsrc/large/help_Done.png"
    elif size == "M":
        bgImageSrc = "rsrc/medium/title_BG.png"
    elif size == "S":
        bgImageSrc = "rsrc/small/title_BG.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    highScoreImg = pygame.image.load(highScoreTxtSrc).convert_alpha()
    doneBtnImg = pygame.image.load(doneBtnSrc).convert_alpha()

    # Create Buttons
    if size == "L":
        doneBtn = Button(doneBtnImg, LRG_HELP_DONE_POS)
    elif size == "M":
        doneBtn = Button(doneBtnImg, MED_HELP_DONE_POS)

    # Handle Actions
    mousePos = pygame.mouse.get_pos()
    if mouseDown:
        if doneBtn.checkTouch(mousePos): screenToGo = TITLE
        else: screenToGo = HIGHSCORES
    else: screenToGo = HIGHSCORES

    # Render
    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(highScoreImg, LRG_HELP_TITLE_POS)
        screen.blit(doneBtnImg, LRG_HELP_DONE_POS)
    elif size == "M":
        screen.blit(highScoreImg, MED_HELP_TITLE_POS)
        screen.blit(doneBtnImg, MED_HELP_DONE_POS)
    elif size == "S":
        screen.blit(highScoreImg, SML_HELP_TITLE_POS)
        screen.blit(doneBtnImg, SML_HELP_DONE_POS)

    return screenToGo