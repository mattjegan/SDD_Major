## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 26th August 2013

## Import all needed libraries

## Built-ins
import os
import sys
import time
import datetime
import string
import random

## Externals
import pygame
from bw_Cons import *
from pygame.locals import *

## Class used for button detection
class Button:
    ## Initialisation method
    def __init__(self, image, topPos):
        ## Set top left corner values
        self.x = topPos[0]
        self.y = topPos[1]
        ## Set dimensional values
        self.x_len = image.get_width()
        self.y_len = image.get_height()
    ## Compares pos to the location of the ScreenImage instance
    def checkTouch(self, pos): 
        mos_x, mos_y = pos[0], pos[1]
        ## Determine whether por not pos is inside the image
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

## Displays the title screen and handles related actions
def displayTitleScreen(screen):
    mouseDown = False
    ## Event Loop
    for event in pygame.event.get():
        ## Check Quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ## Check MouseDown event
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
    
    ## Set image paths
    bgImageSrc = "rsrc/large/title_BG.png"
    bwTextSrc = "rsrc/large/title_Text.png"
    loginSrc = "rsrc/large/title_Login.png"
    createSrc = "rsrc/large/title_CreateAcc.png"
    leaderSrc = "rsrc/large/title_Leaderboards.png"
    helpSrc = "rsrc/large/title_Help.png"
    exitSrc = "rsrc/large/title_Exit.png"

    ## Set image positions
    loginPos = LRG_LOGIN_POS
    createPos = LRG_CREATE_POS
    leaderPos = LRG_LEADER_POS
    helpPos = LRG_HELP_POS
    exitPos = LRG_EXIT_POS

    ## Load Images
    ## Convert alpha allows transparent background (png)
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    bwText = pygame.image.load(bwTextSrc).convert_alpha()
    loginImg = pygame.image.load(loginSrc).convert_alpha()
    createImg = pygame.image.load(createSrc).convert_alpha() 
    leaderImg = pygame.image.load(leaderSrc).convert_alpha()
    helpImg = pygame.image.load(helpSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    ## Create Buttons
    loginBtn = Button(loginImg, loginPos)
    createBtn = Button(createImg, createPos)
    leaderBtn = Button(leaderImg, leaderPos)
    helpBtn = Button(helpImg, helpPos)
    exitBtn = Button(exitImg, exitPos)

    ## Get mouse position
    mousePos = pygame.mouse.get_pos()

    ## Evaluate Actions
    if mouseDown:
        if loginBtn.checkTouch(mousePos): screenToGo = LOGIN
        elif createBtn.checkTouch(mousePos): screenToGo = NEWUSER
        elif leaderBtn.checkTouch(mousePos): screenToGo = HIGHSCORES
        elif helpBtn.checkTouch(mousePos): screenToGo = HELP
        elif exitBtn.checkTouch(mousePos): screenToGo = EXITGAME
        else: screenToGo = TITLE
    else: screenToGo = TITLE

    ## Render the screen
    screen.blit(bgImage, ORIGIN)

    screen.blit(bwText, LRG_TITLE_POS)
    screen.blit(loginImg, LRG_LOGIN_POS)
    screen.blit(createImg, LRG_CREATE_POS)
    screen.blit(leaderImg, LRG_LEADER_POS)
    screen.blit(helpImg, LRG_HELP_POS)
    screen.blit(exitImg, LRG_EXIT_POS)

    return screenToGo

## Displays the login screen and handles related actions
def displayLoginScreen(screen, username, password, onUserField, onPassField, hide):
    mouseDown = False
    ## Event Loop
    for event in pygame.event.get():
        ## Check Quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ## Check MouseDown event
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
        ## Check KeyDown event
        elif event.type == KEYDOWN:
            ## Check modifiers (shift, capslock etc.)
            mods = pygame.key.get_mods()        
            if mods & KMOD_LSHIFT and event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += string.upper(str(pygame.key.name(event.key)))
                elif onPassField:
                    password += string.upper(str(pygame.key.name(event.key)))
            ## Check without modifiers
            elif event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += str(pygame.key.name(event.key))
                elif onPassField:
                    password += str(pygame.key.name(event.key))
            elif event.key == K_BACKSPACE:
                if onUserField: username = username[:-1]
                elif onPassField: password = password[:-1]

    ## Set image paths
    bgImageSrc = "rsrc/large/title_BG.png"
    loginTextSrc = "rsrc/large/login_Text.png"
    usernameSrc = "rsrc/large/login_Username.png"
    passwordSrc = "rsrc/large/login_Password.png"
    fieldSrc = "rsrc/large/login_Field.png"
    confirmSrc = "rsrc/large/login_Confirm.png"
    exitSrc = "rsrc/large/title_Exit.png"
    tickBoxSrc = "rsrc/large/tickBox.png"

    ## Set image positions
    field1Pos = LRG_LOGIN_FIELD1_POS
    field2Pos = LRG_LOGIN_FIELD2_POS
    confirmPos = LRG_LOGIN_CONFIRM_POS
    exitPos = LRG_LOGIN_EXIT_POS
    tickBoxPos = LRG_TICKBOX

    ## Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    loginTextImg = pygame.image.load(loginTextSrc).convert_alpha()
    usernameImg = pygame.image.load(usernameSrc).convert_alpha()
    passwordImg = pygame.image.load(passwordSrc).convert_alpha()
    fieldImg = pygame.image.load(fieldSrc).convert_alpha()
    confirmImg = pygame.image.load(confirmSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()
    tickBoxImg = pygame.image.load(tickBoxSrc).convert_alpha()

    ## Load Letters
    letterDict = {} ## A->Z->a->z filled
    for letterFile in os.listdir("rsrc/large/alphabet"):
        if letterFile == "asterisk.png":
            asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
        ## Filter files in directory
        elif letterFile[0] != "." and letterFile[-3:] != ".py":
            newLetterPath = "rsrc/large/alphabet/" + letterFile
            newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
            letterDict[letterFile[2]] = newLetterImage

    ## Create buttons
    field1Btn = Button(fieldImg, field1Pos)
    field2Btn = Button(fieldImg, field2Pos)
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)
    tickBoxBtn = Button(tickBoxImg, tickBoxPos)

    ## Get mouse position
    mousePos = pygame.mouse.get_pos()

    ## Evaluate Actions
    screenToGo = LOGIN
    if mouseDown:
        if field1Btn.checkTouch(mousePos): onUserField = True; onPassField = False
        elif field2Btn.checkTouch(mousePos): onPassField = True; onUserField = False
        elif confirmBtn.checkTouch(mousePos): 
            onUserField = False
            onPassField = False
            if checkLogin(username, password):
                screenToGo = GAME
            else:
                screenToGo = TITLE
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        ## Check hide button
        elif tickBoxBtn.checkTouch(mousePos): 
            if hide == False:
                hide = True
            else:
                hide = False
        else: onUserField = False; onPassField = False; screenToGo = LOGIN

    # Render screen
    screen.blit(bgImage, ORIGIN)

    screen.blit(loginTextImg, LRG_LOGIN_TITLE_POS)
    screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
    screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
    screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
    screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)
    screen.blit(tickBoxImg, LRG_TICKBOX)

    ## Render text
    if hide == True:
    	screen.blit(asteriskImage, LRG_CHK_AST)

    ## Render username
    totalWidth = 0
    for e, letter in enumerate(username):
        screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
        totalWidth += letterDict[letter].get_width()

    ## Render password
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

    return screenToGo, username, password, onUserField, onPassField, hide

## Confirms if the username and password exist in the user file
def checkLogin(username, password):
    ## Open file for reading and convert to array
    userFile = open("userFile.txt", "rU")
    userData = [line for line in userFile]
    userFile.close()

    isValid = False
    ## Check if any matches occur
    for line in userData:
        scannedUser, scannedPass = line.strip("\n").split(";")
        if scannedUser == username and scannedPass == password:
            isValid = True
            break

    return isValid

## Displays the new user screen and handles related actions
def displayNewUserScreen(screen, username, password, onUserField, onPassField):
    mouseDown = False
    hide = True
    ## Event Loop
    for event in pygame.event.get():
        ## Check Quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ## Check MouseDown event
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True
        ## Check KeyDown event
        elif event.type == KEYDOWN:
            ## Check Modifiers (shift, capslock etc.)
            mods = pygame.key.get_mods()        
            if mods & KMOD_LSHIFT and event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += string.upper(str(pygame.key.name(event.key)))
                elif onPassField:
                    password += string.upper(str(pygame.key.name(event.key)))
            ## Check without modifiers
            elif event.key <= K_z and event.key >= K_a:
                if onUserField:
                    username += str(pygame.key.name(event.key))
                elif onPassField:
                    password += str(pygame.key.name(event.key))
            elif event.key == K_BACKSPACE:
                if onUserField: username = username[:-1]
                elif onPassField: password = password[:-1]

    ## Set image paths
    bgImageSrc = "rsrc/large/title_BG.png"
    newUserTextSrc = "rsrc/large/createAcc_Text.png"
    usernameSrc = "rsrc/large/login_Username.png"
    passwordSrc = "rsrc/large/login_Password.png"
    fieldSrc = "rsrc/large/login_Field.png"
    confirmSrc = "rsrc/large/login_Confirm.png"
    exitSrc = "rsrc/large/title_Exit.png"

    ## Set image positions
    field1Pos = LRG_LOGIN_FIELD1_POS
    field2Pos = LRG_LOGIN_FIELD2_POS
    confirmPos = LRG_LOGIN_CONFIRM_POS
    exitPos = LRG_LOGIN_EXIT_POS

    ## Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    newUserTextImg = pygame.image.load(newUserTextSrc).convert_alpha()
    usernameImg = pygame.image.load(usernameSrc).convert_alpha()
    passwordImg = pygame.image.load(passwordSrc).convert_alpha()
    fieldImg = pygame.image.load(fieldSrc).convert_alpha()
    confirmImg = pygame.image.load(confirmSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    ## Load Letters
    letterDict = {} ## A->Z->a->z filled
    for letterFile in os.listdir("rsrc/large/alphabet"):
        if letterFile == "asterisk.png":
            asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
        ## Filter files in directory
        elif letterFile[0] != "." and letterFile[-3:] != ".py":
            newLetterPath = "rsrc/large/alphabet/" + letterFile
            newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
            letterDict[letterFile[2]] = newLetterImage

    ## Create buttons
    field1Btn = Button(fieldImg, field1Pos)
    field2Btn = Button(fieldImg, field2Pos)
    confirmBtn = Button(confirmImg, confirmPos)
    exitBtn = Button(exitImg, exitPos)

    ## Get mouse position
    mousePos = pygame.mouse.get_pos()

    ## Evaluate Actions
    screenToGo = NEWUSER
    if mouseDown:
        if field1Btn.checkTouch(mousePos): onUserField = True; onPassField = False
        elif field2Btn.checkTouch(mousePos): onPassField = True; onUserField = False
        elif confirmBtn.checkTouch(mousePos) and username != "" and password != "": 
            onUserField = False
            onPassField = False
            isValid = checkValidUser(username, password)
            if isValid == True: storeNewUser(username, password); screenToGo = GAME
            elif isValid == False: pass
            elif isValid == 2: pass 
            screenToGo = TITLE
        elif exitBtn.checkTouch(mousePos): screenToGo = TITLE
        else: onUserField = False; onPassField = False; screenToGo = NEWUSER
    

    ## Render Screen
    screen.blit(bgImage, ORIGIN)

    screen.blit(newUserTextImg, LRG_NEWUSER_TITLE_POS)
    screen.blit(usernameImg, LRG_LOGIN_USERNAME_POS)
    screen.blit(fieldImg, LRG_LOGIN_FIELD1_POS)
    screen.blit(passwordImg, LRG_LOGIN_PASSWORD_POS)
    screen.blit(fieldImg, LRG_LOGIN_FIELD2_POS)

    ## Render username
    totalWidth = 0
    for e, letter in enumerate(username):
        screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
        totalWidth += letterDict[letter].get_width()

    ## Render password
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

    return screenToGo, username, password, onUserField, onPassField

## Confirms if the username and password are of appropriate length
def checkValidUser(username, password):
    isValid = False

    ## Test lengths of username and password to both be > 6
    if len(username) >= 6 and len(password) >= 6: isValid = True
    elif len(username) < 6: isValid = 2
    elif len(password) < 6: isValid = 0
    return isValid

## Writes a new user profile to the user file
def storeNewUser(username, password):
    ## Open file for appending
    userFile = open("userFile.txt", "a")
    ## Append user profile
    userFile.write(username+";"+password+"\n")
    ## Close file
    userFile.close()

## Displays the help screen and handles related actions
def displayHelpScreen(screen):
    mouseDown = False
    ## Event Loop
    for event in pygame.event.get():
        ## Check Quit event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ## Check MouseDown event
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = True

    ## Set image paths
    bgImageSrc = "rsrc/large/title_BG.png"
    helpTxtSrc = "rsrc/large/help_Text.png"
    helpBodySrc = "rsrc/large/help_Body.png"
    helpDoneSrc = "rsrc/large/help_Done.png"

    ## Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha()
    helpTxtImg = pygame.image.load(helpTxtSrc).convert_alpha()
    helpBodyImg = pygame.image.load(helpBodySrc).convert_alpha()
    helpDoneImg = pygame.image.load(helpDoneSrc).convert_alpha()

    ## Create Buttons
    doneBtn = Button(helpDoneImg, LRG_HELP_DONE_POS)

    ## Evaluate Actions
    mousePos = pygame.mouse.get_pos()
    if mouseDown:
        if doneBtn.checkTouch(mousePos): screenToGo = TITLE
        else: screenToGo = HELP
    else: screenToGo = HELP

    ## Render screen
    screen.blit(bgImage, ORIGIN)

    screen.blit(helpTxtImg, LRG_HELP_TITLE_POS)
    screen.blit(helpBodyImg, LRG_HELP_BODY_POS)
    screen.blit(helpDoneImg, LRG_HELP_DONE_POS)

    return screenToGo

## Sequentially runs the game process
def playGame(screen, user):
    ## Start game
    score = playScrollingTextGame(screen)

    ## Submit score
    submitScore(user, score, "scores_alltime.txt")

    ## Start store screen
    avatar = openStoreScreen(screen, score)

    ## Start final screen
    playBattleScene(screen, avatar)
    screenToGo = TITLE
    return screenToGo

## Displays the main game screen and handles related actions
def playScrollingTextGame(screen):
    running = True
    score = 0

    ## Create array of words to type
    wordList = readFileIntoArray("wordList.txt")
    wordList = wordList[0].split("\r")
    for e, word in enumerate(wordList):
        wordList[e] = word.strip()

    ## Make array pseudo-random
    wordList = sattoloShuffle(wordList)

    ## Create timer
    startTime = time.time()
    
    currentWord = ""
    wordOnScreen = ""
    newWord = True

    ## Game Loop
    while running:
        ## Event Loop
        for event in pygame.event.get():
            ## Check Quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            ## Check KeyDown event
            elif event.type == KEYDOWN:    
                if event.key <= K_z and event.key >= K_a:
                        currentWord += str(pygame.key.name(event.key))
                elif event.key == K_BACKSPACE:
                    currentWord = currentWord[:-1]

        ## Set background image path
        bgImageSrc = "rsrc/large/title_BG.png"

        ## Load background image
        bgImage = pygame.image.load(bgImageSrc).convert_alpha()

        ## Check whether a new word needs to be chosen
        if newWord:
            wordOnScreen = wordList[score]
            wordList.remove(wordOnScreen)
            newWord = False

        ## Load Letters
        letterDict = {} ## A->Z->a->z filled
        for letterFile in os.listdir("rsrc/large/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
            ## Filter files in directory
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/large/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage
        
        ## Load Numbers
        numberDict = {} ## 1->9->0 filled
        for numberFile in os.listdir("rsrc/large/numbers"):
            if numberFile[0] != "y": ## b: yellow numbers; y: blue numbers
                newNumberPath = "rsrc/large/numbers/" + numberFile
                newNumberImage = pygame.image.load(newNumberPath).convert_alpha()
                numberDict[numberFile[1]] = newNumberImage
        
        ## Set image paths
        barSrc = "rsrc/large/game_Bar.png"
        fieldSrc = "rsrc/large/game_Field.png"
        typewordSrc = "rsrc/large/game_TypeWord.png"
        clockSrc = "rsrc/large/game_Clock.png"
            
        ## Load images
        barImg = pygame.image.load(barSrc).convert_alpha()
        fieldImg = pygame.image.load(fieldSrc).convert_alpha()
        typewordImg = pygame.image.load(typewordSrc).convert_alpha()
        clockImg = pygame.image.load(clockSrc).convert_alpha()
        
        ## Render background image
        screen.blit(bgImage, ORIGIN)

        ## Convert timer to count down
        currentTime = time.time()
        elapsedTime = currentTime - startTime
        if elapsedTime >= 30:
            running = False

        ## Render screen
        screen.blit(barImg, LRG_GAME_BAR)
        screen.blit(fieldImg, LRG_GAME_FIELD)
        screen.blit(typewordImg, LRG_GAME_TYPE)
        screen.blit(clockImg, LRG_GAME_CLOCK)
                          
        ## Render current word to type
        totalWidth = 0
        for e, letter in enumerate(wordOnScreen):
            screen.blit(letterDict[letter], (LRG_USERNAME_START_POS[0] + totalWidth, LRG_USERNAME_START_POS[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()
    
        ## Render current typing progress of word
        totalWidth = 0
        for e, letter in enumerate(currentWord):
            screen.blit(letterDict[letter], (LRG_GAME_CRTWORD[0] + totalWidth, LRG_GAME_CRTWORD[1] - letterDict[letter].get_height()))
            totalWidth += letterDict[letter].get_width()
            
        ## Render score
        totalWidth = 0
        for e, number in enumerate(str(int(30-elapsedTime))):
            screen.blit(numberDict[number], (LRG_GAME_CLOCK[0]+25 + totalWidth, LRG_GAME_CLOCK[1]+20+(94/2) - numberDict[number].get_height()))
            totalWidth += numberDict[number].get_width()
        
        ## Check if word has been completely typed
        if currentWord == wordOnScreen:
            newWord = True
            currentWord = ""
            score += 1     

        ## Update screen
        pygame.display.update()

    return score

## Reads a file into an array
def readFileIntoArray(fileName):
    ## For files that exist
    try:
        ## Open file
        f = open(fileName)
        ## Read file into array via list comprehension
        array = [line for line in f]
        ## Close file
        f.close()
    ## For files that do not exist
    except:
        array = None
    return array

## Shuffles an array in place
def sattoloShuffle(array):
    ## Get length of array
    i = len(array)

    ## Loop through array backwards
    while i > 1:
        i -= 1
        j = random.randint(0, i)
        ## Swap array[j] with array[i] in place
        array[j], array[i] = array[i], array[j]
    return array

## Displays plain text on screen
## Used for debugging purposes only
def writeText(screen, text, location):
    ## Initialise font engine
    pygame.font.init()

    ## Define font and size
    font = pygame.font.Font(None, 16)

    ## Create screen object
    obj = font.render(text, 1, (0,0,0))

    ## Render text on screen
    screen.blit(obj, location)

## Class used to store different user attributes
class Avatar:
    ## Initialisation method
    def __init__(self, attack, armor, magic):
        self.attack = attack
        self.armor = armor
        self.magic = magic

    ## Display stats in order
    ## Used only for debugging
    def displayStats(self):
        print self.attack, self.armor, self.magic
        
## Displays the store screen and handles related actions
def openStoreScreen(screen, score):
    mouseDown = False
    running = True
    points = score
    avatar = Avatar(0, 0, 0)

    while running:
        ## Event Loop
        for event in pygame.event.get():
            ## Check Quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            ## Check MouseDown event
            elif event.type == MOUSEBUTTONDOWN:
                mouseDown = True
                
        ## Set image paths
        bgImageSrc = "rsrc/large/title_BG.png"
        storeTextSrc = "rsrc/large/sText.png"
        attackSrc = "rsrc/large/attack.png"
        armorSrc = "rsrc/large/armor.png"
        magicSrc = "rsrc/large/magic.png"
        pointsLeftSrc = "rsrc/large/pointsLeft.png"
        storeBodySrc = "rsrc/large/sBody.png"
        storePlusSrc = "rsrc/large/plusBox.png"
        doneSrc = "rsrc/large/help_Done.png"

        ## Load images
        doneImg = pygame.image.load(doneSrc).convert_alpha()
        bgImage = pygame.image.load(bgImageSrc).convert_alpha()
        storeText = pygame.image.load(storeTextSrc).convert_alpha()
        attackImg = pygame.image.load(attackSrc).convert_alpha()
        armorImg = pygame.image.load(armorSrc).convert_alpha()
        magicImg = pygame.image.load(magicSrc).convert_alpha()
        pointsLeftImg = pygame.image.load(pointsLeftSrc).convert_alpha()
        storeBodyImg = pygame.image.load(storeBodySrc).convert_alpha()
        storePlusImg = pygame.image.load(storePlusSrc).convert_alpha()       
                
        ## Load Numbers
        numberDict = {} ## 1->9->0 filled
        for numberFile in os.listdir("rsrc/large/numbers"):
            if numberFile[0] != "y": ## b: yellow numbers; y: blue numbers
                newNumberPath = "rsrc/large/numbers/" + numberFile
                newNumberImage = pygame.image.load(newNumberPath).convert_alpha()
                numberDict[numberFile[1]] = newNumberImage

        ## Create Buttons
        doneBtn = Button(doneImg, LRG_STORE_DONE_POS)
        attBtn = Button(storePlusImg, LRG_ATK_PLS_POS)
        arrBtn = Button(storePlusImg, LRG_ARR_PLS_POS)
        magBtn = Button(storePlusImg, LRG_MAG_PLS_POS)

        ## Evaluate Actions
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

        ## Render Screen
        screen.blit(bgImage, ORIGIN)
                
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

        ## Render points left
        totalWidth = 0
        for e, number in enumerate(str(score)):
            screen.blit(numberDict[number], (LRG_PTNSLFT_POS[0]+100 + totalWidth, LRG_PTNSLFT_POS[1]+100 - numberDict[number].get_height()))
            totalWidth += numberDict[number].get_width()

        ## Render attack
        totalWidth = 0
        for e, number in enumerate(str(avatar.attack)):
            screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_ATK_PLS_POS[1]+10))
            totalWidth += numberDict[number].get_width()

        ## Render armor
        totalWidth = 0
        for e, number in enumerate(str(avatar.armor)):
            screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_ARR_PLS_POS[1]+10))
            totalWidth += numberDict[number].get_width()

        ## Render magic
        totalWidth = 0
        for e, number in enumerate(str(avatar.magic)):
            screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, LRG_MAG_PLS_POS[1]+10))
            totalWidth += numberDict[number].get_width()    
                
        ## Update screen
        pygame.display.update()
    return avatar

## Displays the final screen
def playBattleScene(screen, avatar):
    startTime = time.time()
    running = True
    while running:

        ## Load Letters
        letterDict = {} ## A->Z->a->z filled
        for letterFile in os.listdir("rsrc/large/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
            ## Filter files in directory
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/large/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage

        ## Load background image and render
        bgImageSrc = "rsrc/large/title_BG.png"
        bgImage = pygame.image.load(bgImageSrc).convert_alpha()
        screen.blit(bgImage, ORIGIN)

        ## Create message
        msg = "Congratulations"
        totalWidth = 0
        for letter in msg:
            screen.blit(letterDict[letter], (LRG_LOGIN_POS[0] + totalWidth, (LRG_MAG_PLS_POS[1]-70)))
            totalWidth += letterDict[letter].get_width()

        if avatar.attack > avatar.armor and avatar.attack > avatar.magic: msg = "You are a warrior"
        elif avatar.armor > avatar.attack and avatar.armor > avatar.magic: msg = "You are a shieldman"
        elif avatar.magic > avatar.attack and avatar.magic > avatar.armor: msg = "You are a mage"
        else: msg = "You are awesome"

        ## Render message
        totalWidth = 0
        for letter in msg:
            if letter != ' ':
                screen.blit(letterDict[letter], (LRG_LOGIN_POS[0] + totalWidth, (LRG_MAG_PLS_POS[1]-70+70+70)))
                totalWidth += letterDict[letter].get_width()
            else:
                totalWidth += 20

        ## Display screen for 5 seconds
        if time.time() - startTime >= 5:
            running = False

        ## Update screen
        pygame.display.update()

## Writes a users score to a score file
def submitScore(user, score, fileName):
    ## Open file for appending
    scoreFile = open(fileName, "a")
    
    ## Get current date from OS
    today = datetime.date.today()

    ## Convert date to ordinal integer
    date2rec = str(datetime.date.toordinal(today)) + ';\n'
    
    ## Scores stored in format (user; score; date)
    scoreFile.write(str(user) + ';' + str(score) + ';' + str(date2rec))
    
    ## Close file
    scoreFile.close()

## Sorts all user scores
def sortAllTimeScores(filename):
    ## Get all scores as array
    arrayOfScores = readFileIntoArray(filename)
    for e, element in enumerate(arrayOfScores):
        ## Split element into attributes - (user;score;timeAsOrdinal)
        arrayOfScores[e] = element.split(';')[:3]

    ## Sort by score - decending
    arrayOfScores.sort(key=lambda x: int(x[1]))
    arrayOfScores.reverse()
    
    ## Re-join all attributes into single element - 1D array of strings
    for e, element in enumerate(arrayOfScores):
        arrayOfScores[e] = ';'.join(element)
        arrayOfScores[e] = arrayOfScores[e] + ';\n'

    ## Overwrite file
    fileToWrite = open(filename, "w+a")
    for element in arrayOfScores:
        fileToWrite.write(element)

    ## Close file
    fileToWrite.close()

## Sorts all daily scores
def sortDailyScores(allScores, dailyScores):
    ## Get all scores as array
    arrayOfScores = readFileIntoArray(allScores)

    for e, element in enumerate(arrayOfScores):
        ## Split element into attributes - (user;score;timeAsOrdinal)
        arrayOfScores[e] = element.split(';')[:3]

    ## Find all scores that were not set today
    today = datetime.date.today()
    arrayOfIndexs = []
    for e, element in enumerate(arrayOfScores):
        if element[2] != str(datetime.date.toordinal(today)):
            arrayOfIndexs.append(e)

    ## Delete all scores that weren't set today
    ## Must be deleted in reverse order so to keep index positions
    arrayOfIndexs.reverse()
    for i in arrayOfIndexs:
        del arrayOfScores[i]

    ## Sort by score - decending
    arrayOfScores.sort(key=lambda x: int(x[1]))
    arrayOfScores.reverse()

    ## Re-join all attributes into single element - 1D array of strings
    for e, element in enumerate(arrayOfScores):
        arrayOfScores[e] = ';'.join(element)
        arrayOfScores[e] = arrayOfScores[e] + ';\n'

    ## Overwrite file
    fileToWrite = open(dailyScores, "w+a")
    for element in arrayOfScores:
        fileToWrite.write(element)

    ## Close file
    fileToWrite.close()

## Reduces score files down to 3 entries
def parseScores(filename):
    ## Get scores as array
    arrayOfScores = readFileIntoArray(filename)

    ## Open file for write and append
    fileToWrite = open(filename, "w+a")

    ## Reduce file down to 3 entries
    for e, element in enumerate(arrayOfScores):
        ## Reduce
        if len(arrayOfScores) > 3:
            if e < 3:
                fileToWrite.write(element)
            else:
                break
        ## Don't reduce
        else:
            fileToWrite.write(element)

    ## Close file
    fileToWrite.close()

## Displays the high scores screen and handles any related actions
def displayHighScores(screen):
    mouseDown = False
    running = True
    while running:
        ## Event Loop
        for event in pygame.event.get():
            ## Check Quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            ## Check MouseDown event
            elif event.type == MOUSEBUTTONDOWN:
                mouseDown = True

        ## Set image paths
        bgImageSrc = "rsrc/large/title_BG.png"
        highScoreTxtSrc = "rsrc/large/leader_Text.png"
        dailySrc = "rsrc/large/leader_Daily.png"
        allTimeSrc = "rsrc/large/leader_AllTime.png"
        userSrc = "rsrc/large/leader_Username.png"
        scoreSrc = "rsrc/large/leader_Score.png"
        barSrc = "rsrc/large/leader_Bar.png"
        doneBtnSrc = "rsrc/large/help_Done.png"

        ## Load Images
        bgImage = pygame.image.load(bgImageSrc).convert_alpha()
        highScoreImg = pygame.image.load(highScoreTxtSrc).convert_alpha()
        dailyImg = pygame.image.load(dailySrc).convert_alpha()
        allTimeImg = pygame.image.load(allTimeSrc).convert_alpha()
        userImg = pygame.image.load(userSrc).convert_alpha()
        scoreImg = pygame.image.load(scoreSrc).convert_alpha()
        barImg = pygame.image.load(barSrc).convert_alpha()
        doneBtnImg = pygame.image.load(doneBtnSrc).convert_alpha()

        ## Load Numbers
        numberDict = {} ## 1->9->0 filled
        for numberFile in os.listdir("rsrc/large/numbers"):
            if numberFile[0] != "b": ## b: yellow numbers; y: blue numbers
                newNumberPath = "rsrc/large/numbers/" + numberFile
                newNumberImage = pygame.image.load(newNumberPath).convert_alpha()
                numberDict[numberFile[1]] = newNumberImage

        ## Load Letters
        letterDict = {} ## A->Z->a->z filled
        for letterFile in os.listdir("rsrc/large/alphabet"):
            if letterFile == "asterisk.png":
                asteriskImage = pygame.image.load("rsrc/large/alphabet/asterisk.png").convert_alpha()
            ## Filter files in directory
            elif letterFile[0] != "." and letterFile[-3:] != ".py":
                newLetterPath = "rsrc/large/alphabet/" + letterFile
                newLetterImage = pygame.image.load(newLetterPath).convert_alpha()
                letterDict[letterFile[2]] = newLetterImage

        ## Create Buttons
        doneBtn = Button(doneBtnImg, LRG_HELP_DONE_POS)

        ## Evaluate Actions
        mousePos = pygame.mouse.get_pos()
        if mouseDown:
            if doneBtn.checkTouch(mousePos): 
                screenToGo = TITLE
                running = False
            mouseDown = False

        ## Render screen
        screen.blit(bgImage, ORIGIN)

        screen.blit(highScoreImg, LRG_LEADER_TITLE_POS)
        screen.blit(doneBtnImg, LRG_HELP_DONE_POS)
        
        screen.blit(dailyImg, LRG_LEADER_DAILY)
        screen.blit(userImg, LRG_LEADER_DUSER)
        screen.blit(scoreImg, LRG_LEADER_DSCORE)
        screen.blit(barImg, LRG_LEADER_DBAR)

        ## Render Daily Scores
        parseScores("scores_daily.txt")
        arrayOfScores = readFileIntoArray("scores_daily.txt")
        for e, element in enumerate(arrayOfScores):
            arrayOfScores[e] = element.split(';')

            ## Render score
            totalWidth = 0
            for number in arrayOfScores[e][1]:
                screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + totalWidth, (LRG_MAG_PLS_POS[1]-70 + (e*60))))
                totalWidth += numberDict[number].get_width()

            ## Render Username
            totalWidth = 0
            for letter in arrayOfScores[e][0]:
                screen.blit(letterDict[letter], (LRG_GAME_CRTWORD[0] + 230-470 + totalWidth, (LRG_MAG_PLS_POS[1]-70 + (e*60))))
                totalWidth += letterDict[letter].get_width()

        screen.blit(allTimeImg, LRG_LEADER_ALLTIME)
        screen.blit(userImg, LRG_LEADER_AUSER)
        screen.blit(scoreImg, LRG_LEADER_ASCORE)
        screen.blit(barImg, LRG_LEADER_ABAR)

        ## Render All Time Scores
        parseScores("scores_alltime.txt")
        arrayOfScores = readFileIntoArray("scores_alltime.txt")
        for e, element in enumerate(arrayOfScores):
            arrayOfScores[e] = element.split(';')

            ## Render Username
            totalWidth = 0
            for letter in arrayOfScores[e][0]:
                screen.blit(letterDict[letter], (LRG_GAME_CRTWORD[0] + 230 + totalWidth, (LRG_MAG_PLS_POS[1]-70 + (e*60))))
                totalWidth += letterDict[letter].get_width()

            ## Render score
            totalWidth = 0
            for number in arrayOfScores[e][1]:
                screen.blit(numberDict[number], (LRG_ATK_PLS_POS[0]-75 + 470 + totalWidth, (LRG_MAG_PLS_POS[1]-70 + (e*60))))
                totalWidth += numberDict[number].get_width()

        ## Update screen
        pygame.display.update()

    return screenToGo